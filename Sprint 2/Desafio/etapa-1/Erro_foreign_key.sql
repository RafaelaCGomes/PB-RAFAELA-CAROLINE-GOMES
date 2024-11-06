CREATE TABLE vendedor(
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR (100),
	sexoVendedor SMALLINT (10),
	estadoVendedor VARCHAR (100)
);

INSERT INTO vendedor (idVendedor)
SELECT DISTINCT idVendedor 
FROM tb_locacao;

ALTER TABLE tb_locacao 
ADD CONSTRAINT fk_idVendedor
FOREIGN KEY (idVendedor)
REFERENCES vendedor(idVendedor)






