/*E06 - Apresente a query para listar o autor com maior número de livros publicados.
 O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.*/

 SELECT  autor.codautor,
	autor.nome,
	COUNT(livro.autor) as quantidade_publicacoes
FROM autor 
join livro on autor.codautor = livro.autor 
GROUP BY autor.nome 
ORDER BY quantidade_publicacoes DESC 
LIMIT 1;


