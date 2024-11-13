#Exercício 08 - Parte 2
# Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.
# Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.
# É necessário que você imprima no console exatamente assim:
# 1.	A palavra: maça não é um palíndromo	 
# 2.	A palavra: arara é um palíndromo	 
# 3.	A palavra: audio não é um palíndromo
# 4.	A palavra: radio não é um palíndromo
# 5.	A palavra: radar é um palíndromo	 
# 6.	A palavra: moto não é um palíndromo

lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']


def palavra_palindromo (p):
    return p == p [::-1]

for palavra in lista:
    if palavra_palindromo( palavra):
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")
        



