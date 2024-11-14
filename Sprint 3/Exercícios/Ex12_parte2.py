#Exercício 12 - Parte 2
# Implemente a função my_map(list, f) que recebe uma lista como primeiro 
# argumento e uma função como segundo argumento. Esta função aplica a função 
# recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
# Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que 
# potência de 2 para cada elemento.

lista_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_map(list, f):
    lista_resultado = []
    for elemento in list:
        lista_resultado.append(f(elemento))
    return lista_resultado

def potencia_2(x):
    return x ** 2

resultado = my_map(lista_entrada, potencia_2)
print(resultado)