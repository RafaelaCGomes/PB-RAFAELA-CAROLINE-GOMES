CREATE TABLE vendedor(
	idVendedor INT NOT NULL PRIMARY KEY,
	nomeVendedor VARCHAR (100),
	sexoVendedor SMALLINT (10),
	estadoVendedor VARCHAR (100)
);

INSERT INTO vendedor (idVendedor,nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor,nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;


SELECT *
FROM vendedor v 


