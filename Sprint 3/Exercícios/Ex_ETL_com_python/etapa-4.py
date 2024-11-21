#Etapa04 - A coluna #1 Movie contém o filme de maior
# bilheteria em que o ator atuou. Realize
# a contagem de aparições destes filmes no dataset,
# listando-os ordenados pela quantidade de vezes
# que estão presentes. Considere a ordem decrescente,
# em segundo nível, o nome do filme.


arquivo_csv = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/actors.csv'
arquivo_txt = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/etapa-4.txt'

def ler_arquivo_csv(arquivo_csv): # Função para ler o arquivo csv
    with open(arquivo_csv, mode='r') as arquivo_csv:
        next(arquivo_csv)   #pula a primeira linha
        
        linhas = arquivo_csv.readlines() # Lê todas as linhas do arquivo 
    return linhas

def contar_filmes(linhas): # Função para contar filmes
    contagem_filmes = {}
    
    for linha in linhas:    # Separa a linha em colunas
        colunas = linha.strip().split(',')
        
        filme = colunas[4]
        
        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            contagem_filmes[filme] = 1
    
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda item: (-item[1], item[0])) # Ordena os filmes
    return filmes_ordenados

def escrever_resultado(arquivo_txt, filmes_ordenados ): # Função para escrever o resultado no arquivo txt
    with open(arquivo_txt, mode='w') as arquivo_txt:
       arquivo_txt.write('Quantidade de vezes que esta presente , Nome do filme\n')
       for filme, quantidade in filmes_ordenados:
           arquivo_txt.write(f' {quantidade} , {filme}\n')
           
linhas = ler_arquivo_csv(arquivo_csv) 
filmes_ordenados = contar_filmes(linhas)
escrever_resultado(arquivo_txt, filmes_ordenados)

print('Quantidade de vezes que esta presente , Nome do filme')
for filme, quantidade in filmes_ordenados:
    print(f' {quantidade} , {filme}')
