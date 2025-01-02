# Resumo da Sprint 6

Na sprint 06 foi disponibilizado 

# Exercícios
No exercício de Laboratório AWS S3, pude aprender como criar um bucket S3 e realizar configurações para que funcione como hospedagem de conteúdo estático.




# Evidências

Para ficar de fácil entendimento, realizarei as evidencias dos exercícios conforme a sequencia fornecida na plataforma Udemy.

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

Etapa 01:

1. Iniciei a Etapa do exercício da AWS Athena analisando o nome e o tipo de dado de cada coluna do arquivo [nomes.csv](../Sprint%206/Exercícios/Etapa_01_AWS_S3/nomes.csv)

Para isso, criei um notebook para vizualisar essas informações.

![Informações_csv](../Sprint%206/Exercícios/Evidencias/analise_arquivo_csv.jpg)

2. Criei uma pasta chamada queries dentro do bucket criado na [Etapa01_AWS_S3](../Sprint%206/Exercícios/Etapa_01_AWS_S3/)

![criacao_pasta_queries](../Sprint%206/Exercícios/Evidencias/criacao_pasta_querie_bucket.jpg)

3. Configurei o Athena para acessar o bucket e a pasta queries.

![config_athena](../Sprint%206/Exercícios/Evidencias/config_bicket_athena.jpg)

4.  

![criação_bancodados_athena](../Sprint%206/Exercícios/Evidencias/criacao_banco_dados_athena.jpg)

5. 
![Criação_tabela_athena](../Sprint%206/Exercícios/Evidencias/criacao_tabela.jpg)

6. 
```
select nome from meubanco.tabela_nomes where ano = 1999 order by total limit 15
```
![Teste_consulta01](../Sprint%206/Exercícios/Evidencias/teste_consulta01.jpg)

![Teste_Consulta01a](../Sprint%206/Exercícios/Evidencias/teste_consulta01a.jpg)

7. 
![Teste_consulta02a](../Sprint%206/Exercícios/Evidencias/teste_consulta02a.jpg)

Consulta SQL

´´´
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

´´´
![Teste_consulta02b](../Sprint%206/Exercícios/Evidencias/teste_consulta02b.jpg)

## AWS Lambda


Etapa 1: Criei uma fução lambada no console da AWS.

![criação_função](../Sprint%206/Exercícios/Evidencias/criacao_funcao.jpg)

Etapa 02: Atualizei o código pré escrito na função lambda_function.py, colocando o código a seguir.

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

Em seguida, testei a função criada, porém tive um erro.

![teste_função](../Sprint%206/Exercícios/Evidencias/teste_funcao.jpg)


Etapa 03:

1. Comecei criando uma pasta no sistema e um arquivo Dockerfile.

![Criação_dockerfile](../Sprint%206/Exercícios/Evidencias/arquivo_dockerfile01.jpg)

2. Criei uma imagem seguindo as orientações do exercício. 

![imagem_docker](../Sprint%206/Exercícios/Evidencias/criacao_docker02.jpg)

3. Rodei um containner com base na imagem criada.

![rodando_imagem](../Sprint%206/Exercícios/Evidencias/docker_03.jpg)

4. 
![]()

5. 
![]()

6. 
![]()

7. 
![]()

8. 
![]()

9. 
![Upload_s3](../Sprint%206/Exercícios/Evidencias/upload_zip_09.jpg)

10. 
![]()

11. 
![]()

12. 
![]()

## AWS Limpeza de recursos

1. 

# Certificados
Após a conclusão dos cursos, recebi 


