import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, explode
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_LOCAL', 'S3_INPUT_TMDB_MOVIES', 'S3_INPUT_TMDB_COMPANIES', 'S3_OUTPUT_PATH_REFINED'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_input_local = args['S3_INPUT_LOCAL']
s3_input_TMDB_movies = args['S3_INPUT_TMDB_MOVIES']
s3_input_TMDB_companies = args['S3_INPUT_TMDB_COMPANIES']
s3_output_path_refined = args['S3_OUTPUT_PATH_REFINED']

# Ler os arquivos parquet
df_dynamic_movies_local = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths" :[s3_input_local]},
        format="parquet")

df_dynamic_tmdb_movies = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths" :[s3_input_TMDB_movies]},
        format="parquet")

df_dynamic_tmdb_companies = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths" :[s3_input_TMDB_companies]},
        format="parquet")

#Converte DynamicFrame em dataframe.
movies_local_df = df_dynamic_movies_local.toDF()
movies_tmdb_df = df_dynamic_tmdb_movies.toDF()
companies_tmdb_df = df_dynamic_tmdb_companies.toDF()


#coluna "belongs_to_collection" do movies_tmdb_df
movies_tmdb_df = movies_tmdb_df.select(
    col("*"),
    col("belongs_to_collection.id").alias("id_colecao"),
    col("belongs_to_collection.name").alias("nome_colecao")).drop("belongs_to_collection")

#coluna "revenue" do movies_tmdb_df
movies_tmdb_df = movies_tmdb_df.select(
    col("*"),
    col("revenue.int").alias("int_receita"),
    col("revenue.long").alias("long_receita")
).drop("revenue")

#Explodir a coluna production_contrie porém mantendo a relaçao entre iso e nome.
movies_tmdb_df = movies_tmdb_df.withColumn("country", explode(col("production_countries")))

# Criar DataFrame da tabela Fato_movies (parquet1)
parquet1_df = movies_tmdb_df.select(
    col("imdb_id").alias("Id_filme"),
    col("genre_id").alias("Id_genero"),
    col("id_production_companies").alias("Id_produtora"),
    col("country.iso_3166_1").alias("Iso_pais_producao"),
    col("id_colecao").alias("Id_colecao"),
    col("popularity").alias("Popularidade"),
    col("vote_average").alias("Media_votos"),
    col("vote_count").alias("Total_votos"),
    col("int_receita").alias("Receita")
)
parquet1_df = parquet1_df.dropDuplicates()


#selecionar as colunas que quero de cada df para fazer o join e formar a tabela dim_filme
df_local_selected = movies_local_df.select(
    col("id").alias("Id_filme"),
    col("tituloOriginal").alias("Titulo_original"),
    col("anoLancamento").alias("Ano_lancamento"),
    col("tempoMinutos").alias("Tempo_minutos"))

df_tmdb_selected = movies_tmdb_df.select(
    col("imdb_id").alias("Id_filme"),
    col("budget").alias("Orcamento"))

#criar Dataframe da tabela dim_filme (parquet2)
parquet2_df= df_local_selected.join(df_tmdb_selected, on="Id_filme", how="inner")

#retirar duplicatas de dim_filme
parquet2_df = parquet2_df.dropDuplicates(["Id_filme"])


#criar Dataframe da tabela dim_gereno (parquet3)
parquet3_df = movies_tmdb_df.select(
    col("genre_id").alias("Id_genero"),
    col("genre_name").alias("Nome_genero")).dropDuplicates()

# Criar DataFrame da tabela dim_produtora (parquet4)
parquet4_df = companies_tmdb_df.select(
    col("id_production_companies").alias("Id_produtora"),
    col("name").alias("Nome_produtora"),
    col("origin_country").alias("Pais_origem")).dropDuplicates()

#criar Dataframe da tabela dim_pais_producao (parquet5)
parquet5_df = movies_tmdb_df.select(
    col("country.iso_3166_1").alias("Iso_pais_producao"),
    col("country.name").alias("Nome_pais")).dropDuplicates()


#criar Dataframe da tabela dim_colecao (parquet6)
parquet6_df = movies_tmdb_df.select(
    col("id_colecao").alias("Id_colecao"),
    col("nome_colecao").alias("Nome_colecao")).dropDuplicates()

#garantir somente um parquet
parquet1_df = parquet1_df.coalesce(1)
parquet2_df = parquet2_df.coalesce(1)
parquet3_df = parquet3_df.coalesce(1)
parquet4_df = parquet4_df.coalesce(1)
parquet5_df = parquet5_df.coalesce(1)
parquet6_df = parquet6_df.coalesce(1)

#dicionario para nomes da tabela e o df
dataframes = {
    "fato_movies": parquet1_df,
    "dim_filme": parquet2_df,
    "dim_genero": parquet3_df,
    "dim_produtora": parquet4_df,
    "dim_pais_producao": parquet5_df,
    "dim_colecao": parquet6_df
}

#converter de volta para DynamicFrame
dynamic_frames = {name: DynamicFrame.fromDF(df, glueContext) for name, df in dataframes.items()}

#salvar cada parquet em uma pasta do s3
output_paths = {name: f"{s3_output_path_refined}/{name}" for name in dataframes}

for name, dynamic_frame in dynamic_frames.items():
    glueContext.write_dynamic_frame.from_options(
        frame=dynamic_frame,
        connection_type="s3",
        connection_options={"path": output_paths[name]},
        format="parquet"
    )


job.commit()