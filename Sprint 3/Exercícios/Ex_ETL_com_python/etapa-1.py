#Etapa01 - Apresente o ator/atriz com maior numero de filmes e a respectiva quantidade.
#A quantidade de filmes encontra-se na coluna Number of movies do arquivo.


arquivo_csv = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/actors.csv'
arquivo_txt = 'C:/Users/User/Desktop/Compass.uol/Sprint03/Exercicios/ETL/etapa-1.txt'

ator_com_maior_n_de_filmes = ""
maior_n_de_filmes = 0

with open(arquivo_csv, mode='r') as arquivo_csv:
    linhas = arquivo_csv.readlines()

    
    for linha in linhas[1:]:
        colunas = linha.strip().split(',') #separa linhas em colunas
        
        ator = colunas[0] #ator coluna1 - indice 0
        n_de_filmes = float(colunas[2]) #numero de filmes coluna 2

        if n_de_filmes > maior_n_de_filmes:
            maior_n_de_filmes = n_de_filmes
            ator_com_maior_n_de_filmes = ator

resultado = f'O ator/atriz com maior numero de filmes: {ator_com_maior_n_de_filmes} com {maior_n_de_filmes} filmes.'

with open(arquivo_txt, mode='w') as arquivo_txt: 
    arquivo_txt.write(resultado) 

print(resultado)