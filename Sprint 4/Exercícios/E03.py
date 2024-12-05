""" E03 - A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.
1.	lancamentos = [
2.	    (200,'D'),
3.	    (300,'C'),
4.	    (100,'C')
5.	]
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. 
Na lista anterior, por exemplo, teríamos como resultado final 200.
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
reduce (módulo functools), map    """

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    val_ajustado = map(lambda x : x[0] if x[1] == 'C' else -x[0], lancamentos) #verifiica se o indice 1 corresponde a 'c', para que x[0] ficar positivo.
    valor_final = reduce(lambda acum,y : acum+y, val_ajustado) #reduce = reduz a um unico numero, acumulando os dados dos indices.
    return valor_final

print(calcula_saldo(lancamentos=[(200,'D'),(300,'C'),(100,'C')]))
