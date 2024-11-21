#Exercício 21 - Parte 1
# Implemente duas classes, Pato e Pardal , que herdam de uma superclasse 
# chamada Passaro as habilidades de voar e emitir som.
# Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.
# Imprima no console exatamente assim:
# 1.	Pato
# 2.	Voando...
# 3.	Pato emitindo som...
# 4.	Quack Quack
# 5.	Pardal
# 6.	Voando...
# 7.	Pardal emitindo som...
# 8.	Piu Piu

class Passaro:  #superclasse passaro
    def __init__(self, nome):
        self.nome = nome
    
    def voar(self): #metodo voar
        print("Voando...")
    
class Pato(Passaro): #classe pato
    def __init__(self):
        self.nome = "Pato"

    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro): #classe pardal
    def __init__(self):
        self.nome = "Pardal"

    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")


pato = Pato()
print(pato.nome)
pato.voar()
pato.emitir_som()

pardal = Pardal()
print(pardal.nome)
pardal.voar()
pardal.emitir_som()  