import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime


# Carregar as credenciais da AWS por input
aws_access_key_id=input("Digite sua AWS ACCESS KEY ID: ").strip()
aws_secret_access_key=input("Digite sua AWS SECRET ACESS KEY: ").strip()
aws_session_token=input("Digite sua SESSION TOKEN: ").strip()


#função para enviar os arquivos
def upload_s3(nome_arquivo, nome_bucket, caminho_bucket ):
    try:
        cliente_s3 = boto3.client('s3',
        aws_access_key_id=aws_access_key_id, 
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token)

        cliente_s3.upload_file(nome_arquivo, nome_bucket, caminho_bucket)

        print(f"Arquivo {nome_arquivo} enviado com sucesso para o bucket {nome_bucket}.")
        return True
    
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return False
    except NoCredentialsError:
        print("Erro: Nenhuma credencial da AWS foi encontrada.")
        return False
    except Exception as e:
        print(f"Erro ao enviar o arquivo: {e}")
        return False


#Dados aws geral
nome_bucket = 'awsbucket-desafio'

camada_armazenamento = 'Raw'
origem_dados = 'Local'
formato_dados = 'CSV'

data = datetime.now()
ano = data.strftime('%Y')  # Ano atual do processamento
mes = data.strftime('%m')   # Mês atual do procesamento
dia = data.strftime('%d')   # Dia atual do processamento


#Movies
especificacao_dados_movies = 'Movies'
caminho_local_movies = '/app/movies.csv'
s3_caminho_movies = f"{camada_armazenamento}/{origem_dados}/{formato_dados}/{especificacao_dados_movies}/{ano}/{mes}/{dia}/movies.csv"


upload_s3(caminho_local_movies, nome_bucket, s3_caminho_movies)

#Series
especificacao_dados_series = 'Series'
caminho_local_series = '/app/series.csv'
s3_caminho_series = f"{camada_armazenamento}/{origem_dados}/{formato_dados}/{especificacao_dados_series}/{ano}/{mes}/{dia}/series.csv"


upload_s3(caminho_local_series, nome_bucket, s3_caminho_series)
