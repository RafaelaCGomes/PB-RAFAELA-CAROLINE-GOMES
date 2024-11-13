#Exercício de programação 1- Parte 1
#Desenvolva um código em Python que crie variáveis para 
#armazenar o nome e a idade de uma pessoa, juntamente com seus valores correspondentes. 
#Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

nome = "Rafaela"
idade = 24

import datetime
ano_atual = datetime.datetime.now().year

cem_anos = ano_atual + (100-idade)

print(cem_anos)