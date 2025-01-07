def cadastrar_aluno(lista_alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matricula do aluno: ")
    dt_nasc = input("Digite a data de nascimento do aluno: ")
    sexo = input("Digite o sexo do aluno: ")
    endereco = input("Digite o endereço do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    email = input("Digite o email do aluno:")

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "dt_nasc": dt_nasc,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,

    }
    lista_alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def cadastrar_prof(lista_prof):
    nome = input("Digite o nome do professor: ")
    matricula = input("Digite a matricula do professor: ")
    dt_nasc = input("Digite a data de nascimento do professor: ")
    sexo = input("Digite o sexo do professor: ")
    endereco = input("Digite o endereço do professor: ")
    telefone = input("Digite o telefone do professor: ")
    email = input("Digite o email do professor:")
    disciplina = input("Digite a disciplina do professor :")


    professor = {
        "nome": nome,
        "matricula": matricula,
        "dt_nasc": dt_nasc,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplina": disciplina,

    }



def listar_alunos(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nLista de alunos cadastrados:")
    for idx, aluno in enumerate(lista_alunos, start=1):
        print(f"Nome: {aluno['nome']}, Matricula: {aluno['matricula']}, Data de nascimento: {aluno['dt_nasc']}, Sexo: {aluno['sexo']}, Endereço: {aluno['endereco']}, Telefone: {aluno['telefone']}, E-mail: {aluno['email']}")

def menu():
    alunos = []
    while True:
        print("\nMenu:")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()