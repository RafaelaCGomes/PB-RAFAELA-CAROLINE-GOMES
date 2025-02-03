import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, explode
from awsglue.dynamicframe import DynamicFrame
from datetime import datetime

## @params: [JOB_NAME]t
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH_JSON','S3_OUTPUT_PATH_PARQUET'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_input_path_json = args['S3_INPUT_PATH_JSON']
s3_output_path_parquet = args['S3_OUTPUT_PATH_PARQUET']


# Caminhos para as pastas
#s3_input_path_json = "s3://awsbucket-desafio/Raw/TMDB/JSON/2025/01/20/"
#caminho_parquet = "s3://awsbucket-desafio/Trusted/TMDB/Parquet/movies/2025/01/20/"

# Ler arquivos JSON
df_dynamic = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths" :[s3_input_path_json]},
        format="json",
        format_options={
            "multiline":True,
            "mode":"PERMISSIVE"})

#Converte DynamicFrame em dataframe.
df = df_dynamic.toDF()

# Remover coluna spoken_languages
df = df.drop("spoken_languages")

#explodir a coluna production_companies
exploded_df = df.withColumn("production_company", explode(col("production_companies")))

# explodir a coluna "production_countries"
exploded_df = exploded_df.withColumn("production_country", explode(col("production_countries")))

# Explodir a coluna de gêneros
exploded_df = exploded_df.withColumn("genre", explode(col("genres")))

# Criar DataFrame do primeiro Parquet - movies
parquet1_df = exploded_df.select(
    "adult",
    "backdrop_path",
    "belongs_to_collection",
    "budget",
    col("genre.id").alias("genre_id"),
    col("genre.name").alias("genre_name"),
    "homepage",
    "id",
    "imdb_id",
    "origin_country",
    "original_language",
    "original_title",
    "overview",
    "popularity",
    "poster_path",
    col("production_company.id").alias("id_production_companies"),
    "production_countries",
    col("production_countries.iso_3166_1").alias("iso_3166_1"),
    col("production_countries.name").alias("country_name"),
    "release_date",
    "revenue",
    "runtime",
    "status",
    "tagline",
    "title",
    "video",
    "vote_average",
    "vote_count"
)

# Criar DataFrame do segundo Parquet - production_companies
parquet2_df = exploded_df.select(
    col("production_company.id").alias("id_production_companies"),
    col("production_company.logo_path"),
    col("production_company.name"),
    col("production_company.origin_country")
).dropDuplicates()

#garatir que gere somente 1 parquet para cada csv
parquet1_df = parquet1_df.coalesce(1)
parquet2_df = parquet2_df.coalesce(1)

# Converter de volta para DynamicFrame
parquet1_df_dynamic = DynamicFrame.fromDF(parquet1_df, glueContext)
parquet2_df_dynamic = DynamicFrame.fromDF(parquet2_df, glueContext)


# Escreve o primeiro DynamicFrame no S3 (movies)
glueContext.write_dynamic_frame.from_options(
    frame=parquet1_df_dynamic,
    connection_type="s3",
    connection_options={"path": f"{s3_output_path_parquet}/movies"},
    format="parquet")

#Escreve o segundo DynamicFrame no s3 (production_companies)
glueContext.write_dynamic_frame.from_options(
    frame=parquet2_df_dynamic,
    connection_type="s3",
    connection_options={"path": f"{s3_output_path_parquet}/production_companies"},
    format="parquet")

job.commit()