/*E07 - Apresente a query para listar o nome dos autores com nenhuma publicação.
Apresentá-los em ordem crescente.*/

SELECT autor.nome
FROM autor 
left JOIN livro on autor.codautor = livro.autor 
WHERE livro.titulo IS NULL;




