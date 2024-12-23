import logging
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

#Minhas credenciais da AWS
aws_access_key_id='ASIA4DMVQ3KKWL77OQ4U'
aws_secret_access_key='nLvznGF6DW6vvOi3dWJ1MmjjydhM7DT1yuryd3Bn'
aws_session_token='IQoJb3JpZ2luX2VjEBIaCXVzLWVhc3QtMSJHMEUCIQCSbxoX7378TEymu+HgLN9suqlaWo4ezhF1j2OJQ9ezEwIgErUbfo8gl2YUynRWO4A7IE1j5E05Bpmi007hPS37aywqrgMI2///////////ARAAGgw4MzE5MjY2MjI4NjkiDFaDBawoQ9xwQ4W5HyqCA7mNP/odfUgnz2JMg707HBoMHrstvQ32YMGaX2Y6h3qKRuH5cwg8xo6zzF6csV1XMMObT/OUrubl936Qy1MbA3UdX6aWBh4CShoypQmOK99h3IBap7ZFbuSuyeth8TUdMoLuojRJRsfwT7uTWmoqYyKWrTI1lz1N5NGwI4nSo66gRdvib2zX2zaxMSnvXAUr5G7Q9UKcH5gO/BEivg8X9bcD+O4EaV8M/UdCNDSqjJ7XPkd6l8YiPGUFcfFIKnm3CUdoEarJ4tXMtJzIN77hoIFHseveUnKPoE9bz7dCR5GKB1+VS7BGmAPbAxNM0m0PqRPv4c/8Quvmj1z55W5fYw6siqZqe8+w54cc7hf4HtXcgo7yxboh6e+UWWSeJXfC8XU/RdjdnwHbI/wMbMpCKwdx8rEC1FRZVlXIwWyesZ4kYZL/AQvY4TpAWg3FWctd0I/Si0E/uZUT1cCrRGZuOB6BoUExoLNiBobuHB1Hrj/3Z/VctSX1pFPKrExpqnjYROmRMLK4prsGOqYBp9yMH9Tc08opnz33rPzVTQW0/FDU0IkvpI4ebqBKTnaWV2qpmhfaW9QeC4ehkTed7NW1G/pZw2ETKoCdMc+g0lzLTsOd+PKFUHl+cMJ92TVFiZVhDGxPRP0WRCBEcUPYORs97g6V2ldS6kdPBQTYGYsPTKc7bU0PVjpE0zmvnk2o386HddqLveaSGOBuLYvoGr4x3NZfkzspfLgE8rgd6mrltmwMsQ=='
aws_region = 'us-east-1'

#Nome do bucket
nome_bucket = 'desafio-sprint-05'

#Dados do dataset tratado - Estoque_camarao_tratado
csv_tratado_caminho = 'C:/Users/User/Desktop/Compass.uol/Sprint05/Desafio/Estoque_camarao_tratado.csv'
nome_objeto02_bucket = 'Dataset_tratado.csv'

#Dados do dataset final após manipulações - Cidade_com_maior_estoque
csv_manipulado_caminho = 'C:/Users/User/Desktop/Compass.uol/Sprint05/Desafio/Cidade_com_maior_estoque.csv'
nome_objeto03_bucket = 'Dataset_final_manipulado.csv'

try:
    #Cliente S3 com credenciais explícitas
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token, 
        region_name=aws_region
    )
    # Enviando o arquivo Estoque_camarão_tratado.CSV para o bucket (após tratamento de dados)
    s3.upload_file(
        Filename=csv_tratado_caminho,  
        Bucket=nome_bucket,      # Nome do bucket
        Key=nome_objeto02_bucket       # Nome do arquivo no S3
    )
    print(f"Arquivo '{csv_tratado_caminho}' enviado com sucesso para o bucket '{nome_bucket}' como '{nome_objeto02_bucket}'!")

   # Enviando o arquivo Cidade_com_maior_estoque.CSV para o bucket (após as manipulações)
    s3.upload_file(
        Filename=csv_manipulado_caminho,  
        Bucket=nome_bucket,      # Nome do bucket
        Key=nome_objeto03_bucket       # Nome do arquivo no S3
    )
    print(f"Arquivo '{csv_manipulado_caminho}' enviado com sucesso para o bucket '{nome_bucket}' como '{nome_objeto03_bucket}'!")

except NoCredentialsError:
    print("Credenciais AWS não encontradas!")
except ClientError as e:
    print(f"Erro ao criar o bucket: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")