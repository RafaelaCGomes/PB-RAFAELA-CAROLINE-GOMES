#Etapa02- Apresente a média de receita de bilheteria
#bruta dos principais filmes, considerando todos os autores.
#Estamos falando da média da coluna Gross.

arquivo_csv = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/actors.csv'
arquivo_txt = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/etapa-2.txt'

def ler_arquivo_csv(arquivo_csv): # Função para ler o arquivo csv
    with open(arquivo_csv, mode='r') as arquivo_csv:
        next(arquivo_csv)   #pula a primeira linha
        
        linhas = arquivo_csv.readlines() # Lê todas as linhas do arquivo 
    return linhas

def cal_media_gross(linhas): # Função para calcular a média do valor bruto
    total_gross = 0
    numero_de_atores = 0
    
    for l in linhas:
        colunas = l.strip().split(',')
        try:
            gross = float(colunas[5].strip())
        except ValueError: 
            continue

        total_gross += gross        # Adicione o valor de "Gross" ao total  
        numero_de_atores  += 1      #soma o número de atores

    media_gross = total_gross / numero_de_atores # Calcule a média 
    return media_gross

def escrever_resultado(arquivo_txt, media_gross): # Função para escrever o resultado no arquivo txt
    with open(arquivo_txt, mode='w') as arquivo_txt:
        arquivo_txt.write(f'A media de receita de bilheteria bruta dos principais filmes, considerando todos os autores e: {media_gross:.2f}')

linhas = ler_arquivo_csv(arquivo_csv)
media_gross = cal_media_gross(linhas)
escrever_resultado(arquivo_txt, media_gross)


print(f'A media de receita de bilheteria bruta dos principais filmes, considerando todos os autores e: {media_gross:.2f}')
