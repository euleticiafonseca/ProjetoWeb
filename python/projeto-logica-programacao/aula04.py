
'''
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
'''
'''
idade = 70

if idade <= 16: 
    print("Criança")
elif idade <= 29:
    print("Jovem")
elif idade <= 65:
    print("Adulto")
else:
    print("Idoso")
'''
'''
print("Amarelo - Verde - Vermelho")
cor = input("Escolha uma cor: ")

if cor.lower() == 'amarelo': 
    print("Atenção")
elif cor.lower() == 'verde':
    print("Siga")
elif cor.lower() == 'vermelho':
    print("Pare")
else:
    print("Cor inválida")
'''    

'''
Escreva um programa que pergunte ao usuário se ele deseja
calcular a área de um triângulo, círculo, quadrado ou 
retângulo. E com base nessa informação, exiba o resultado

Triangulo -> (b*h)/2
Retangulo -> b*h
Quadrado -> l**2
Circulo --> 3.14*(r**2)
'''

fig = input("Qual a figura a ser calculada? ")
resultado = 0

if fig == 'quadrado':
    l = float(input("Digite o lado: "))
    resultado = l**2
elif fig == 'retangulo':
    b = float(input("Digite a base: "))
    h = float(input("Digite a altura: "))
    resultado = (b*h)
elif fig == "triangulo":
    b = float(input("Digite a base: "))
    h = float(input("Digite a altura: "))
    resultado = (b*h)/2
elif fig == "circulo":
    r = float("Digite o raio: ")
    resultado = 3.14*(r**2)
else:
    resultado = "resposta inválida"
print(resultado)





