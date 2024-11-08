# Resumo da Sprint 1
Nessa Sprint, foi dado como objetivo aprender e desenvolver consultas em banco de dados na linguagem SQL.

Para isso, foi fornecido um curso de SQL onde ajudou a entender comandos básicos da linguagem e como tratar os dados do banco de dados.

**Resumo do curso de SQL:** 
No curso pude aprender como conecter um banco de dados, alguns comandos que foram extremamente necessários para a resolução dos exercícios e desafio.

-Funções básicas:
SELECT (coluna01, coluna02, coluna03)   --Seleciona as colunas.
FROM name_tabela            -- Dessa tabela.
WHERE condição_x            --Filtrar linhas de acordo com uma condição.
ORDER BY coluna_01 DESC     --Ordena  em ordem decrescente (ASC --ascendente).
LIMIT x                     --limita o n° de linhas da consulta.
 
-Operadores aritméticos: Servem para executar operações matemáticas.
Tipos --> +	-	*	/	^	%

-Operadores comparação: Servem para comparar dois valores retornando TRUE ou FALSE.
Tipos --> =	>	<	>=	<=	<>
Exemplo:    WHERE publicacao > '2015-01-01'

-Operadores lógicos: Usados para unir expressões simples em uma composta.
Tipos --> AND	OR	NOT	   BETWEEN	       IN	          LIKE	   ILIKE     IS NULL
Exemplo: WHERE status = 'Concluído' AND (nmcanalvendas = 'Ecommerce' OR nmcanalvendas = 'Matriz')

-Funções agregadas: Servem para executar operações aritmética nos registros de uma coluna .
Tipos --> COUNT()	    SUM()	  MIN()  	MAX()   	AVG()
Exemplo: 
SUM(qtd)  AS quantidade_vendas
SUM(qtd * vrunt) as gasto

-Função agregada GROUP BY: Serve para agrupar registros semelhantes de uma coluna. Normalmente utilizado em conjunto com as Funções de agregação.

-JOINS: Servem para combinar colunas de uma ou mais tabelas
Tipos de JOINS --> LEFT JOIN	INNER JOIN	RIGHT JOIN	FULL JOIN

-Tabelas: Criação e Deleção
	-Para criar tabelas a partir de uma query basta escrever a query normalmente e colocar o comando INTO antes do FROM informando o schema e o nome da tabela  a ser criada.

	-Para criar tabelas a partir do zero é necessário:
    (a) criar uma tabela vazia com o comando CREATE TABLE; 
    (b) Informar que valores serão inseridos com o comando INSERT INTO seguido do nome das colunas;
    (c) Inserir os valores manualmente em forma de lista após o comando VALUES

    -Para deletar uma tabela utiliza-se o comando DROP TABLE

-Tabelas: Criação, atualização e Deleção de colunas.

    -Para fazer qualquer modificação nas colunas de uma tabela utiliza-se o comando  ALTER TABLE seguido do nome da tabela.
    -Para adicionar colunas utiliza-se o comando ADD seguido do nome da coluna e da unidade da nova coluna.
    -Para mudar o tipo de unidade de uma coluna utiliza-se o comando ALTER COLUMN 
    -Para renomear uma coluna utiliza-se o comando RENAME COLUMN
    -Para deletar uma coluna utiliza-se o comando DROP COLUMN


Além disso, participei do curso AWS Partner: Sales Accreditation (Business) (Portuguese)

**Resumo curso AWS Partner: Sales Accreditation (Business) (Portuguese)**
De forma geral, pude aprender o que é computação em núvem e quais são os modelos de implantação desse serviço, porém os tópicoa mais interessantes que achei do curso foi que: 

Aprendi que a AWS presta diversos serviços, em diversas categorias, sendo elas: Computação, Armazenamento, Banco de dados,Segurança, Gerenciamento e Redes.

Além disso, os clientes possuem diferentes perspectivas diante dos resultados que o Cloud Value Framework fornece, como: Economia de custo, Produtividade da equipe, Resiliencia operacional e Agilidade empresarial.

# Exercícios
📑[Resolução do Exercício 01](../Sprint%202/Exercicios/ex01.sql)

📑[Resolução do Exercício 02](../Sprint%202/Exercicios/ex02.sql)

📑[Resolução do Exercício 03](../Sprint%202/Exercicios/ex03.sql)

📑[Resolução do Exercício 04](../Sprint%202/Exercicios/ex04.sql)

📑[Resolução do Exercício 05](../Sprint%202/Exercicios/ex05.sql)

📑[Resolução do Exercício 06](../Sprint%202/Exercicios/ex06.sql)

📑[Resolução do Exercício 07](../Sprint%202/Exercicios/ex07.sql)

📑[Resolução do Exercício 08](../Sprint%202/Exercicios/ex08.sql)

📑[Resolução do Exercício 09](../Sprint%202/Exercicios/ex09.sql)

📑[Resolução do Exercício 10](../Sprint%202/Exercicios/ex10.sql)

📑[Resolução do Exercício 11](../Sprint%202/Exercicios/ex11.sql)

📑[Resolução do Exercício 12](../Sprint%202/Exercicios/ex12.sql)

📑[Resolução do Exercício 13](../Sprint%202/Exercicios/ex13.sql)

📑[Resolução do Exercício 14](../Sprint%202/Exercicios/ex14.sql)

📑[Resolução do Exercício 15](../Sprint%202/Exercicios/ex15.sql)

📑[Resolução do Exercício 16](../Sprint%202/Exercicios/ex16.sql)

📑[Resolução do Exercício exportação de dados 3.1 ](../Sprint%202/Exercicios/exII_3.1etapa1.csv)

📑[Resolução do Exercício exportação de dados 3.2](../Sprint%202/Exercicios/exII_3.2etapa2.csv)

# Evidências
Para a resolução dos exercícios, abri os bancos de dados fornecidos no Dbeaver e fui resolvendo primeiro pelo computador, para depois colocar os resultados na plataforma da Udemy.

Para a resolução, precisei procurar alguns vídeos por fora do curso, por ser meu primeiro contato com a linguagem, tive dificuldades em lembrar a sintax.

Os exercícos referente a biblioteca, achei mais tranquilos, usando comandos mais simples e básicos.

Somente o exercicio 05, que tive um pouco de dificuldade para pensar na sintax correta.
![Exercício 05](../Sprint%202/Evidencias/Ex_05.jpg)

Os exercícios referente a loja, achei um pouco mais complexos, tendo que usar algumas funções.

Como por exemplo, no exercício 09, tive que usar o seguinte trecho de query para selecionar o produto entre as datas e com status concluído.
```sql
WHERE dtven BETWEEN '2014-02-03' AND '2018-02-02'
	AND status = 'Concluído'
```
![Exercício09](../Sprint%202/Evidencias/Ex_09.jpg)

O exercício 10 também tive um pouco de dificuldade, precisando pedir ajuda aos colegas para entender como realizar o cálculo da comissão e como arredondar o valor com duas casas decimais. Sendo necessário usar o seguinte trecho.
```sql
ROUND(SUM(t2.qtd *t2.vrunt) * (t.perccomissao)/100,2) as comissao
```
![Exercício10](../Sprint%202/Evidencias/Ex_10.jpg)

Os demais exercícios consegui concluir após estudar e entender melhor a linguagem.

# Certificados
Após o término do curso AWS Partner: Sales Accreditation (Business) (Portuguese), recedi o [Certificado AWS](../Sprint%202/Certificados/RafaelaCGomes_AWS%20Course%20Completion%20Certificate.pdf)

