/*E05 - Apresente a query para listar o nome dos autores que 
publicaram livros através de editoras NÃO situadas na região 
sul do Brasil. Ordene o resultado pela coluna nome, em ordem 
crescente. 
Não podem haver nomes repetidos em seu retorno.*/

SELECT DISTINCT autor.nome
FROM autor    
join livro on autor.codautor = livro.autor 
JOIN editora on livro.editora = editora.codeditora 
JOIN endereco on editora.endereco = endereco.codendereco 
WHERE endereco.estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY autor.nome ASC;



 

