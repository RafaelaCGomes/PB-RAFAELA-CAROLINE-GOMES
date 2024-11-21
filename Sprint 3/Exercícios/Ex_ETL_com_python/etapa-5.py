#Etapa05 -  Apresente a lista dos atores ordenada 
#pela receita bruta de bilheteria de seus filmes
#(Coluna Total Gross), em ordem decrescente.
# Ao escrever no arquivo, considere o padrão de saída
# (nome do ator) - (receita total bruta), adicionando
# um resultado em cada linha. 

arquivo_csv = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/actors.csv'
arquivo_txt = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/etapa-5.txt'

def ler_arquivo_csv(arquivo_csv): # Função para ler o arquivo csv
    with open(arquivo_csv, mode='r') as arquivo_csv:
        next(arquivo_csv)   #pula a primeira linha
        
        linhas = arquivo_csv.readlines() # Lê todas as linhas do arquivo 
    return linhas

def extrair_t_gross(linhas):
    total_gross = [] 
    
    for l in linhas: 
        colunas = l.strip().split(',')
        
        ator = colunas[0] 
        try: 
            gross = float(colunas[1].strip()) 
            total_gross.append((ator, gross)) 
        except ValueError: 
            continue
    return total_gross


def ordenar_t_gross(total_gross):
    total_gross_ordenado = sorted(total_gross, key=lambda x: -x[1])
    return total_gross_ordenado


def escrever_resultado(arquivo_txt, total_gross_ordenado):
    with open(arquivo_txt, mode='w') as arquivo:
        for ator, gross in total_gross_ordenado:
            arquivo.write(f'{ator} - {gross:.2f}\n')

linhas = ler_arquivo_csv(arquivo_csv)
total_gross = extrair_t_gross(linhas)
total_gross_ordenado = ordenar_t_gross(total_gross)
escrever_resultado(arquivo_txt, total_gross_ordenado)

for ator, gross in total_gross_ordenado:
    print(f'{ator} - {gross:.2f}')
