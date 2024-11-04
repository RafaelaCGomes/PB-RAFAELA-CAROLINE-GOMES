 /*Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
 O resultado deve conter apenas as colunas quantidade, nome, estado e cidade.
 Ordenar as linhas pela coluna que representa a quantidade de livros 
 em ordem decrescente.*/
 
 SELECT COUNT(livro.editora) as quantidade,
 		editora.nome,
 		endereco.estado,
 		endereco.cidade
 from livro 
 join editora on editora.codeditora = livro.editora
 JOIN endereco on editora.endereco = endereco.codendereco
 GROUP by editora.nome, endereco.estado, endereco.cidade
 order by quantidade desc
 limit 5;
 
 

