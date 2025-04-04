#!/bin/bash

###################################################################
# Nome: processamento_de_vendas.sh				   #
#								   #
# Autor: Rafaela Caroline Gomes					   #
#								   #
#Descrição: O Script fará a criação de diretórios, copiará arquivo #
#	dados_de_vendas.csv, cria subdiretório, renomeia o arquivo,#
#	cria um novo arquivo .txt onde contém alguns dados,        #
#	especifícos gerando um relatório.			   #
# Uso: Agendamento.						   #
##################################################################

DIRETORIO_VENDAS="/home/rafaela/ecommerce/vendas"

#Criação do diretorio VENDAS
if [ -d "$DIRETORIO_VENDAS" ]; then
	echo "O diretório vendas já existe"
else
	mkdir "$DIRETORIO_VENDAS"
	echo "Diretório vendas criado"
fi

#Arquivo a ser copiado para dentro de vendas
ARQUIVOS_DADOS="/home/rafaela/ecommerce/dados_de_vendas.csv"
cp "$ARQUIVOS_DADOS" "vendas"
echo "Arquivo dados_de_vendas copiado para o diretório vendas"


SUBDIR_BACKUP="/home/rafaela/ecommerce/vendas/backup"
#Criação do subdiretório backup
if [ -d "$SUBDIR_BACKUP" ]; then
	echo "O subdiretório backup já existe"
else
	mkdir "$SUBDIR_BACKUP" 
	echo "Subdiretório backup criado"
fi

#Obtenção da data de execução no formato yyyymmdd e redefinição do nome do arquivo em backup.
DATA_EXECUCAO=$(date +"%y%m%d")
NOVO_ARQUIVO_BACKUP="dados-$DATA_EXECUCAO.csv"
cp "$ARQUIVOS_DADOS" "$SUBDIR_BACKUP/$NOVO_ARQUIVO_BACKUP"
echo "Arquivo '$ARQUIVOS_DADOS' copiado para '$SUBDIR_BACKUP' com o nome '$NOVO_ARQUIVO_BACKUP'."

#Renomeação do nome do arquivo dados-<yyyymmdd>.csv para bakup-dados-<yyyymmdd>.csv dentro de backup.
BACKUP_DADOS="backup-dados-$DATA_EXECUCAO.csv"
if [ -f "$SUBDIR_BACKUP/$NOVO_ARQUIVO_BACKUP" ]; then
	mv "$SUBDIR_BACKUP/$NOVO_ARQUIVO_BACKUP" "$SUBDIR_BACKUP/$BACKUP_DADOS"
	echo "Arquivo '$NOVO_ARQUIVO_BACKUP' renomeado para '$BACKUP_DADOS' dentro do diretório '$SUBDIR_BACKUP'."
else 
	echo "Arquivo '$NOVO_ARQUIVO_BACKUP' não encontrado."
fi
echo""
#Declaração das informações do relatório.txt
ARQUIVO_DADOS_VEND="/home/rafaela/ecommerce/vendas/dados_de_vendas.csv"
ARQUIVO="/home/rafaela/ecommerce/vendas/backup/backup-dados-$DATA_EXECUCAO.csv"
if [ -f "$ARQUIVO" ]; then
	echo "Arquivo '$ARQUIVO' encontrado"
else
	echo "Arquivo '$ARQUIVO' não encontrado"
fi
echo""
DATA_RELATORIO=$(date +"%y%m%d %H:%M")
DATA_PRIM_REGISTRO=$(head -n 2 "$ARQUIVO" | cut -d, -f5)
DATA_ULT_REGISTRO=$(tail -n 1 "$ARQUIVO" | cut -d, -f5)
QUANT_ITENS_DIF=$( tail -n +2 "$ARQUIVO" | cut -d, -f2  | sort -u | wc -l)
DEZ_PRIMEIRAS_LINHAS=$( tail -n +2 "$ARQUIVO" | head -n 10 )

echo "As dez primeiras linhas do arquivo '$ARQUIVO_ORIG' é:"
echo "'$DEZ_PRIMEIRAS_LINHAS'"
echo""

#Criação dos arquivo relatório.txt em backup
RELATORIO_TXT="relatorio-$DATA_EXECUCAO.txt"
touch "$SUBDIR_BACKUP/$RELATORIO_TXT"
{
echo "Data do sistema: '$DATA_RELATORIO'. "
echo""
echo "Data do primeiro registro: '$DATA_PRIM_REGISTRO'."
echo""
echo "Data do último registro: '$DATA_ULT_REGISTRO'."
echo""
echo "Quantidade de itens diferentes: '$QUANT_ITENS_DIF'."
echo""
echo "As dez primeiras linhas do arquivo são:"
echo "'$DEZ_PRIMEIRAS_LINHAS'"
} > "$SUBDIR_BACKUP/$RELATORIO_TXT"


if [ -f "$SUBDIR_BACKUP/$RELATORIO_TXT" ]; then
	echo "Relatorio '$RELATORIO_TXT' criado"
else
	echo "Relatorio não criado"
fi

#Comprimindo o arquivo backup-dados-<yyyymmdd>.csv para backup-dados-<yyyymmdd>.zip
NOME_ARQ_ZIP="/home/rafaela/ecommerce/vendas/backup/backup-dados-$DATA_EXECUCAO.zip"
NOME_ARQ_CSV="/home/rafaela/ecommerce/vendas/backup/backup-dados-$DATA_EXECUCAO.csv"
zip "$NOME_ARQ_ZIP" "$NOME_ARQ_CSV"
echo "Arquivo '$NOME_ARQ_CSV' comprimido em '$NOME_ARQ_ZIP'."
echo""

#Apagar o arquivo backup-dados-<yyyymmdd>.csv de backup
rm "$NOME_ARQ_CSV"
if [ -f "$NOME_ARQ_CSV" ]; then
	echo "Arquivo '$NOME_ARQ_CSV' não apagado"
else
	echo "Arquivo '$NOME_ARQ_CSV' apagado"
fi
echo""
#Apagar o arquivo dados_de_vendas.csv de vendas
rm "$ARQUIVO_DADOS_VEND"
if [ -f "$ARQUIVO_DADOS_VEND" ]; then
	echo "Arquivo '$ARQUIVO_DADOS_VEND' não apagado"
else
	echo "Aquivo '$ARQUIVO_DADOS_VEND' apagado"
fi
echo""
echo "Fim do script."

