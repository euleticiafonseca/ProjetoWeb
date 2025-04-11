'''
Operadores Logicos:

AND(E) :
    Retorna um True quando todas as condições são verdade
OR(OU) :
    Retorna um True se pelo menos uma condição é verdade
NOT(Nao) :
    Inverte o valor booleano (True/False)

'''

media = float(input("Qual a sua média? "))
freq = float(input("Qual a sua frequencia? "))

print("Atingiu a media: ", media >= 6)
print("Atingiu a frequencia: ", freq >= 75)

aprovacao = (media >= 6) and (freq >= 75)
print("Passou na materia: ", aprovacao)




