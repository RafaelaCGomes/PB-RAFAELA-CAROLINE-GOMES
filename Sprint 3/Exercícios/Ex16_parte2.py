#Exercício 16 - Parte 2
# Escreva uma função que recebe uma string de números separados por vírgula e
# retorne a soma de todos eles. 
# Depois imprima a soma dos valores.
# A string deve ter valor  "1,3,4,6,10,76"


def som(string):
    lista = string.split(",")
    soma = 0
    for n in lista:
        soma += int(n)
    return soma
    
print(som("1,3,4,6,10,76"))
