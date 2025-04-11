'''
Loop: while (enquanto)

o while é executado até que uma condição se torne verdade,
POR ISSO precisamos ter CUIDADO com condições que NUNCA
SERÃO VERDADEIRAS!

Sintaxe:

while condicao:
    comandos
'''
'''
valor = 1

#enquanto a variavel valor for  menor ou igual a 5
while valor <= 5: 
    print(valor) #exibe a variavel valor

    #soma 1 na variavel valor e depois guarda na mesma
    valor += 1 

'''

'''
Loop: For (para)

O laço "for" é usado quando já sabemos a quantidade de 
iterações que devem ser feitas, diferente do while que 
depende de uma condição verdadeira.

Sintaxe:
for intervalo:
    comandos
'''
'''
#a função range(n) gera um intervalo de 0 até n-1
#para i (variavel de controle) de 0 a 2
for i in range(3): 
    print(i) #exibe a variavel i
'''

'''
Faça um programa que receba 4 valores e exiba a soma 
dos valores positivos. Utilize o while e o for para 
resolver o mesmo exercício.
'''
#usando o while 
contador = 1
soma = 0

while contador <= 4:
    v = int(input("Digite um valor: "))
    if v > 0:
        soma += v

    contador += 1

print(soma)


