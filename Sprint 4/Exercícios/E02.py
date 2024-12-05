"""E02 - Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
É obrigatório aplicar as seguintes funções:
•	len
•	filter
•	lambda
Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código."""

#função para contar as vogais.
def conta_vogais(texto:str)-> int:
   vogais = ("aeiou")
   filtrar = filter(lambda x: x in vogais, texto.lower())
   contar_vog = len(list(filtrar))
   return contar_vog

print(conta_vogais("Aqui está uma frase com vogais")) 