#Exercício 14 - Parte 2
# Escreva uma função que recebe um número variável de parâmetros não 
# nomeados e um número variado de parâmetros nomeados e imprime o valor de 
# cada parâmetro recebido.
# Teste sua função com os seguintes parâmetros:
# (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)


def imprime_parametros(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(valor)

imprime_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

