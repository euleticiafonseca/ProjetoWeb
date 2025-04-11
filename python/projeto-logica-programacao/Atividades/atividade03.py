'''
Imagine que você está desenvolvendo um sistema para uma
agência de viagens e precisa organizar as informações
sobre os clientes e suas respectivas viagens. Para cada
cliente você deve armazenar: 
    -uma lista com o nome dos clientes
    -para cada cliente um dicionário que associa o 
    destino da viagem como chave e uma tupla com a data
    de partida e retorno
    -o sistema deve permitir a consulta de todas as 
    viagens por nome de cliente e destino.
'''
##1º Criar lista com o nome dos clientes
clientes = ["Maria", "Antonia", "Edna", "Eder"]

##2º Armazenar as viagens dos clientes
viagens = {
    "Maria" : {
        "Paris": ("2023-05-10", "2023-05-20"),
        "Nova York": ("2024-02-15", "2024-02-27")
    },
    "Antonia": {
        "Rio de Janeiro": ("2024-12-12", "2024-12-25")
    },
    "Eder": {
        "Curitiba": ("2025-05-12", "2025-05-25"),
        "Brasilía": ("2025-01-01", "2025-02-02")
    }
}

nome_buscado = input("Nome do Cliente: ")
while nome_buscado != '0':
    ##Exibindo as viagens: 
    print(f"Viagens {nome_buscado}: ")
    if nome_buscado in viagens: 
        for destino in viagens[nome_buscado]:
            print('Destino: ', destino)
            print('Ida: ', viagens[nome_buscado][destino][0])
            print('Volta: ',viagens[nome_buscado][destino][1])
            print('-'*40)
    else :
        print("Ops! Cliente não localizado.")
        print("Tente: ", list(viagens.keys()))
    nome_buscado = input("Nome do Cliente: ")


