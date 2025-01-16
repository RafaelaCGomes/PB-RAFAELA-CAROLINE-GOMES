import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import upper
from pyspark.sql import functions
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths" :[
            source_file
        ]
    },
    "csv",
    {"withHeader" : True, "separator": "," },
    )

# Imprime o schema do df.
df.printSchema()

#Converte DynamicFrame em dataframe.
df = df.toDF()

#Alterar a caixa de valores de nome para MAIUSCULO.
df_maiusculo = df.withColumn("nome", upper(df["nome"]))

#Imprimir a contagem de linhas presentes no dataframe.
contagem_linhas = df_maiusculo.count()
print(f"Contagem de linhas: {contagem_linhas}")

#Imprimir a contagem de nomes, agrupando os dados do df pelas colunas ano e sexo.
df_agrupado_ano_s = df_maiusculo.groupBy("ano", "sexo", "nome").agg(functions.count("nome").alias("contagem"))
print("Contagem de nomes, agrupado por ano e sexo")
df_agrupado_ano_s.show()

#Ordenar os dados de modo que o ano mais recente apareça como primeiro registro no df.
df_ordenado = df_agrupado_ano_s.orderBy(functions.col("ano").desc())
print("Ordem dos dados por ano mais recente")
df_ordenado.show()


#Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.
df_feminino = df_maiusculo.filter(df_maiusculo.sexo == "F")# Apenas os registros de sexo feminino
df_agrupado_feminino = df_feminino.groupBy("ano", "nome").agg(functions.count("nome").alias("contagem"))
df_resultado_fem = df_agrupado_feminino.orderBy(functions.col("contagem").desc()).limit(1)
print("Nome feminino com mais registros e em que ano ocorreu:")
df_resultado_fem.show()


#Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu.
df_masculino = df_maiusculo.filter(df_maiusculo.sexo == "M")
df_agrupado_masculino = df_masculino.groupBy("ano", "nome").agg(functions.count("nome").alias("contagem"))
df_resultado_mas = df_agrupado_masculino.orderBy(functions.col("contagem").desc()).limit(1)
print('Nome masculino com mais registros e em que ano ocorreu')
df_resultado_mas.show()


#Apresentar o total de registros (masculinos e femininos) para cada ano presente no df.
#(considerar apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente)
df_agrupado_ano = df_maiusculo.groupBy("ano").agg(functions.count("*").alias("total_registros"))
df_ordenado_ano = df_agrupado_ano.orderBy(functions.col("ano").asc())
df_top_10_anos = df_ordenado_ano.limit(10)
print("Total de registros (masculinos e femininos) para cada ano presente no df.")
df_top_10_anos.show()


# Converter de volta para DynamicFrame
df_maiusculo_dy = DynamicFrame.fromDF(df_maiusculo, glueContext, "df_maiusculo")

#Escrever o conteudo do df com os valores de nome em maiúsculo 
#gravação deve ocorrer no subdir frequencia_registros_nomes_eua 
#formato JSON
#Particionamento deve ocorrer pelas colunas sexo e ano

glueContext.write_dynamic_frame.from_options(
    frame=df_maiusculo_dy,
    connection_type="s3",
    connection_options={"path": target_path, "partitionKeys": ["sexo", "ano"]},
    format="json"
)

job.commit()