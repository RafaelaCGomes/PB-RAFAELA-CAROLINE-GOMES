--Criação da tabela vendedor.
CREATE TABLE Vendedor(
	idVendedor INT NOT NULL PRIMARY KEY,
	nomeVendedor VARCHAR (100),
	sexoVendedor SMALLINT (10),
	estadoVendedor VARCHAR (100)
);
--Criação da tabela cliente.
CREATE TABLE Cliente (
	idCliente INT NOT NULL PRIMARY KEY,
	nomeCliente VARCHAR (100),
	cidadeCliente VARCHAR (100),
	estadoCliente VARCHAR (100),
	paisCliente VARCHAR (100)
);

--Criação da tabela combustivel.
CREATE TABLE Combustivel (
	idCombustivel INT NOT NULL PRIMARY KEY,
	tipoCombustivel INT
);

--Criação da tabela carro.
CREATE TABLE Carro (
	idCarro INT NOT NULL PRIMARY KEY,
	kmCarro INT,
	classiCarro VARCHAR (100),
	marcaCarro VARCHAR (100),
	modeloCarro VARCHAR (100),
	anoCarro INT,
	idCombustivel INT,
	FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);


--Alteração do nome da tabela antiga.
ALTER TABLE tb_locacao RENAME TO Antiga_tb_locacao;

--Criação da tabela locacao.
CREATE TABLE Locacao (
	idLocacao INT NOT NULL PRIMARY KEY,
	dataLocacao DATE,
	horaLocacao TIME,
	qtdDiaria INT,
	vlrDiaria DECIMAL (5,2),
	dataEntrega DATE,
	horaEntrega TIME,
	idCliente INT,
	idVendedor INT,
	idCarro INT,
	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
	FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor),
	FOREIGN KEY (idCarro) REFERENCES Carro(idCarro)
);

--Dados na tabela vendedor.
INSERT INTO Vendedor (idVendedor,nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor,nomeVendedor, sexoVendedor, estadoVendedor
FROM Antiga_tb_locacao ;

SELECT *
FROM Vendedor v ;

--Dados na tabela cliente.
INSERT INTO Cliente (idCliente, nomeCliente, CidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Antiga_tb_locacao ;

SELECT *
FROM Cliente c ;
	
--Dados na tabela combustivel.
INSERT INTO Combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel , tipocombustivel
FROM Antiga_tb_locacao ;

SELECT *
FROM Combustivel c ;

--Dados na tabela carro.
INSERT INTO Carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel )
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel 
FROM Antiga_tb_locacao 
WHERE kmCarro = (
	SELECT MAX(kmCarro)
	FROM Antiga_tb_locacao AS kmMax
	WHERE kmMax.idCarro = Antiga_tb_locacao.idCarro
) GROUP BY idCarro;

SELECT *
FROM Carro c ;

--Dados na tabela Locação.
INSERT INTO Locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idVendedor, idCarro)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idVendedor, idCarro
FROM Antiga_tb_locacao ;


SELECT *
FROM Locacao l ;


--Formatação da coluna horaLocacao.
UPDATE Locacao 
SET horaLocacao = printf('%02d:%s', CAST(substr(horaLocacao , 1, instr(horaLocacao , ':') - 1) AS INTEGER), substr(horaLocacao , instr(horaLocacao , ':') + 1));

--Formatação da coluna dataLocação para YYYY-MM-DD.
UPDATE Locacao 
SET dataLocacao = substr(dataLocacao, 1, 4) || '-' || substr(dataLocacao, 5, 2) || '-' || substr(dataLocacao , 7, 2);

--Formatação da coluna dataEntrega para YYYY-MM-DD.
UPDATE Locacao 
SET dataEntrega = substr(dataEntrega , 1, 4) || '-' || substr(dataEntrega , 5, 2) || '-' || substr(dataEntrega , 7, 2);

SELECT *
FROM Locacao l ;


--Deletando a antiga tabela locação.

DROP TABLE Antiga_tb_locacao ;














































