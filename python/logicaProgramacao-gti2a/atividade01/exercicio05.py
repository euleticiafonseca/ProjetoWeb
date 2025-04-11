'''
Exercício 05 :
Leia o saldo da conta e o valor do produto que o
usuário deseja comprar. Mostre se ele pode realizar
a compra com o saldo disponível
'''

saldo = float(input("Qual o saldo da conta? "))
valorProduto = float(input("Qual o valor do produto? "))

print("Pode comprar? ", saldo >= valorProduto)

