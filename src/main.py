import json
from datetime import datetime

FILE_NAME = "maintenance_data.json"

def carregar_dados():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def salvar_dados(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def criar_om():
    dados = carregar_dados()

    om = input("Número da OM: ")
    descricao = input("Descrição da manutenção: ")

    nova_om = {
        "om": om,
        "descricao": descricao,
        "status": "aberta",
        "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    dados.append(nova_om)
    salvar_dados(dados)

    print("OM criada com sucesso!")

def listar_oms():
    dados = carregar_dados()

    if not dados:
        print("Nenhuma OM cadastrada.")
        return

    for om in dados:
        print("------------------------")
        print("OM:", om["om"])
        print("Descrição:", om["descricao"])
        print("Status:", om["status"])
        print("Data:", om["data_criacao"])

def menu():
    while True:
        print("\n==== Sistema de Manutenção ====")
        print("1 - Criar OM")
        print("2 - Listar OMs")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_om()

        elif opcao == "2":
            listar_oms()

        elif opcao == "3":
            break

        else:
            print("Opção inválida")

menu()
