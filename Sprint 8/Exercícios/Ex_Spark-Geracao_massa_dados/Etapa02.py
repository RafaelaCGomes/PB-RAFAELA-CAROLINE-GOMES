import csv

#lista animais
animais = ['cachorro', 'gato', 'calopsita', 'cavalo', 'elefante',
           'rinoceronte', 'leão', 'pato', 'rato', 'camaleão',
           'porco', 'vaca', 'peixe', 'cobra', 'tartaruga', 
           'cabrito', 'girafa', 'tigre', 'jacaré', 'zebra']

#lista em ordem alfabetica
animais.sort()

#printa cada item linha por linha
[print(animal)for animal in animais]

#grava em arquivo csv linha por linha
with open('animais_ordenados.csv', 'w' ) as arquivocsv:
    for animal in animais:
       arquivocsv.write(animal + '\n')
