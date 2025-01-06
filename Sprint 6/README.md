# Resumo da Sprint 6

Na sprint 06 foi disponibilizado diversos cursos da AWS, onde pude aprender e ver como funcionan o console de diversos recursos da AWS.

Além disso, pude colocar em prática criar bucket, criar banco de dados e tabelas no AWS Athena e realizar consultas no Amazon Lambda.

# Exercícios
No exercício de Laboratório AWS S3, aprendi como criar um bucket S3 e realizar configurações para que funcione como hospedagem de conteúdo estático.

No exercício o AWS Athena, aprendi como criar banco de dados, tabelas e realizar querys de consulta da tabela e banco de dados criado com base em um arquivo csv.

Já no exercício de Lambda, criei uma função e uma camada para conseguir executar essa função.




# Evidências

Para ficar de fácil entendimento, realizarei as evidências dos exercícios conforme a sequencia fornecida na plataforma Udemy.

## Etapas da resolução do exercício.

## Lab AWS s3

Mesmo já tendo realizado a criação de um bucket na sprint 05, achei interessante realizar a deleção do antigo bucket e criar um novo para a sprint 06. 

1. Após excluir os bickets ja criados, comecei criando novamente o bucket S3.

![Bucket_criado](../Sprint%206/Exercícios/Evidencias/criacao_bucket_novo.jpg)

2. Ativei a hospedagem de site estático no bucket criado.

![Hospedagem_site_estatico](../Sprint%206/Exercícios/Evidencias/hospedagem_site_estatico.jpg)

3. Adicionei os arquivos de indice e de erro ao bucket.

![index_e_erro](../Sprint%206/Exercícios/Evidencias/index_e_erro.jpg)

4. Atualizei as configurações de acesso público, para que seja possível acessar o site. Deixei desmarcado o bloqueio acesso público.

![bloqueio_acesso_publico](../Sprint%206/Exercícios/Evidencias/desbloqueio_acesso_publico.jpg)

5. Adicionei uma politica de bucket para conceder acesso de leitura.

![politica_bucket](../Sprint%206/Exercícios/Evidencias/politica_bucket.jpg)

6. Criei o documento de índice, nesse caso, chamado index.html

![doc_index](../Sprint%206/Exercícios/Evidencias/index_html.jpg)

7. Criei o documento de erro, chamado 404.html

![_doc_erro](../Sprint%206/Exercícios/Evidencias/erro_html.jpg)

8. Em seguida, fiz upload do arquivo de índice, de erro e do arquivo csv para o bucket. Criei também uma pasta chamada dados e dentro dela coloquei o arquivo nomes.csv.

![Upload_index_csv_404](../Sprint%206/Exercícios/Evidencias/upload_index_erro.jpg)

![Upload_csv](../Sprint%206/Exercícios/Evidencias/upload_csv.jpg)

9. Realizei o teste do endpoint para ver se estava tudo funcionando.

![Teste_endpoint01](../Sprint%206/Exercícios/Evidencias/teste_endpoint.jpg)

O endpoint criado após a criação do bucket foi:

http://exlabbuckets3.s3-website-us-east-1.amazonaws.com


## AWS Athena

### Etapa 01:

1. Iniciei a Etapa do exercício da AWS Athena analisando o nome e o tipo de dado de cada coluna do arquivo [nomes.csv](../Sprint%206/Exercícios/Etapa_01_AWS_S3/nomes.csv)

Para isso, criei um notebook para vizualisar essas informações.

![Informações_csv](../Sprint%206/Exercícios/Evidencias/analise_arquivo_csv.jpg)

2. Criei uma pasta chamada queries dentro do bucket criado na [Etapa01_AWS_S3](../Sprint%206/Exercícios/Etapa_01_AWS_S3/)

![criacao_pasta_queries](../Sprint%206/Exercícios/Evidencias/criacao_pasta_querie_bucket.jpg)

3. Configurei o Athena para acessar o bucket e a pasta queries.

![config_athena](../Sprint%206/Exercícios/Evidencias/config_bicket_athena.jpg)

### Etapa 2: 

Criei o banco de dados chamado meubanco.

![criação_bancodados_athena](../Sprint%206/Exercícios/Evidencias/criacao_banco_dados_athena.jpg)

### Etapa 3: 

1. Criei a tabela com as colunas existentes no csv.

![Criação_tabela_athena](../Sprint%206/Exercícios/Evidencias/criacao_tabela.jpg)

2. Realizei uma consulta dos 15 nomes mais usados no ano de 1999. 

```
select nome from meubanco.tabela_nomes where ano = 1999 order by total limit 15
```

![Teste_consulta01](../Sprint%206/Exercícios/Evidencias/teste_consulta01.jpg)

![Teste_Consulta01a](../Sprint%206/Exercícios/Evidencias/teste_consulta01a.jpg)

3. Realizei uma nova consulta onde mostra os três nomes mais usados por décadas desde 1950 até 2024.

![Teste_consulta02a](../Sprint%206/Exercícios/Evidencias/teste_consulta02a.jpg)

Para a consulta SQL, utilizei o seguinte código.


    with selecao_nomes as (
        select
            floor(ano / 10) * 10 as decada,
            nome,
            total,
            row_number() over (
                partition by floor(ano / 10) * 10
                order by total desc
            ) as rank
        from
            meubanco.tabela_nomes
        where
            ano between 1950 and 2024
        )
        select
            decada, nome, total
        from
            selecao_nomes
        where
            rank <= 3
        order by
            decada,total desc


Tendo como resultado:

![Teste_consulta02b](../Sprint%206/Exercícios/Evidencias/teste_consulta02b.jpg)

## AWS Lambda

### Etapa 1: 

