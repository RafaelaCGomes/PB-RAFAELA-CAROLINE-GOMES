--Criação da tabela cliente.
CREATE TABLE cliente (
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR (100),
	cidadeCliente VARCHAR (100),
	estadoCliente VARCHAR (100),
	paisCliente VARCHAR (100)
);
--criação da tabela carro.
CREATE TABLE carro (
	idCarro INT PRIMARY KEY,
	kmCarro INT,
	classiCarro VARCHAR (100),
	marcaCarro VARCHAR (100),
	modeloCarro VARCHAR (100),
	anoCarro INT
);
--Alteração da tabela carro para adicionar a coluna idCombustivel.
ALTER TABLE carro ADD idCombustivel INT

--Criação da tabela combustivel.
CREATE TABLE combustivel (
	idCombustivel INT PRIMARY KEY,
	tipoCombustivel INT
);
	
SELECT *
FROM combustivel c 





