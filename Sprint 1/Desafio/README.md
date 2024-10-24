# Resumo e Objetivo
O desafio da Sprint 01 teve como objetivo criar um script executável em linux que criasse um relatório final, unindo relatórios que foram gerados por outro script executável, esse por sua vez, foi programado e rodou por quatro dias seguidos, gerando relatórios diários.

Foi fornecido um arquivo dados_de_vendas.csv, de onde foi extraido os dados para a produção do primeiro relatório, para os demais relatórios, foi alterado manualmente os dados do arquivo dados_de_vendas.csv, gerando assim, diariamente relatórios com informações diferentes.

# Etapas da criação dos scripts executáveis
Em ambos os executáveis, fui escrevendo e testando cada parte isolada, com o intuito de ir corrigindo os erros de sintax e pontuações durante o processo de escrita.

**Script01.** ... [Etapa I](etapa-1)

    Ao criar o arquivo Processamento_de_vendas.sh, não estava conseguindo editá-lo, ao mudar as configurações de permissão o probelma foi resolvido. 

    ![Problema de permissão](../Evidencias/sample.webp)

    Comecei a criação do executável criando um cabeçalho onde há informações importantes como nome do autor, breve descrição da função do script e como ele será executado.

     ![Cabeçalho](../Evidencias/sample.webp)

    Após isso, dei inícios aos comandos de criação de diretório, subdiretório e realização da cópia do arquivo dados_de_vendas.csv para dentro do diretório, sendo utilizado o código:
    ...
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
    ...
    Tendo como saída
    ![Criação vendas, backup e cópia de dados_de_vendas]()

    


2. ... [Etapa II](etapa-2)

    Já com esse código, o objetivo é ...

    ```
    Esta é uma outra linha de código
    ```
    



