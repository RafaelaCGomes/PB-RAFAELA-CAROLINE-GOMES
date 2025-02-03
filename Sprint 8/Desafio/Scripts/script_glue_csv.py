
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH_MOVIES','S3_OUTPUT_PATH_MOVIES','S3_INPUT_PATH_SERIES','S3_OUTPUT_PATH_SERIES'])


sc = SparkContext() 
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


s3_input_path_movies = args['S3_INPUT_PATH_MOVIES']
s3_output_path_movies = args['S3_OUTPUT_PATH_MOVIES']

s3_input_path_series = args['S3_INPUT_PATH_SERIES']
s3_output_path_series = args['S3_OUTPUT_PATH_SERIES']

#Caminhos do S3
#s3_input_path_movies = "s3://awsbucket-desafio/Raw/Local/CSV/Movies/2025/01/06/movies.csv"
#s3_output_path_movies = "s3://awsbucket-desafio/Trusted/Local/Parquet/Movies/"

#s3_input_path_series = "s3://awsbucket-desafio/Raw/Local/CSV/Series/2025/01/06/series.csv"
#s3_output_path_series = "s3://awsbucket-desafio/Trusted/Local/Parquet/Series/"


#Função para processar o csv
def processo_csv(s3_input_path, s3_output_path):
    try:
# Le o arquivo CSV do S3 em um DataFrame
        df_dynamic = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths" :[s3_input_path]},
        format="csv",
        format_options={"withHeader" : True, "separator": "|" })
        
#Converte DynamicFrame em dataframe.
        df = df_dynamic.toDF() 

#Conversão da coluna anoLancamento, tempoMinutos, anoNascimento, anoFalecimento para number se existir
        colunas_converter = ['anoLancamento','tempoMinutos','anoNascimento','anoFalecimento']
        for coluna in colunas_converter:
            if coluna in df.columns:
                df = df.withColumn(coluna, col(coluna).cast(IntegerType()))
                
#garatir que gere somente 1 parquet para cada csv
        df = df.coalesce(1)

# Converter de volta para DynamicFrame
        df_dynamic = DynamicFrame.fromDF(df, glueContext)

# Grave o DataFrame no formato Parquet no S3
        glueContext.write_dynamic_frame.from_options(
            frame=df_dynamic,
            connection_type="s3",
            connection_options={"path": s3_output_path},
            format="parquet")

        print(f'Arquivo processado e salvo em {s3_output_path}')
    except Exception as e:
        print(f'Erro ao processar o arquivo: {s3_input_path}: {e}')



#processar cada arquivo
processo_csv(s3_input_path_movies, s3_output_path_movies)
processo_csv(s3_input_path_series, s3_output_path_series)

job.commit()

