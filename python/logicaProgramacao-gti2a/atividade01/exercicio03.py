'''
Exercício 03 :
Pergunte a idade do usuário e informe o ano em que ele nasceu.
'''
#variavel idade guardando o valor digitado no input
idade = int(input("Digite a sua idade: "))
anoAtual = int(input("Digite o ano atual: "))

ano = anoAtual - idade

print("Você nasceu em ", ano)

