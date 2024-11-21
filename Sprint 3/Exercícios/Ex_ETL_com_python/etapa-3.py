#Etapa03 - Apresente o ator/atriz com a maior média
#de receita de blheteria bruta por filme do conjunto
#dados. Considere a coluna Average per Movie para 
# fins de alculo.

arquivo_csv = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/actors.csv'
arquivo_txt = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/etapa-3.txt'

def ler_arquivo_csv(arquivo_csv): # Função para ler o arquivo csv
    with open(arquivo_csv, mode='r') as arquivo_csv:
        next(arquivo_csv)   #pula a primeira linha
        
        linhas = arquivo_csv.readlines() # Lê todas as linhas do arquivo 
    return linhas

def cal_maior_media(linhas): # Função para calcular a maior média
    maior_media = 0
    ator_com_maior_media = ""
    
    for l in linhas:# Separa a linha em colunas
        colunas = l.strip().split(',')
    
        ator = colunas[0]
        try:
            media_filme = float(colunas[3].strip()) 
        except ValueError:
            continue  

        if media_filme > maior_media: # Verifica se a média é maior que a maior média encontrada
            maior_media = media_filme
            ator_com_maior_media = ator
    return ator_com_maior_media, maior_media


def escrever_resultado(arquivo_txt, ator, media ): # Função para escrever o resultado no arquivo txt
    with open(arquivo_txt, mode='w') as arquivo_txt:
        arquivo_txt.write(f'O ator/atriz com a maior media de receita de blheteria bruta por filme e:{ator} com media: {media:.2f}')

linhas = ler_arquivo_csv(arquivo_csv)
ator, media = cal_maior_media(linhas)
escrever_resultado(arquivo_txt, ator, media)


print(f'O ator/atriz com a maior media de receita de blheteria bruta por filme e: {ator} com media: {media:.2f}')
