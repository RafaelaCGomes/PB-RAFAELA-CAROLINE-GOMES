# Resumo e Objetivo

Para o desafio da sprint, precisei selecionar um dataset do portal de dados públicos do Governo Brasileiro.

Após analisar, escolhi o ..... [csv]

Realizei o tratamento de dados do dataset original, realizar as manipulações necessárias e enviar para o bucket, tive como entregáveis:

Arquivo [ tratamento dados .py] e [arquivo manipulações . py].
Arquivo [csv tratado] e arquivo [csv manipulado].
Para o upload dos arquivos para a AWS, realizei um [Script criação buscket e envio do csv original] e [script envio dos demais csv] 



# Etapas
Para uma melhor organização da resolução do exercício, dividirei o desafio em etapas.

## Etapa01: Criação do bucket e envio do dataset original.

Na primeira etapa, realizei a criação do bucket por meio de um [script_python], usando a biblioteca boto3.

![script_bucket_aws01]

![script_bucket_aws02]

![No_bucket_aws]

## Etapa02: Tratamento e manipulação dos dados.

Após, realizei a análise dos dados selecionados, como vi que não tinha dados nulos e inconsistências, realizei somente a conversão do tipo dos dados de algumas colunas para numérico.

Em seguida, salvei em um novo arquivo.csv.

![script_]

![]

Com o dataframe novo tratado, realizei as manipulações estipuladas no enunciado do desafio.

Para isso, criei um novo script python, onde eu conseguisse responder a questão:

- 

Para as manipulações:

1. Comecei

2. 

3. 

4. 

5. 

6. 

Como resultado final das manipulação, tive como saida um novo dataframe [arquivo.csv] e um arquivo [arquivo.txt] com a pergunta e a resposta.


## Etapa03: Envio dos dataframe tratado e manipulado.

Por fim, após todo o processo de tratamento e manipulações, resultando em uma unica resposta, enviei os dataframes para o bucket criado anteriormente.

Para isso, criei um novo script python onde usei novamente a biblioteca boto3 para enviar os arquivos na nuvem.

[script_aws_2]

![]








