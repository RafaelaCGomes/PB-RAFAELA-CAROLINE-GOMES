FROM python:3.11-slim

#Diretório
WORKDIR /app   

#Copiando os arquivos CSV para o container
COPY movies.csv .
COPY series.csv .

#Copiando o script Python para o container
COPY script.py .

RUN pip install boto3

#Rodar o script Python
CMD ["python", "script.py"]
