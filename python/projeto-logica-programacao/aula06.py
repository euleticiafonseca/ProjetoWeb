'''
Listas: são estruturas para armazenar diferentes valores 
em um unico lugar
'''
'''
nomes = ["Ana", "Marcelo", "Edna", "João"]
idades = [20, 18, 30, 25]

print(nomes) #mostra a lista de nomes completa
print(idades) #mostra a lista de idades completa

print(nomes[0]) #mostra somente o primeiro nome da lista
print(idades[-1])#mostra a ultima idade da lista

print("Lista nomes: ", nomes)
nomes[2] = "Antonia"
print("nomes[2] = Antonia", nomes)
'''

'''
Tuplas: são estruturas de dados que armazenam diversos 
valores, porem seus valores são imutáveis
'''
cpfs = ('444.444.444-44', '111.111.111-11', '123.123.123-12')

print('Tupla cpfs: ', cpfs)
print("1º CPF: ", cpfs[0])

'''
Dicionarios: são estruturas de dados que armazenam valores baseados no conceito
de chave e valor 
'''
notas = {
    "Maria" : 7.5, 
    "João" : 5.6
}

print("nota de Maria: ", notas["Maria"])
print("Notas: ", notas)







