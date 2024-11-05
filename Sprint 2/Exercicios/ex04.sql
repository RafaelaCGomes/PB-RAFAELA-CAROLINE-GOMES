 /*E04 - Apresente a query para listar a quantidade de livros publicada por cada autor. 
Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).*/
 
SELECT autor.nome,
 	autor.codautor,
 	autor.nascimento,
 	COUNT(livro.autor) as quantidade
from autor 
left join livro on autor.codautor = livro.autor
group by autor.nome, autor.codautor, autor.nascimento
ORDER by autor.nome  


 
 

