#Exercício 17 - Parte 2
# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
# a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""  1,2,3,4
     5,6,7,8
     9,10,11,12
"""

def dividir_lista(lista):
    tamanho_total_lista = len(lista)
    tamanho_parte = tamanho_total_lista // 3  

    parte1 = lista[:tamanho_parte]  #divide a lista em 3 partes.
    parte2 = lista[tamanho_parte:2*tamanho_parte]
    parte3 = lista[2*tamanho_parte:]

    return parte1, parte2, parte3


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_lista(lista)
print(parte1, parte2, parte3)