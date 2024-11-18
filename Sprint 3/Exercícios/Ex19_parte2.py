#Exercício 19 - Parte 2
# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
# 1.	import random 
# 2.	# amostra aleatoriamente 50 números do intervalo 0...500
# 3.	random_list = random.sample(range(500),50)
# Use as variáveis abaixo para representar cada operação matemática:
# 1.	mediana
# 2.	media
# 3.	valor_minimo 
# 4.	valor_maximo 
# Importante: Esperamos que você utilize as funções abaixo em seu código:
#•	random
#•	max
#•	min
#•	sum

import random 
import math

#amostra aleatoriamente 50 números do intervalo 0...500

random_list = random.sample(range(500),50)
def calc_mediana(lista):
    l_ordenada = sorted(lista)
    meio = len(l_ordenada) // 2
    if len(l_ordenada) % 2 == 1:
        return l_ordenada[meio]
    else:
        return ((l_ordenada[meio - 1] + l_ordenada[meio]) / 2)

mediana = calc_mediana(random_list)
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
