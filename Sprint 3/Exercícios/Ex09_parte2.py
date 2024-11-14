#Exercício 09 - Parte 2
# Dada as listas a seguir:
# primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
# sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
# idades = [19, 28, 25, 31]
# Faça um programa que imprima o dados na seguinte estrutura:
# "índice - primeiroNome sobreNome está com idade anos".
# Exemplo:
# 0 - João Soares está com 19 anos
#Você deve Utilizar a função enumerate().

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, nome in enumerate(primeirosNomes):
    sobrenome = sobreNomes[i]
    idade = idades [i]

    print(f"{i} - {nome} {sobrenome} está com {idade} anos")
