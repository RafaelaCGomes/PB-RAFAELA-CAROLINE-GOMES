# Resumo da Sprint 7



# Exercícios
No exercício do TMDB, criei minha conta na plataforma, configurei a conta e tive acesso a chave da APPI, sendo que após, realizei um teste local para ver se estava funcionando.

No exercício de Glue, aprendi na na prática como criar IAM Role, configurar a conta para usar o AWS Glue,Configurar o Lake Formation, criar e testar jobs e por fim, criar crawlers.





# Evidências

Para ficar de fácil entendimento, realizarei as evidências dos exercícios conforme a sequencia fornecida na plataforma Udemy.

## Etapas da resolução do exercício.

## Exercício TMDB
### Etapa 1
1. Criei minha conta no portal do TMDB e confirmei o e-mail.

![Conta_criada_TMDB](../Sprint%207/Exercícios/Ex_TMDB/Evidencias/Conta_criada_TMDB.jpg)

2. Após configurar o perfil, tive acesso a chave da API.

### Etapa 2
Realizei o exemplo fornecido para testar se estava funcionando corretamente.

1. Digitei o exemplo fornecido e o executei.

![Exemplo_exercicio_tmdb](../Sprint%207/Exercícios/Ex_TMDB/Evidencias/Ex_exemplo_TMDB.jpg)

![Resultado_exemplo_exercicio_tmdb](../Sprint%207/Exercícios/Ex_TMDB/Evidencias/Ex_exemplo_TMDB_02.jpg)



## Exercício Lab Glue

### Etapa 01: 
Enviei o arquivo csv baixado para o bucket s3.

![Arquivo_csv](../Sprint%207/Exercícios/Lab_Glue/Evidencias/nome_csv.jpg)

![Bucket_s3](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa01_A.jpg)

![Bucket_s3_csv](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa01_B.jpg)

### Etapa 2:
Criei o IAM conforme as orientações.

![IAM_01](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa02_A.jpg)

![IAM_02](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa02_B.jpg)

### Etapa 03:
Configurei a conta para utilizar o AWS Glue conforme as orientações.

![Configuração_conta](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa03_A.jpg)

![Configuração_conta_02](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa03_B.jpg)

![Configuração_conta_03](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa03_C.jpg)

### Etapa 4:
Configurei as permissões no AWS Lake Formation conforme as orientações.

![Config_Lake_F_01](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa04_a.jpg)

![Config_Lake_F_02](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa04_b.jpg)

### Etapa 5:
Criei um novo job, seguindo as orientações.

No job, inseri o código exemplo disponibilizado, sendo o mesmo do arquivo [job_exercicio.py](../Sprint%207/Exercícios/Lab_Glue/job_exercicio.py)

![job_etapa_5](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa05-exemplo.jpg)

Ao rodar rodar, fiz várias tentativas, recebi erro de escrita de parametros, alterei e ainda continuou dando erro.

![Erro_job](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa05_erro.jpg)

Ao analizar o código e o CSV, percebi que haviam inconsistências, sendo alterado os campos "separator": "|" para "separator": "," e no código exemplo, estava filtrando a coluna 'anoLancamento', sendo que no csv é somente 'ano'. Tendo então o código [job_teste_exercicio.py](./Exercícios/Lab_Glue/job_teste_exercicio.py).

![correção_erro](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa05_correcaoerro.jpg)

![job_corrigido_e_rodando](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa05_job_ok.jpg)

Resultando no arquivo [parquet](../Sprint%207/Exercícios/Lab_Glue/part-00000-8e7ec108-b540-4feb-b85f-a7a0703b596f-c000.snappy.parquet)

![Etapa05_parquet_resultado](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa05_parquet_resultado.jpg)

Sendo ele salvo no bucket s3.
![Etapa05_bucket_parquet](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa05_s3_parquet_exemplo.jpg)

### Etapa 5.2
Nessa etapa, alterei o job criado anteriormente, colocando o código [job_exercicio.py](../Sprint%207/Exercícios/Lab_Glue/job_exercicio.py).

No bucket s3 criei ourtra pasta.
![bucket_exercicio](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa5.2_S3_a.jpg)

E segui todas as indicações do exercício.

![exercicio_etapa5.2_b](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa5.2_job_b.jpg)

![exercicio_jobs_rodados](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa5.2_jobs_rodados.jpg)

![exercicio_etapa5.2_c](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa5.2_job_c.jpg)

Tendo como resultado após rodas o job.
 
![exercicio_etapa5.2_d](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa5.2_s3_d.jpg)

![exercicio_etapa5.2_b](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Etapa5.2_s3_e.jpg)

### Etapa 6
Criei e rodei uma crawler conforme as indicações do exercício. 

![Criando_crawler-01](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Crawler-01.jpg)

![Criando_crawler-02](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Crawler-02.jpg)

![Criando_crawler-03](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Crawler-03.jpg)

![Rodando_crawler-04](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Crawler-04.jpg)

![Crawler_database-05](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Crawler-05.jpg)

![Crawler_Athena-06](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Crawler-06.jpg)

![Crawler_Athena-0](../Sprint%207/Exercícios/Lab_Glue/Evidencias/Crawler-07.jpg)

Após a comsulta, resultando na tabela [Tabela_resultado_crawler](../Sprint%207/Exercícios/Lab_Glue/ac0717a1-889c-4551-91c3-76861f259507.csv)

## Exercício Spark

### Etapa 1: 



# Certificados
