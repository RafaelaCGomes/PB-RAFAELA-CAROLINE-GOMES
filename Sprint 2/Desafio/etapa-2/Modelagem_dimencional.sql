--Consultas relacional.
SELECT * FROM Locacao l 
SELECT * FROM Carro c 
SELECT * FROM Combustivel c 
SELECT * FROM Cliente c 
SELECT * FROM Vendedor v 

--Criação de tabelas para a modelagem dimencional.

--Dimensao vendedor
CREATE TABLE dim_vendedor(
	id INT NOT NULL PRIMARY KEY,
	nome VARCHAR (100),
	sexo SMALLINT (10),
	estado VARCHAR (100)
);

--Dimensao Cliente
CREATE TABLE dim_cliente (
	id INT NOT NULL PRIMARY KEY ,
	nome VARCHAR (100),
	cidade VARCHAR (100),
	estado VARCHAR (100),
	pais VARCHAR (100)
);

--Dimensão Carro
CREATE TABLE dim_carro (
	id INT NOT NULL PRIMARY KEY,
	km INT,
	classi VARCHAR (100),
	marca VARCHAR (100),
	modelo VARCHAR (100),
	ano INT,
	idCombustivel INT,
	tipoCombustivel INT
);

--Fato locacao
CREATE TABLE ft_locacao (
	idLocacao INT NOT NULL PRIMARY KEY,
	idCliente INT,
	idVendedor INT,
	idCarro INT,
	dataLocacao DATE,
	horaLocacao TIME,
	qtdDiaria INT,
	vlrDiaria DECIMAL (5,2),
	dataEntrega DATE,
	horaEntrega TIME,
	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
	FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor),
	FOREIGN KEY (idCarro) REFERENCES Carro(idCarro)
);

--Dados na tabela dim_vendedor.
INSERT INTO dim_vendedor (id,nome, sexo, estado)
SELECT DISTINCT idVendedor,nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor ;

--Dados na tabela dim_cliente.
INSERT INTO dim_cliente (id, nome, cidade, estado, pais)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente ;

--Dados na tabela dim_carro.
INSERT INTO dim_carro (id, km, classi, marca, modelo, ano, idCombustivel, tipoCombustivel )
SELECT DISTINCT c.idCarro,
	c.kmCarro,
	c.classiCarro,
	c.marcaCarro,
	c.modeloCarro,
	c.anoCarro,
	c.idCombustivel,
	cm.tipoCombustivel 
FROM Carro c
JOIN Combustivel cm on c.idCombustivel = cm.idCombustivel 


--Dados na tabela ft_locação.
INSERT INTO ft_locacao  (idLocacao, idCliente, idVendedor, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega )
SELECT DISTINCT idLocacao, idCliente, idVendedor, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM Locacao ;





--Conculta dimensionamento.
SELECT * FROM dim_vendedor;
SELECT * FROM dim_cliente;
SELECT * FROM dim_carro;
SELECT * FROM ft_locacao;

	

















