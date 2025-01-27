import random

#Criar lista contendo 250 numero inteiros de forma aleatória.
lista_aleatoria = [random.randint(0, 500) for i in range(250)]

#Método reverse
lista_aleatoria.reverse()

#Imprimir lista
print(lista_aleatoria)