'''E05
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, 
no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.
Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual 
contendo as seguintes informações:
•	Nome do estudante
•	Três maiores notas, em ordem decrescente
•	Média das três maiores notas, com duas casas decimais de precisão
O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do 
estudante e obedecendo ao formato descrito a seguir:

Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

Exemplo:
Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
•	round
•	map
•	sorted'''

#função para gerar o relatorio com os dados formatados.
def gerador_relatorio(nomearquivo):
    with open(nomearquivo, mode='r') as arquivo: #abrir o arquivo.
        linhas = arquivo.readlines()
        
    informacao = list(map(lambda linha: linha.strip().split(','), linhas)) #transformar em lista as info. usando a virgula como delimitadora

    #função para processar os dados dos estudantes.
    def processar_estudante(informacao):
        nome = informacao [0]
        notas = list(map(int, informacao[1:]))
        maiores_notas = sorted(notas, reverse=True)[:3] #maiores 3 notas.
        media = round(sum(maiores_notas) /3, 2) #soma as maiores notas e divide por 3, result. com 2 casas decimais.
        return (nome, maiores_notas, media)

 
    estudantes_processados = list(map(processar_estudante, informacao)) #gera lista das informações processadas.

    estudantes_ordenados = sorted(estudantes_processados, key=lambda x: x[0]) #ordena a lista de acordo com o nome.

    #função para formatar a saída das informações, principalmente a média.
    def formatar_saida(informacao):
        nome, maiores_notas, media = informacao
        media_formatada = f'{media:.2f}' if media % 1 != 0 else f'{media:.1f}' #formata as casas decimais da média.
        return f'Nome: {nome} Notas: {maiores_notas} Média: {media_formatada}' 
    
    resultado = map(formatar_saida, estudantes_ordenados)

    print("\n".join(resultado))


gerador_relatorio('estudantes.csv')