Criei uma fução lambda no console da AWS.

![criação_função](../Sprint%206/Exercícios/Evidencias/criacao_funcao.jpg)

### Etapa 02: 

1. Atualizei o código pré escrito na função lambda_function.py, colocando o código a seguir.

```
import json
import pandas
import boto3
 
def lambda_handler(event, context):
    s3_client = boto3.client('s3')
 
    bucket_name = 'exlabbuckets3'
    s3_file_name = 'dados/nomes.csv'
    objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    df=pandas.read_csv(objeto['Body'], sep=',')
    rows = len(df.axes[0])
 
    return {
        'statusCode': 200,
        'body': f"Este arquivo tem {rows} linhas"
    }

```

![atualização_função](../Sprint%206/Exercícios/Evidencias/atualização_funcao.jpg)

2. Em seguida, testei a função criada, porém tive um erro.

![teste_função](../Sprint%206/Exercícios/Evidencias/teste_funcao.jpg)

### Etapa 03:
Como deu erro ao executar a função, precisei criar uma Layer (camada) que contenha um arquivo zip que importe pandas em sistema linux.

1. Comecei criando uma pasta no sistema e um arquivo Dockerfile.

![Criação_dockerfile](../Sprint%206/Exercícios/Evidencias/arquivo_dockerfile01.jpg)

2. Criei uma imagem seguindo as orientações do exercício. 

![imagem_docker](../Sprint%206/Exercícios/Evidencias/criacao_docker02.jpg)

3. Rodei um containner com base na imagem criada.

![rodando_imagem](../Sprint%206/Exercícios/Evidencias/docker_03.jpg)

4. Criei diretórios dentro do container que receberá as bibliotecas necessárias.

![Diretorios_docker](../Sprint%206/Exercícios/Evidencias/dir_container_04.jpg)

5. No diretório python criada em layer_dir, baixei a biblioteca pandas usando o comando:

```
pip3 install pandas -t
```
Em seguida, conferi se os arquivos foram no diretório corretamente.

![Diretorio_pandas](../Sprint%206/Exercícios/Evidencias/pandas_cont_05_06.jpg)

6. Voltei em layer_dir e compactei o diretório python usando o comando:

```
zip -r minha-camada-pandas.zip .
```
![Zip_python](../Sprint%206/Exercícios/Evidencias/zip_python_07.jpg)

7. Após listar o container em execução por meio de outra janela do terminal. Utilizei o ID do container para salvar o arquivo zip para a maquina local.

![Salvando_zip](../Sprint%206/Exercícios/Evidencias/salvando_zip_local_08.jpg)

8. Fiz uploado do arquivi zip no bucket criado no exercício [AWS_s3](../Sprint%206/Exercícios/Ex_AWS_S3/)

![Upload_s3](../Sprint%206/Exercícios/Evidencias/upload_zip_09.jpg)

9. Retornei ao AWS Lambda, criei uma camada e adicionei o link do bucket onde foi salvo o arquivo zip.

![camada_lambda](../Sprint%206/Exercícios/Evidencias/camada_lambda_10.jpg)

10. Retornei a funções e editei a função criada anteriormente, adicionando a camada criada.

![add_camada_função](../Sprint%206/Exercícios/Evidencias/add_camada_layer_11.jpg)

11. Executei novamente a função, mas obtive um erro.

![teste_lambda_erro_memoria](../Sprint%206/Exercícios/Evidencias/erro_layer_12.jpg)

12. Atualizei o tamanho da memória e o tempo da função Lambda.

![Atualização_função](../Sprint%206/Exercícios/Evidencias/atualizacao_memoriaetempo_12.jpg)

13. Após executar novamente, consegui executar com êxito.

![novo_teste_lambda](../Sprint%206/Exercícios/Evidencias/novo_teste_13.jpg)

## AWS Limpeza de recursos

Após executar os exercícios, realizei a limpeza do bucket, excluindo todos os arquivos dele.

![limpeza_recursos](../Sprint%206/Exercícios/Evidencias/limpeza_recursos.jpg)

# Certificados
Após a conclusão dos cursos, recebi os certificados:

[Noções básicas de Analytics - Parte 1](../Sprint%206/Certificados/Rafaela_C_gomes_Noções_básicas_de_Analytics_na_AWS-Parte1.pdf)

[Fundamentos de Analytics na AWS- Parte 2](../Sprint%206/Certificados/Rafaela_gomes_Fundamentos_de_analytics_na_AWS_Parte2.pdf)

[Introducttion to Amazon Athena](../Sprint%206/Certificados/Rafaela_gomes_Introduction_to_Amazon_Athena.pdf)

[Serverless Analytics](../Sprint%206/Certificados/Rafaela_gomes_ServerlessAnalytics.pdf)

[Amazon QuickSight - Getting Started](../Sprint%206/Certificados/Rafaela_gomes-Amazon%20QuickSight%20-%20Getting%20Started%20(English).pdf)

[Amazon EMR Getting Started](../Sprint%206/Certificados/Rafaela_gomes-Amazon_EMR_Getting_Started.pdf)

[AWS Glue Getting Started](../Sprint%206/Certificados/Rafaela_gomes-AWS%20Glue%20Getting%20Star.pdf)

[Best Practices for Data Warehousing with Amazon Redshift](../Sprint%206/Certificados/Rafaela_gomes-AWS%20Skill%20Builder%20-%20Best%20Practices%20for%20Data%20Warehousing%20with%20Amazon%20Redshift%20(Portuguese).pdf)

[Getting Started with Amazon Redshift](../Sprint%206/Certificados/Rafaela_gomes-Getting%20Started%20with%20Amazon%20Redshift%20(Portuguese).pdf)



