/*E10 - A comissão de um vendedor é definida a partir de um percentual sobre o 
total de vendas (quantidade * valor unitário) por ele realizado. 
O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
Com base em tais informações, calcule a comissão de todos os vendedores,
considerando todas as vendas armazenadas na base de dados com status concluído.
As colunas presentes no resultado devem ser vendedor(tbvendedor.nmvdd), valor_total_vendas e comissao.
O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.*/

SELECT t.nmvdd as vendedor,
	SUM(t2.qtd *t2.vrunt) as valor_total_vendas,
	ROUND(SUM(t2.qtd *t2.vrunt) * (t.perccomissao)/100,2) as comissao
FROM tbvendedor t 
join tbvendas t2 on t.cdvdd = t2.cdvdd
WHERE t2.status = 'Concluído'
GROUP BY t.nmvdd 
ORDER BY comissao DESC




