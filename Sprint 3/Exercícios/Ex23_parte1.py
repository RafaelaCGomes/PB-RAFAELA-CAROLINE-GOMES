#Exercício 23 -  Parte 1
#Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
# Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, 
#e retorne a subtração dos dois (resultados negativos são permitidos).	
#Utilize os valores abaixo para testar seu exercício:
#1.	x = 4 
#2.	y = 5
#imprima:
#1.	Somando: 4+5 = 9
#2.	Subtraindo: 4-5 = -1

class Calculo:
    def soma(self, x, y):
        print(f"Soamndo: {x} + {y} = {x + y}")
        return x + y
    
    def subtracao(self, x, y):
        print(f"Subtraindo: {x} - {y} = {x - y}")
        return x - y
    
 
calculo = Calculo()
calculo.soma(4, 5)
calculo.subtracao(4, 5)
