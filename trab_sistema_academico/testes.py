def cadastrar_aluno(lista_alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matricula do aluno: ")
    dt_nasc = input("Digite a data de nascimento do aluno: ")
    sexo = input("Digite o sexo do aluno: ")
    endereco = input("Digite o endereço do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    email = input("Digite o email do aluno: ")

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

def cadastrar_professor(lista_professores):
    nome = input("Digite o nome do professor: ")
    matricula = input("Digite a matricula do professor: ")
    dt_nasc = input("Digite a data de nascimento do professor: ")
    sexo = input("Digite o sexo do professor: ")
    endereco = input("Digite o endereço do professor: ")
    telefone = input("Digite o telefone do professor: ")
    email = input("Digite o email do professor: ")
    disciplina = input("Digite a disciplina do professor: ")

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
    lista_professores.append(professor)
    print("Professor cadastrado com sucesso!")

def cadastrar_disciplina(lista_disciplinas):
    nome = input("Digite o nome da disciplina: ")
    codigo = input("Digite o código da disciplina: ")
    carga_horaria = input("Digite a carga horária da disciplina: ")
    professor = input("Digite o nome do professor responsável: ")

    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_horaria": carga_horaria,
        "professor": professor,
    }
    lista_disciplinas.append(disciplina)
    print("Disciplina cadastrada com sucesso!")

def cadastrar_turma(lista_turmas):
    nome = input("Digite o nome da turma: ")
    codigo = input("Digite o código da turma: ")
    disciplina = input("Digite o nome da disciplina: ")
    professor = input("Digite o nome do professor: ")
    alunos = input("Digite os nomes dos alunos (separados por vírgula): ").split(', ')

    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplina": disciplina,
        "professor": professor,
        "alunos": alunos
    }
    lista_turmas.append(turma)
    print("Turma cadastrada com sucesso!")

def listar_alunos(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\nLista de alunos cadastrados:")
    for aluno in lista_alunos:
        print(
            f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, "
            f"Data de nascimento: {aluno['dt_nasc']}, Sexo: {aluno['sexo']}, "
            f"Endereço: {aluno['endereco']}, Telefone: {aluno['telefone']}, E-mail: {aluno['email']}"
        )

def listar_professores(lista_professores):
    if not lista_professores:
        print("Nenhum professor cadastrado.")
        return

    print("\nLista de professores cadastrados:")
    for professor in lista_professores:
        print(
            f"Nome: {professor['nome']}, Matrícula: {professor['matricula']}, "
            f"Data de nascimento: {professor['dt_nasc']}, Sexo: {professor['sexo']}, "
            f"Endereço: {professor['endereco']}, Telefone: {professor['telefone']}, E-mail: {professor['email']}, "
            f"Disciplina: {professor['disciplina']}"
        )

def listar_disciplinas(lista_disciplinas):
    if not lista_disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("\nLista de disciplinas cadastradas:")
    for disciplina in lista_disciplinas:
        print(
            f"Nome: {disciplina['nome']}, Código: {disciplina['codigo']}, "
            f"Carga Horária: {disciplina['carga_horaria']}, Professor: {disciplina['professor']}"
        )

def listar_turmas(lista_turmas):
    if not lista_turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("\nLista de turmas cadastradas:")
    for turma in lista_turmas:
        print(
            f"Nome: {turma['nome']}, Código: {turma['codigo']}, "
            f"Disciplina: {turma['disciplina']}, Professor: {turma['professor']}, "
            f"Alunos: {', '.join(turma['alunos'])}"
        )

def cadastros(lista_alunos, lista_professores, lista_disciplinas, lista_turmas):
    while True:
        print("\nMenu Cadastros:")
        print("1. Cadastro de Aluno")
        print("2. Cadastro de Professor")
        print("3. Cadastro de Disciplina")
        print("4. Cadastro de Turma")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno(lista_alunos)
        elif opcao == "2":
            cadastrar_professor(lista_professores)
        elif opcao == "3":
            cadastrar_disciplina(lista_disciplinas)
        elif opcao == "4":
            cadastrar_turma(lista_turmas)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def listagens(lista_alunos, lista_professores, lista_disciplinas, lista_turmas):
    while True:
        print("\nMenu Listagens:")
        print("1. Listar Alunos")
        print("2. Listar Professores")
        print("3. Listar Disciplinas")
        print("4. Listar Turmas")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_alunos(lista_alunos)
        elif opcao == "2":
            listar_professores(lista_professores)
        elif opcao == "3":
            listar_disciplinas(lista_disciplinas)
        elif opcao == "4":
            listar_turmas(lista_turmas)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu():
    lista_alunos = []
    lista_professores = []
    lista_disciplinas = []
    lista_turmas = []

    while True:
        print("\nMenu Principal:")
        print("1. Cadastros")
        print("2. Listagens")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastros(lista_alunos, lista_professores, lista_disciplinas, lista_turmas)
        elif opcao == "2":
            listagens(lista_alunos, lista_professores, lista_disciplinas, lista_turmas)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
