#!/bin/bash
##################################################################
#Nome: consolidador_de_processamento_de_vendas.sh		 #
#								 #
#Autor: Rafaela Caroline Gomes					 #
#								 #
#Descrição: O script juntará dados de relatórios gerados 	 #
#	diariamente por outro script, formando um novo relatório #
#	chamado relatorio_final.txt				 #
#								 #
#Uso: Manual							 #
##################################################################

SUBDIR="/home/rafaela/ecommerce/vendas/backup"
RELATORIO_F="relatorio_final.txt"

#Criação do relatorio final.
touch "$RELATORIO_F"
if [ -f "/home/rafaela/ecommerce/relatorio_final.txt" ]; then
	echo "Relatório criado"
else
	echo "Relatorio não criado"
fi
#Procura os arquivos e concatena o conteudo e insere no relatorio final
for relatorio in "$SUBDIR"/*.txt ; do
	cat "$relatorio" >> "$RELATORIO_F"
done
echo "Arquivos unidos em "$RELATORIO_F"."

