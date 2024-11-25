from entrada import *

def cadastrar_aluno(id):
    """
    Lê os dados de um aluno e retorna um dicionário com as informações.

    Parâmetros:
      - id: ID único para o aluno.

    Retorno:
      - Dicionário com os dados do aluno.
    """
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome do aluno: ")
    idade = ler_inteiro("Idade do aluno: ", pos=True)
    peso = ler_real("Peso (kg): ", pos=True)
    altura = ler_real("Altura (m): ", pos=True)
    # Calcula o IMC com base no peso e altura
    imc = peso / (altura ** 2)
    return {
        "id": id,
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2)  # Arredondar para 2 casas decimais
    }

def imprimir_alunos(alunos):
    """
    Imprime todos os alunos cadastrados.

    Parâmetros:
      - alunos: Lista de dicionários contendo os dados dos alunos.
    """
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | Idade: {aluno['idade']} | "
                  f"Peso: {aluno['peso']}kg | Altura: {aluno['altura']}m | IMC: {aluno['imc']}")

def buscar_aluno_por_id(alunos, id_busca):
    """
    Busca um aluno pelo ID.

    Parâmetros:
      - alunos: Lista de dicionários contendo os dados dos alunos.
      - id_busca: ID do aluno a ser buscado.

    Retorno:
      - Dicionário com os dados do aluno encontrado ou None se não encontrado.
    """
    for aluno in alunos:
        if aluno["id"] == id_busca:
            return aluno
    return None

def imprimir_dados_aluno(aluno):
    """
    Imprime os dados detalhados de um aluno.

    Parâmetros:
      - aluno: Dicionário contendo os dados do aluno.
    """
    print(f"\n--- Dados do Aluno ---")
    print(f"ID: {aluno['id']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']} anos")
    print(f"Peso: {aluno['peso']} kg")
    print(f"Altura: {aluno['altura']} m")
    print(f"IMC: {aluno['imc']}")
