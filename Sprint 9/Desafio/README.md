# Resumo e Objetivo
 
O desafio da sprint 9 consistiu em realizar job no GLue para criar uma nova camada chamada Refined com as colunas necessárias para a realização da análise com base nos dados da camada Trusted.


# Etapas

## Etapa 1
Iniciei o desafio realizando consultas no Athena as tabelas criadas na sprint 8, para definir quais colunas irei usar na modelagem e quais tratamentos será necessário realizar.

![Etapa01A](../Evidencias/etapa01A.jpeg)

![Etapa01B](../Evidencias/etapa01B.jpeg)

Em seguida criei views das tabelas que vou utilizar no dimensionamento dos dados.

View da tabela fato filmes
![View_fato_filmes](../Evidencias/etapa01_fato_filmes.jpeg)

![View_fato_filmesA](../Evidencias/etapa01_fato_filmesA.jpeg)

View da dimensão filme
![View_dim_filme](./Evidencias/etapa01_dim_filme.jpeg)

![View_dim_filmeA](../Evidencias/etapa01_dim_filmeA.jpeg)

View da dimensão gênero
![View_dim_genero](../Evidencias/etapa01_dim_genero.jpeg)

![View_dim_generoA](../Evidencias/etapa01_dim_generoA.jpeg)

View da dimensão produtora
![View_dim_produtora](../Evidencias/etapa01_dim_produtora.jpeg)

![View_dim_produtoraA](../Evidencias/etapa01_dim_produtoraA.jpeg)

View da dimensão pais produtora
Nessa tabela percebi que precisaria explodir a coluna para desmenbrar o iso do pais e o nome, criando uma tabela com o id e o nome, e manter na fato somente o id.

O mesmo será necessário fazer para a dimensão coleção.

![View_dim_pais_producao](../Evidencias/etapa01_dim_pais_producao.jpeg)

![View_dim_pais_producaoA](../Evidencias/etapa01_dim_pais_producaoA.jpeg)

![view_dim_coleção](../Evidencias/etapa01_dim_coleção.jpeg)

## Etapa 2
Usando o modelo das views criadas no Athena e usando o DbDesigner online, criei um desenho da modelagem criada.

Tendo como resultado:
![Modelo_dimensional](../Evidencias/modelo_dimensional.jpeg)

## Etapa 3
Iniciei então a escrita do script do job do Glue.

