#Exercício 11 - Parte 2 
# Leia o arquivo person.json, faça o parsing e 
# imprima seu conteúdo.
# Dica: leia a documentação do pacote json

import json
with open('person.json', 'r') as arquivo:
    leitura = json.load(arquivo)

print(leitura)