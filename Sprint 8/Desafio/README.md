# Resumo e Objetivo
 
O desafio da sprint 8 teve como objetivo criar scripts para trasformar os arquivos do diretório Raw do bucket S3 para Parquet, utilizando jobs do AWS Glue.

Os scripts usados no Glue foram salvos em .py e estão disponíveis como: [script_glue_csv.py](./Scripts/script_glue_csv.py) e [script_glue_json.py](./Scripts/script_glue_json.py)

O arquivo [script_glue_csv.py](./Scripts/script_glue_csv.py) foi usado para o tratamento de dados e a transformação dos arquivos csv de origem local salvos no S3 para parquet.

Já o script [script_glue_json.py](./Scripts/script_glue_json.py) foi usado para o tratamento e transformação dos jsons salvos no bucket de origem do TMDB.

Ao desenvolver do desafio, acabei alterando algumas perguntas do desafio final, chegando até o momento com as seguintes perguntas norteadoras da análise:

1- Qual foi o filme com maior e menor votos da franquia Star Wars? Em quais anos foram lançados esses dois filmes? (Top 2 filmes + votados e menos votados da franquia)

2- Pensando nos anos de lançamento desses dois filmes (maior e menor votação Star Wars), quais outros filmes que possuem votação maior/menor que esses, sem serem da franquia Star Wars? ( 2 filmes mais votados e 2 menos votados fora da franquia, do mesmo ano dos filmes Star Wars)

3- Qual o orçamento e receita dos filmes de maior e menor votação da franquia e fora da franquia?

4- Todos os filmes da Star Wars foram feitos pelo mesmo produtor?  Qual a produtora que gravou os filmes de maior e menor votação da franquia?

5- Qual a produtora dos outros filmes (maior e menor) votação fora da franquia?

6- A popularidade desses filmes ( mais e menos votos Star Wars e mais e menos votos fora da franquia) corresponde ao número de votos? Comparar popularidade com número de votos

# Etapas

## Etapa 1

Comecei escrevendo os scripts e tentando localmente utilizando o Google Colab. Após testar e rodar localmente, fiz as alterações necessárias para implementar no Glue.

## Etapa 2
No script [script_glue_csv.py](./Scripts/script_glue_csv.py), fiz as alterações para que rodasse no Glue.

Comecei importando as bibliotecas necessárias para a execusão e iniciei a sessão do Glue e spark, além de declarar os parametros necessários para a execução do job.

![etapa02_01A](../Evidencias/etapa02_01A.jpeg)

![etapa02_01B](../Evidencias/etapa02_01B.jpeg)

Comecei criando uma função para processar o csv.

![etapa02_02](../Evidencias/etapa02_02.jpeg)

A função começa lendo o csv e criando um Dynamicframe com base no csv que está salvo no bucket S3.

```
df_dynamic = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths" :[s3_input_path]},
        format="csv",
        format_options={"withHeader" : True, "separator": "|" })
```
Em seguida, a função converte esse Dynamicframe para dataframe.

```
        df = df_dynamic.toDF() 
```
Após analisar o arquivo csv, observei que todas as colunas estavam como string, então fiz a conversão de algumas colunas para integer, utilizando o trecho de código:
```
#Conversão da coluna anoLancamento, tempoMinutos, anoNascimento, anoFalecimento para number se existir
        colunas_converter = ['anoLancamento','tempoMinutos','anoNascimento','anoFalecimento']
        for coluna in colunas_converter:
            if coluna in df.columns:
                df = df.withColumn(coluna, col(coluna).cast(IntegerType()))
```
Como vou usar essa função para processar os csv de series e filmes, quis ter certeza que fosse gerado somente um parquet para cada arquivo csv, para isso usei a função "coalesce(1)" para garatir somente uma partição do dataframe.

```
        df = df.coalesce(1)
```
Por fim, a função converte o dataframe novamente para Dynamicframe, salva em parquet no path_output do s3, tendo saídas de erros, caso ocorra.

![etapa02_03](../Evidencias/etapa02_03.jpeg)

Por fim, no script chamo a função e informo os paths de entrada e saída para o arquivo movies.csv e series.csv do bucket S3, encerrando em seguida o job.

```
#processar cada arquivo
processo_csv(s3_input_path_movies, s3_output_path_movies)
processo_csv(s3_input_path_series, s3_output_path_series)

job.commit()
```
## Etapa 3
Já no script [script_glue_json.py](../Scripts/script_glue_json.py), após rodar localmente, realizei as alterações necessárias também para rodar em um job do Glue.

Iniciei o script inportando as bibliotecas necessárias, definindo os parâmetros e declarando os paths.

![etapa03_01](../Evidencias/etapa03_01.jpeg)

Em seguida, li todos os arquivos jsons existentes no bucket s3 e converti o dinamic frame em dataframe, utilizando o trecho a seguir:
```
df_dynamic = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths" :[s3_input_path_json]},
        format="json",
        format_options={
            "multiline":True,
            "mode":"PERMISSIVE"})
#Converte DynamicFrame em dataframe.
df = df_dynamic.toDF()
```
Em seguida, realizei alguns tratamentos das colunas que achei necessárias conforme a minha análise.

Comecei excluindo a coluna spoken_languages, pois não irei utilizá-la e explodi as informações das colunas production_companies, production_countries e genres.

![etapa03_02](../Evidencias/etapa03_02.jpeg)

