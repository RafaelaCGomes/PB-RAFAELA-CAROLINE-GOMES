/*E12 - Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor 
valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep,
dtnasc e valor_total_vendas.*/

SELECT 
    t2.cddep,
    t2.nmdep,
    t2.dtnasc,
    SUM(t.qtd * t.vrunt) AS valor_total_vendas
FROM tbvendas t 
LEFT JOIN tbdependente t2 ON t.cdvdd = t2.cdvdd
WHERE t.status = 'Concluído' 
GROUP BY t.cdvdd 
ORDER BY valor_total_vendas
LIMIT 1





