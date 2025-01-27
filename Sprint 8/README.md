# Resumo da Sprint 8

Na sprint 8 realizei novos exercícios de spark o que ajudou na resolução do desafio.


# Exercícios
No exercício do TMDB dessa sprint, como já havia feito na sprint passada, segui as orientações da plataforma Udemy.

No exercicio de Spark (Geração e massa de dados), realizei exercícios de aquecimento onde foi criado listas aleátorias e na última etapa, criar um arquivo txt contendo 10000000 nomes aleatórios.

No último exercício de Spark, utilizei o arquivo nomes_aleatórios.txt gerado no exercício anterior para realizar alterações e consultas.



# Evidências

Para ficar de fácil entendimento, realizarei as evidências dos exercícios conforme a sequencia realizada.

## Etapas da resolução do exercício.

## Exercício TMDB
### Etapa 1
1. Criei minha conta no portal do TMDB e confirmei o e-mail.

![Conta_criada_TMDB](./Exercícios/Ex_TMDB/Evidencias/Conta_criada_TMDB.jpg)

2. Após configurar o perfil, tive acesso a chave da API.

### Etapa 2
Realizei o exemplo fornecido para testar se estava funcionando corretamente.

1. Digitei o exemplo fornecido e o executei.

![Exemplo_exercicio_tmdb](./Exercícios/Ex_TMDB/Evidencias/Ex_exemplo_TMDB.jpg)

![Resultado_exemplo_exercicio_tmdb](./Exercícios/Ex_TMDB/Evidencias/Ex_exemplo_TMDB_02.jpg)



## Exercício Spark - Geração e massa de dados

### Etapa 01: 

Criei um código python [Etapa01.py](./Exercícios/Ex_Spark-Geracao_massa_dados/Etapa01.py) que gere uma lista com 250 números inteiros aleatórios, apliquei reverse e imprimi a lista.

![Etapa01_A](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa01_A.jpg)

![Etapa01_B](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa01_B.jpg)

### Etapa 2:
Criei o script [Etapa02.py](./Exercícios/Ex_Spark-Geracao_massa_dados/Etapa02.py) que gera uma lista de 20 animais, ordena em ordem alfabética, imprime e grava em arquivo csv, um animal em cada linha, gerando o arquivo [animais_ordenados.csv](./Exercícios/Ex_Spark-Geracao_massa_dados/animais_ordenados.csv)

![Etapa02_A](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa02_A.jpg)

![Etapa02_B](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa02_B.jpg)

![Etapa02_C](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa02_C.jpg)

### Etapa 03:

Nessa etapa, segui as instruções do exercício e criei o arquivo [Etapa03.py](./Exercícios/Ex_Spark-Geracao_massa_dados/Etapa03.py), que gera o arquivo nomes_aleatórios.txt. 

Para envio ao repositório, achei interessante compactar por conta do tamanho do arquivo, sendo ele [nomes_aleatórios](./Exercícios/Ex_Spark-Geracao_massa_dados/nomes_aleatorios.zip)

- Passo 1: Instalei a biblioteca names.

![Etapa03_Passo01](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa03_Passo1.jpg)

- Passos 2 à 5: Segui as instruções e criei o código.

![Etapa03_Passo2-5](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa03_Passo2-5.jpg)

- Rodei o código.

![Etapa03_Passo5](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa03_Passo5.jpg)

- Passo 6: Conferi os dados do arquivo gerado.
![Etapa03_Passo6](./Exercícios/Ex_Spark-Geracao_massa_dados/Evidencias/Etapa03_Passo6.jpg)

## Exercício Spark

Para esse exercício, utilizei o Google Colab por conta de problemas na instalação do spark na minha máquina.

Tendo então o código [Ex_Spark_Sprint8](./Exercícios/Ex_Spark/Ex_Spark_Sprint8.py).

- Etapa 1: Comecei importando as bibliotecas necessárias e iniciando, definindo e iniciando a sessão Spark. Além disso, abri o arquivo nomes_aleatorios.txt e carreguei em um dataframe.

![Etapa01_A](./Exercícios/Ex_Spark/Evidencias/Etapa1_A.jpg)

- Etapa 2: Visualisei uma amostra do dataframe, renomeei a coluna para Nomes e imprimi o schema do dataframe usando os comandos:

````
df_nomes = df.withColumnRenamed("_c0", "Nomes")

df_nomes.printSchema()
````

![Etapa02_A](./Exercícios/Ex_Spark/Evidencias/Etapa2_A.jpg)

![Etapa02_B](./Exercícios/Ex_Spark/Evidencias/Etapa2_B.jpg)

- Etapa 3: Adicionei uma nova coluna e atribui valores aleatórios entre Fundamental, Medio e Superior, usando o trecho de código:

````
df_nomes = df_nomes.withColumn("random_val", rand())

df_nomes = df_nomes.withColumn("Escolaridade",
    when(col("random_val") < 0.33, "Fundamental")
    .when(col("random_val") < 0.66, "Medio")
    .otherwise("Superior")).drop("random_val")
````
![Etapa3](./Exercícios/Ex_Spark/Evidencias/Etapa3.jpg)

- Etapa 4: Nessa etapa, criei uma lista de países da América do Sul, onde foi adicinado uma nova coluna ao dataframe e preenchida com os países de forma aleatória.

![Etapa4](./Exercícios/Ex_Spark/Evidencias/Etapa4.jpg)

- Etapa 5: Adiconei uma nova coluna e preenchi com valores de ano aleatório entre 1945 e 2010.

![Etapa5](./Exercícios/Ex_Spark/Evidencias/Etapa5.jpg)

- Etapa 6: Usando select e filter, selecionei as pessoas que nasceram no século 21.

![Etapa6](./Exercícios/Ex_Spark/Evidencias/Etapa6.jpg)

- Etapa 7: Refiz a pesquisa anterior, mas dessa vez usando SparkSQL.

![Etapa7](./Exercícios/Ex_Spark/Evidencias/Etapa7.jpg)

- Etapa 8: Nessa etapa, usando filter, contei o numero de pessoas que são nascidas entre 1980 e 1994 (Geração millennials)

![Etapa8](./Exercícios/Ex_Spark/Evidencias/Etapa8.jpg)

- Etapa 9: Repiti a consulta da etapa 8, porém usando Spark SQL.

![Etapa9](./Exercícios/Ex_Spark/Evidencias/Etapa9.jpg)

- Etapa 10: Agora usando Spark SQL, realizei a consulta da quantidade de pessoas de cada país que pertencem a cada geração descrita no exercício e mostrei as linhas desse novo dataframe.

![Etapa10-A](./Exercícios/Ex_Spark/Evidencias/Etapa10-A.jpg)

![Etapa10-B](./Exercícios/Ex_Spark/Evidencias/Etapa10-B.jpg)

Para mostrar todas as linhas, por ser um dataframe pequeno, usei "collect()".

![Etapa10-C](./Exercícios/Ex_Spark/Evidencias/Etapa10-C.jpg)

![Etapa10-D](./Exercícios/Ex_Spark/Evidencias/Etapa10-D.jpg)
 
 


# Certificados
Nessa sprint não houve cursos da AWS.