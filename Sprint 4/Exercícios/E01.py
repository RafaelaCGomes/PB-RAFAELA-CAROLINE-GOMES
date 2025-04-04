"""E01
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício: map, filter, sorted, sum

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores."""


with open ('number_txt', mode='r') as number_txt: #abre o arquivo
    numeros = map(int ,number_txt.readlines())

filtro_pares = filter(lambda x: x %2 ==0, numeros) 
num_ordenados = sorted(filtro_pares, reverse=True)
maiores_cinco = num_ordenados[:5]
soma = sum(maiores_cinco)

print(maiores_cinco)
print(soma)

