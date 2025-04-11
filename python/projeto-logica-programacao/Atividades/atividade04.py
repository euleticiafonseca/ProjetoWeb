'''
1. Crie uma função que receba o nome e sobrenome 
   de uma pessoa.
2. Crie uma função que exiba o nome completo e a 
   quantidade de caracteres desse nome.
'''

def recebeNome():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")

    return nome + ' ' + sobrenome

def exibeInfos(): 
    nomeCompleto = recebeNome()
    print("Nome completo: ", nomeCompleto)
    print("Tamanho: ", len(nomeCompleto)-1)

exibeInfos()





