#Etapa 1
from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when, udf, col, floor, expr
from pyspark.sql.types import StringType, IntegerType

import random

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()
print("SparkSession iniciada com sucesso!")

df = spark.read.csv("/content/drive/MyDrive/Colab Notebooks/nomes_aleatorios.txt")

df.show(5)

#Etapa 2
df_nomes = df.withColumnRenamed("_c0", "Nomes")

df_nomes.printSchema()

df_nomes.show(10)

#Etapa 3
#Adicionar coluna Escolaridade e atribuir valores aleatórioos entre Fundamental, Medio e Superior
df_nomes = df_nomes.withColumn("random_val", rand())
df_nomes = df_nomes.withColumn("Escolaridade",
                    when(col("random_val") < 0.33, "Fundamental")
                    .when(col("random_val") < 0.66, "Medio")
                    .otherwise("Superior")).drop("random_val")
df_nomes.show(10)

#Etapa4
#lista de países da america do sul
paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]

def paisaleatorio():
  return random.choice(paises)
udf_paisaleatorio = udf(paisaleatorio, StringType())

#adicionar a coluna ao df e completar com os países
df_nomes = df_nomes.withColumn("Pais", udf_paisaleatorio())
df_nomes.show(10)

#Etapa 5
#gerar anos entre 1945 a 2010
df_nomes = df_nomes.withColumn("AnoNascimento", (floor(rand() * (2010 - 1945 + 1)) + 1945).cast(IntegerType()))
df_nomes.show(10)

#Etapa 6
#selecionar as pessoas que nasceram nesse século (entre 2000 e 2100) e add ao df_select usando select
df_select = df_nomes.filter(col("AnoNascimento") >= 2000).select("Nomes", "AnoNascimento")
df_select.show(10)

#Etapa 7
df_nomes.createOrReplaceTempView("nomes")
spark.sql("SELECT Nomes, AnoNascimento FROM nomes WHERE AnoNascimento >= 2000").show(10)

#Etapa 8
#Usando filter, contar o numero de pessoas que são da geração Millenials (entre 1980 e 1994)
df_millenials = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994))
df_millenials.count()

#Etapa 9
#usando Spark SQL
spark.sql("SELECT COUNT(*) FROM nomes WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994").show()

#Etapa 10
#quantidade de pessoas de cada pais para cada geração.

df_final = spark.sql("""
SELECT Pais,
       CASE
           WHEN AnoNascimento >= 1944 AND AnoNascimento <= 1964 THEN 'Baby Boomers'
           WHEN AnoNascimento >= 1965 AND AnoNascimento <= 1979 THEN 'Geração X'
           WHEN AnoNascimento >= 1980 AND AnoNascimento <= 1994 THEN 'Millenials (Geração Y)'
           WHEN AnoNascimento >= 1995 AND AnoNascimento <= 2015 THEN 'Geração Z'
      END AS Geracao,
      COUNT(*) AS Quantidade
FROM nomes
GROUP BY Pais, Geracao
ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")
df_final.show()

#mostrando todas as linhas do df_final
rows = df_final.collect()
for row in rows:
    print(row)