# Resumo e Objetivo
O desafio da Sprint 01 teve como objetivo criar um script executável em linux que criasse um relatório final, unindo relatórios que foram gerados por outro script executável, esse por sua vez, foi programado e rodou por quatro dias seguidos, gerando relatórios diários.

Foi fornecido um arquivo dados_de_vendas.csv, de onde foi extraido os dados para a produção do primeiro relatório, para os demais relatórios, foi alterado manualmente os dados do arquivo dados_de_vendas.csv, gerando assim, diariamente relatórios com informações diferentes.

# Etapas da criação dos scripts executáveis
Em ambos os executáveis, fui escrevendo e testando cada parte isolada, com o intuito de ir corrigindo os erros de sintax e pontuações durante o processo de escrita.

##Script01 [Etapa I](etapa-1)

1. Ao criar o arquivo Processamento_de_vendas.sh, não estava conseguindo editá-lo, ao mudar as configurações de permissão o probelma foi resolvido. 

![Problemas de permissão](/Sprint%201/Evidencias/Problema_permissao.png)
2. Comecei a criação do executável criando um cabeçalho onde há informações importantes como nome do autor, breve descrição da função do script e como ele será executado.

![Cabeçalho](./Evidencias/Cabeçalho.png)

3. Após isso, dei inícios aos comandos de criação de diretório, subdiretório e realização da cópia do arquivo dados_de_vendas.csv para dentro do diretório, sendo utilizado o código:
```linux
    DIRETORIO_VENDAS="/home/rafaela/ecommerce/vendas"
    if [ -d "$DIRETORIO_VENDAS" ]; then
        echo "O diretório vendas já existe"
    else
        mkdir "$DIRETORIO_VENDAS"
        echo "Diretório vendas criado"
    fi

    if [ -d "$SUBDIR_BACKUP" ]; then
        echo "O subdiretório backup já existe"
    else
        mkdir "$SUBDIR_BACKUP"
        echo "Subdiretório backup criado"
    fi

    ARQUIVOS_DADOS="/home/rafaela/ecommerce/dados_de_vendas.csv"
    cp "$ARQUIVOS_DADOS" "vendas"
    echo "Arquivo dados_de_vendas copiado para o diretório vendas"
```
Tendo como saída
![Criação vendas, backup e cópia de dados_de_vendas](./Evidencias/Criação_dir_subdir_copia.png)

4. Logo após, é realizado a renomeação do arquivo para o formato dados-yyyymmdd. Para isso foi necessário obter a data de execução para adicioná-a ao título a travvéz do comando date.

```linux
    DATA_EXECUCAO=$(date +"%y%m%d")
```
    
![Renome para dados-yyyymmdd](./Evidencias/Renome_dados-yyymmdd.png)

5. É realizado uma nova renomeação para o formato backup-dados-yyyymmdd, sendo que a função mv foi usada para isso.
```linux
     BACKUP_DADOS="backup-dados-$DATA_EXECUCAO.csv"
    if [ -f "$SUBDIR_BACKUP/$NOVO_ARQUIVO_BACKUP" ]; then
            mv "$SUBDIR_BACKUP/$NOVO_ARQUIVO_BACKUP" "$SUBDIR_BACKUP/$BACKUP_DADOS"
            echo "Arquivo '$NOVO_ARQUIVO_BACKUP' renomeado para '$BACKUP_DADOS' dentro do diretório '$SUBDIR_BACKUP'."
    else
            echo "Arquivo '$NOVO_ARQUIVO_BACKUP' não encontrado."
    fi 
```

    
##Script02 [Etapa II](etapa-2)

2. ... 

Já com esse código, o objetivo é ...

```
Esta é uma outra linha de código
```
    



