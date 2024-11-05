/*E08 - Apresente a query para listar o código e o nome do vendedor com maior número de vendas 
(contagem), e que estas vendas estejam com o status concluída.  
As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.*/

SELECT  t.cdvdd , t.nmvdd
FROM tbvendedor t
join tbvendas t2 on t.cdvdd = t2.cdvdd 
WHERE t2.status = 'Concluído'
GROUP BY t.cdvdd , t.nmvdd 
ORDER BY COUNT(t2.cdvdd) DESC 
LIMIT 1
