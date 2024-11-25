import json
from aluno import *
from entrada import *
from navegabilidade import *

# Variáveis de controle dos dados na memória
id = 1
alunos = []

# Função para salvar os dados em um arquivo
def salvar_dados(alunos, arquivo="alunos.json"):
    with open(arquivo, "w") as f:
        json.dump(alunos, f)
    print("Dados salvos com sucesso!")

# Função para carregar os dados de um arquivo
def carregar_dados(arquivo="alunos.json"):
    global id
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
            if dados:
                ultimo_id = max([aluno["id"] for aluno in dados])
                id = ultimo_id + 1  # Ajustar o próximo ID
            return dados
    except FileNotFoundError:
        return []  # Se o arquivo não existe, retorna uma lista vazia

# Carregar os dados ao iniciar o programa
alunos = carregar_dados()

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")

    # Navegabilidade
    if opc == 1:
        # Cadastrar aluno
        aluno = cadastrar_aluno(id)
        alunos.append(aluno)
        id += 1
    elif opc == 2:
        # Imprimir todos os cadastros
        imprimir_alunos(alunos)
    elif opc == 3:
        # Buscar aluno por ID
        id_busca = ler_inteiro("Digite o ID do aluno: ", pos=True)
        aluno = buscar_aluno_por_id(alunos, id_busca)
        if aluno:
            print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | IMC: {aluno['imc']}")
        else:
            print("Aluno não encontrado.")
    elif opc == 4:
        # Filtrar alunos por IMC
        imc_min = ler_real("IMC mínimo: ", pos=True)
        imc_max = ler_real("IMC máximo: ", pos=True)
        filtrados = filtrar_alunos_por_imc(alunos, imc_min, imc_max)
        imprimir_alunos(filtrados)
    elif opc == 5:
        # Salvar e sair
        salvar_dados(alunos)
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

    limpar_tela()
