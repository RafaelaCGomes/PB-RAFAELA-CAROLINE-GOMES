/* E13- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz 
(Considerar apenas vendas concluídas). 
As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.*/

SELECT 
	cdpro, 
    nmcanalvendas, 
    nmpro,
    SUM(qtd)  AS quantidade_vendas
FROM tbvendas t 
WHERE status = 'Concluído'
    AND (nmcanalvendas = 'Ecommerce' OR nmcanalvendas = 'Matriz')
GROUP BY 
    cdpro, nmcanalvendas, nmpro
ORDER BY 
    quantidade_vendas ASC
LIMIT 10;