Nesse momento percebi que ficaria mais organizado se eu separasse a coluna production_companies em outro dataframe para ser particionado e salvo em um arquivo parquet separado, pois a coluna contém informações importantes que usarei em minha análise.

Para isso, o primeiro dataframe defini como movies que contém as colunas com informações sobre os filmes e uma coluna com o id_production_companies para garantir o vínculo com o outro dataframe.

```
# Criar DataFrame do primeiro Parquet - movies
parquet1_df = exploded_df.select(
    "adult",
    "backdrop_path",
    "belongs_to_collection",
    "budget",
    col("genre.id").alias("genre_id"),
    col("genre.name").alias("genre_name"),
    "homepage",
    "id",
    "imdb_id",
    "origin_country",
    "original_language",
    "original_title",
    "overview",
    "popularity",
    "poster_path",
    col("production_company.id").alias("id_production_companies"),
    "production_countries",
    col("production_countries.iso_3166_1").alias("iso_3166_1"),
    col("production_countries.name").alias("country_name"),
    "release_date",
    "revenue",
    "runtime",
    "status",
    "tagline",
    "title",
    "video",
    "vote_average",
    "vote_count"
)
```
Já o segundo dataframe defini como production_companies que contém as colunas com informações sobre as produtoras, garanti que ouvesse somente as linhas que não estavam repetidas.

```
# Criar DataFrame do segundo Parquet - production_companies
parquet2_df = exploded_df.select(
    col("production_company.id").alias("id_production_companies"),
    col("production_company.logo_path"),
    col("production_company.name"),
    col("production_company.origin_country")
).dropDuplicates()
```
Em seguida, garanti que os dois dataframes fossem salvos em uma única partição, converti ambos os dataframes novamente em Dynamicframes e salvei ambos em parquet no bucket s3.

![etapa03_03](../Evidencias/etapa03_03.jpeg)

## Etapa 4

Com ambos os scripts prontos e adaptados para o job Glue, implementei e rodei ambos.

Antes do passos do Glue, acho interessante mostrar a estrutura do bucket S3.

![etapa04_01](../Evidencias/etapa04_01.jpeg)

![etapa04_02](../Evidencias/etapa04_02.jpeg)

Criei o IAM para a execução dos jobs.

![etapa04_03](../Evidencias/etapa04_03.jpeg)

Configurei o AWS Lake Formation.
![etapa04_04](../Evidencias/etapa04_04.jpeg)

Implementei o [script_glue_csv](../Scripts/script_glue_csv.py) no job glue e configurei todos os detalhes do job.

![etapa04_05](../Evidencias/etapa04_05.jpeg)

![etapa04_06](../Evidencias/etapa04_06.jpeg)

![etapa04_07](../Evidencias/etapa04_07.jpeg)

Rodei o job e conferi se os arquivos csv haviam sendo salvos corretamente no bucket S3.

![etapa04_08](../Evidencias/etapa04_08.jpeg)

![etapa04_09](../Evidencias/etapa04_09.jpeg)

![etapa04_10](../Evidencias/etapa04_10.jpeg)

Em seguida, implementei o [script_glue_json](../Scripts/script_glue_json.py) em um novo job e configurei todos os detalhes do job.

![etapa04_11](../Evidencias/etapa04_11.jpeg)

![etapa04_12](../Evidencias/etapa04_12.jpeg)

Rodei o job e conferi no bucket S3 se os arquivos parquet haviam sido salvos corretamente.
![etapa04_13](../Evidencias/etapa04_13.jpeg)

![etapa04_14](../Evidencias/etapa04_14.jpeg)

![etapa04_15](../Evidencias/etapa04_15.jpeg)

![etapa04_16](../Evidencias/etapa04_16.jpeg)

## Etapa 5
Em seguida, realizei crawles com base nos parquet gerados e conferi no Athena se as informações estavam completas.

1- Iniciei criando e rodando a crawler do parquet de origem do csv movies/local.
![etapa05_01](../Evidencias/etapa05_01.jpeg)
No Athena, realizei uma consulta breve somente para conferir.
![etapa05_02](../Evidencias/etapa05_02.jpeg)
![etapa05_03](../Evidencias/etapa05_03.jpeg)

2- Em seguida criei e rodei a crawler do parquet de origem do csv series/local.
![etapa05_04](../Evidencias/etapa05_04.jpeg)
E realizei um consulta no Athena.
![etapa05_05](../Evidencias/etapa05_05.jpeg)
![etapa05_06](../Evidencias/etapa05_06.jpeg)

3- Criei e rodei a crawler do parquet de origem dos json/TMDB, nesse caso do parquet production_companies.
![etapa05_07](../Evidencias/etapa05_07.jpeg)
Realizei uma consulta no Athena.
![etapa05_08](../Evidencias/etapa05_08.jpeg)
![etapa05_09](../Evidencias/etapa05_09.jpeg)

4- Por fim criei a crawler do parquet  movies de origem dos json/TMDB.
![etapa05_10](../Evidencias/etapa05_10.jpeg)
Realizei a consulta no Athena.
![etapa05_11](../Evidencias/etapa05_11.jpeg)
![etapa05_13](../Evidencias/etapa05_13.jpeg)

Por fim, obtive 4 tabelas disponíveis no Glue Catalog de origem Parquet, sendo duas (movies e series) pertencente a local e duas (movies_47c... e production_companies) pertencente a TMDB.

![etapa05_14](../Evidencias/etapa05_14.jpeg)