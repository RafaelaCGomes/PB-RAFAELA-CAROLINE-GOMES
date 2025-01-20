import csv
import requests
import json
import os
import boto3
from datetime import datetime

# Configuração da API do TMDB
CHAVE_TMDB = os.environ.get('CHAVE_TMDB')
url = 'https://api.themoviedb.org/3/movie/{movie_id}'

# Configuração do Boto3
s3 = boto3.client('s3')
NOME_BUCKET = os.environ.get('NOME_BUCKET') 

# Buscar detalhes de um filme pelo ID
def buscar_detalhes_filmes(movie_id):
    url_base = url.format(movie_id=movie_id)
    params = {'api_key': CHAVE_TMDB}
    try:
        response = requests.get(url_base, params=params)
        response.raise_for_status()  # Levanta erros HTTP
        print(f"URL requisitada: {url_base}, Status Code: {response.status_code}")
        return response.json()  # Resposta em formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar detalhes do filme ID {movie_id}: {e}")
        return None
    

# Salvar dados JSON no bucket S3
def salvar_json_em_s3(data, bucket_name, file_path):
    try:
        s3.put_object(Bucket=bucket_name, Key=file_path, Body=json.dumps(data, ensure_ascii=False, indent=4))
        print(f"Arquivo salvo em: s3://{bucket_name}/{file_path}")
    except Exception as e:
        print(f"Erro ao salvar arquivo no S3: {e}")

# Leitura do CSV na Layer
def ler_csv_na_layer(caminho_csv):
    try:
        with open(caminho_csv, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]  # Retorna uma lista de dicionários
    except Exception as e:
        print(f"Erro ao ler o CSV da Layer: {e}")
        return None

# Lê IDs de filmes de um CSV na Layer, baixa detalhes e salva em json no S3
def ler_filmes_csv_e_baixar_detalhes(caminho_csv, batch_size=100):
    # Carregar os IDs do CSV da Layer
    rows = ler_csv_na_layer(caminho_csv)
    if rows is None or 'id' not in rows[0]:
        raise ValueError("O CSV deve conter uma coluna chamada 'id' com os IDs dos filmes.")

    # Lista para armazenar os detalhes dos filmes
    movie_details = []
    batch_number = 1  # Contador para os arquivos JSON

    # Data atual para o caminho do arquivo
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    # Iterar pelos IDs e buscar os detalhes
    for i, row in enumerate(rows, start=1):
        movie_id = row['id']
        details = buscar_detalhes_filmes(movie_id)
        if details:
            movie_details.append(details)

        # Salvar quando atingir o tamanho do lote ou no final da lista
        if len(movie_details) == batch_size or i == len(rows):
            file_name = f"detalhes_filmes_batch_{batch_number}.json"
            file_path = f"Raw/TMDB/JSON/{year}/{month}/{day}/{file_name}"
            salvar_json_em_s3(movie_details, NOME_BUCKET, file_path)
            movie_details = []  # Limpar o lote atual
            batch_number += 1
            print(f"Lote {batch_number} salvo em: s3://{NOME_BUCKET}/{file_path}")

# Função Lambda para processar a execução
def lambda_handler(event, context):
    # O caminho da Layer onde o CSV está armazenado
    CAMINHO_CSV = os.environ.get('CAMINHO_CSV')
    ler_filmes_csv_e_baixar_detalhes(CAMINHO_CSV, batch_size=100)