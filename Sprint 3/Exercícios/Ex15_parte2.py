#Exercício 15 - Parte 2
# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, 
# True se a lâmpada estiver ligada, 
# False caso esteja desligada. 
# A classe Lampada possuí os seguintes métodos:
# •	liga(): muda o estado da lâmpada para ligada
# •	desliga(): muda o estado da lâmpada para desligada
# •	esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
# Para testar sua classe:
# 1.	Ligue a Lampada
# 2.	Imprima: A lâmpada está ligada? True
# 3.	Desligue a Lampada
# 4.	Imprima: A lâmpada ainda está ligada? False

class Lampada:
    def __init__(self, ligada=False): #Estado inicial Desligado
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):              #retorna o estado da lampada (T/ligado ou F/desligado)
        return self.ligada

lampada = Lampada()                      # Cria uma lâmpada

lampada.liga()
print("A lâmpada está ligada?", lampada.esta_ligada())  

lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada())