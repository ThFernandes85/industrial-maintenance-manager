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


### Future Improvements
- Add SQLite database
- Build REST API with FastAPI
- Create dashboard with Streamlit

---

## 🇧🇷 Visão Geral

Industrial Maintenance Manager é um sistema simples para registrar e acompanhar Ordens de Manutenção (OMs).

Este projeto simula como atividades de manutenção industrial podem ser gerenciadas digitalmente.

### Funcionalidades
- Criar ordens de manutenção
- Listar ordens cadastradas
- Registrar status e data de criação

### Tecnologias
- Python
- Armazenamento em JSON
- Interface via terminal

### Estrutura do projeto


### Melhorias futuras
- Adicionar banco SQLite
- Criar API com FastAPI
- Criar dashboard com Streamlit
