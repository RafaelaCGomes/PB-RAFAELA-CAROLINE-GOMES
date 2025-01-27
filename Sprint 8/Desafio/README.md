# Resumo e Objetivo
 
O desafio da Sprint7 teve como objetivo utilizar a API do TMDB para buscar dados dos filmes que não estão no CSV, salvar esses dados em JSON em um bucket S3.

Para o desafio, após ter criado minha Chave da API no exercício do TMDB, utilizei ela para testar meu código localmente e após isso, fiz as alterações necessárias para rodar no Lambda.

Separei o desafio em 4 etapas, pois achei mais fácil de explicar os passos que segui para realizá-lo.

# Etapas

## [Etapa-01: ](../Desafio/Etapa-01/)
Comecei pensando em quais filmes eu precisaria para miha analise, como pensei em analisar uma franquia de filmes específica, achei interessante pegar do tmdb, somente os dados dos filmes entre os anos em que foi lançado filme dessa franquia.

Criei então um arquivo [tabelas.ipynb](../Desafio/Etapa-01/tabelas.ipynb) onde filtrei os dados do arquivo filmes.csv que eu queria, ou seja, selecionei todos os filmes entre os anos 1970 a 2019 e do gênero fantasy.

![Etapa01_A](../Evidencias/Etapa01_A.jpg)

![Etapa01_B](../Evidencias/Etapa01_B.jpg)

![Etapa01_C](../Evidencias/Etapa01_C.jpg)

![Etapa01_D](../Evidencias/Etapa01_D.jpg)

![Etapa01_E](../Evidencias/Etapa01_E.jpg)

![Etapa01_F](../Evidencias/Etapa01_F.jpg)

![Etapa01_G](../Evidencias/Etapa01_G.jpg)

Resultando em [filmes_unicos.csv](../Desafio/Etapa-01/filmes_unicos.csv), que contém os ids únicos dos filmes do gênero Fantasy, entre os anos de 1970 a 2019.


## [Etapa-02](../Desafio/Etapa-02/)

Fiz um teste local, onde conferi se estava funcionando corretamente o código.

Para isso criei o [teste_tmdb_local.py](../Desafio/Etapa-02/teste_tmdb_local.py), que rodei localmente e obtive como resultado uma pasta local com arquivo JSON.

![Etapa-02_A](../Evidencias/Etapa02_A.jpg)

![Etapa-02_B](../Evidencias/Etapa02_B.jpg)


## [Etapa-03](../Desafio/Etapa-03/)

Em seguida fiz um Dockerfile e criei uma imagem.

![Etapa03_A](../Evidencias/Etapa03_A.jpg)

Criei a imagem e rodei um container para zipar a biblioteca requests e o arquivo filmes_unicos.csv para adicionar a Layer do Lambda.

![Etapa03_B](../Evidencias/Etapa03_B.jpg)

![Etapa03_C](../Evidencias/Etapa03_C.jpg)

![Etapa03_D](../Evidencias/Etapa03_D.jpg)

## [Etapa-04](../Desafio/Etapa-04/)

Alterei o código python para conseguir implantar no Lambda, tendo assim o [teste_AWS.py](../Desafio/Etapa-04/teste_AWS.py)

![Etapa04_A](../Evidencias/Etapa04_A.jpg)

Fui para a AWS, criei minha função Lambda e adicionei a camada criada.
![Etapa04_B](../Evidencias/Etapa04_B.jpg)

Atualizei as permissões necessárias para a função ter acesso ao bucketS3.

![Etapa04_C](../Evidencias/Etapa04_C.jpg)

Atualizei as variáveis de ambiente.
![Etapa04_D](../Evidencias/Etapa04_D.jpg)

Para conferir, o bucket antes de rodar o código pyhton no Lambda.

![Etapa04_E](../Evidencias/Etapa04_E_bucket_antes.jpg)

Inplementei o código e rodei.
![Etapa04_F1](../Evidencias/Etapa04_F1.jpg)

![Etapa04_F](../Evidencias/Etapa04_F.jpg)

Voltando ao BucketS3, é possivel ver que foi criado e salvo os JSON.

![Etapa04_G](../Evidencias/Etapa04_G.jpg)

![Etapa04_H](../Evidencias/Etapa04_H.jpg)