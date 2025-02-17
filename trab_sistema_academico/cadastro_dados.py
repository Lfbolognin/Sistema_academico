#############FAZ OS CADASTROS ####################

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
    lista_prof.append(professor)
    print("Professor cadastrado com sucesso!")

def cadastrar_disciplina(lista_disciplina):
    nome = input("Digite o nome do professor: ")
    codigo = input("Digite o codigo da disciplina: ")
    carga_hr = input("Digite a Carga hora da disciplina: ")
    professor = input("Digite o sexo do professor: ")
    
    disciplina = {
        "nome": nome,
        "codigo": codigo,
        "carga_hr": carga_hr,
        "professor": professor,  
    }
    lista_disciplina.append(disciplina)
    print("Disciplina cadastrada com sucesso!")

def cadastrar_turma(lista_turma, lista_alunos):
    nome = input("Digite o nome da turma: ")
    codigo = input("Digite o codigo da turma: ")
    disciplina = input("Digite o nome da disciplina: ")
    professor = input("Digite o nome do professor: ")
    alunos = input("Digite os alunos dessa turma: ")
    
 # Cadastro dos alunos na turma
    alunos_turma = []
    while True:
        matricula_aluno = input("Digite a matrícula de um aluno para adicionar à turma (ou 'fim' para encerrar): ")
        if matricula_aluno.lower() == 'fim':
            break

        # Verificar se o aluno está cadastrado
        aluno_encontrado = False
        for aluno in lista_alunos:
            if aluno['matricula'] == matricula_aluno:
                alunos_turma.append(aluno)
                aluno_encontrado = True
                print(f"Aluno {aluno['nome']} adicionado à turma.")
                break

        if not aluno_encontrado:
            print("Aluno não encontrado. Tente novamente ou digite 'fim' para encerrar.")

    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplina": disciplina,
        "professor": professor,
        "alunos": alunos,
       
    }
    lista_turma.append(turma)
    print("Turma cadastrada com sucesso!")
############################################################

######################FAZ A LISTAGEM DOS DADOS######################

def listar_alunos(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nLista de alunos cadastrados:")
    for idx, aluno in enumerate(lista_alunos, start=1):
        print(f"Nome: {aluno['nome']}, Matricula: {aluno['matricula']}, Data de nascimento: {aluno['dt_nasc']}, Sexo: {aluno['sexo']}, Endereço: {aluno['endereco']}, Telefone: {aluno['telefone']}, E-mail: {aluno['email']}")

def listar_professor(lista_professores):
    if not lista_professores:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nLista de alunos cadastrados:")
    for idx, professor in enumerate(lista_professores, start=1):
        print(f"Nome: {professor['nome']}, Matricula: {professor['matricula']}, Data de nascimento: {professor['dt_nasc']}, Sexo: {professor['sexo']}, Endereço: {professor['endereco']}, Telefone: {professor['telefone']}, E-mail: {professor['email']}, Disciplina: {professor['disciplina']} ")

def listar_turma(lista_turma):
    if not lista_turma:
        print("Nenhum aluno cadastrado.")
        return
    
    print("\nLista de alunos cadastrados:")
    for idx, turma in enumerate(lista_turma, start=1):
        print(f"Nome: {turma['nome']}, Codigo: {turma['codigo']}, Disciplina: {turma['disciplina']}, Professor: {turma['professor']}, Alunos: {turma['alunos']}")

def listar_disciplina(lista_disciplina):
    if not lista_disciplina:
        print("Nenhuma disciplia cadastrada.")
        return
    
    print("\nLista de Disciplinas cadastradas:")
    for idx, disciplina in enumerate(lista_disciplina, start=1):
        print(f"Nome: {disciplina['nome']}, Codigo: {disciplina['codigo']}, Carga Hora: {disciplina['carga_hr']}, Professor: {disciplina['disciplina']}")
#######################################################################################

#############EFETUA AS FILTRAGENS ####################

def filtro_professor_disciplina(lista_professores):
    if not lista_professores:
        print("Esse professor não está cadastrado")
        return
    
    disciplica_consultada = input("Digite o nome da disciplina para filtrar os professores: ")

    professores_filtrados = [
         professor for professor in lista_professores if professor['disciplina'].lower() == disciplica_consultada.lower()

    ]


    if professores_filtrados:
        print(f"\nProfessores que ensinam a disciplina '{disciplica_consultada}':")
        for professor in professores_filtrados:
            print(f"Nome: {professor['nome']}, Matricula: {professor['matricula']}, E-mail: {professor['email']}")
    else:
        print(f"Nenhum professor encontrado para a disciplina '{disciplica_consultada}'.")

def disciplinas_por_professor(lista_professores):
    if not lista_professores:
        print("Nenhum professor cadastrado.")
        return

    nome_professor = input("Digite o nome do professor para ver as disciplinas alocadas: ")

    # Procurando o professor na lista
    professor_encontrado = None
    for professor in lista_professores:
        if professor['nome'].lower() == nome_professor.lower():
            professor_encontrado = professor
            break

    if professor_encontrado:
        print(f"\nDisciplinas alocadas ao professor {nome_professor}:")
        if 'disciplina' in professor_encontrado:
            print(professor_encontrado['disciplina'])
        else:
            print(f"O professor {nome_professor} não tem disciplinas alocadas.")
    else:
        print(f"Professor {nome_professor} não encontrado.")

########################################################################################################################

##MENUS ESPECIFICOS##

def cadastros (lista_alunos, lista_professores, lista_disciplina, lista_turma):
    while True:
        print("\nMenu cadastros:")
        print("1. Cadastro Aluno")
        print("2. Cadastro Professor")
        print("3. Cadastro Disciplina")
        print("4. Cadastro Turma")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno(lista_alunos)
        elif opcao == "2":
            cadastrar_prof(lista_professores)
        elif opcao == "3":
            cadastrar_disciplina(lista_disciplina)
        elif opcao == "4":
            cadastrar_turma(lista_turma)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def listagens(lista_alunos, lista_professores, lista_disciplina, lista_turmas):
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
            listar_professor(lista_professores)
        elif opcao == "3":
            listar_disciplina(lista_disciplina)
        elif opcao == "4":
            listar_turma(lista_turmas)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def filtros(lista_alunos, lista_professores, lista_disciplina, lista_turmas):
    while True:
        print("\nMenu de consultas:")
        print("1. Consulta de professor x disciplina")
        print("2. Listar disciplinas atribuidas a algum professor")
        print("3. Listar Disciplinas")
        print("4. Listar Turmas")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            filtro_professor_disciplina(lista_professores)
        elif opcao == "2":  # A opção 5 será a nova funcionalidade
            disciplinas_por_professor(lista_professores)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

########################################################################################################################

##MENUS GERAL##

def menu():
    lista_alunos = []
    lista_professores = []
    lista_disciplina = []
    lista_turma = []

    while True:
        print("\nMenu principal:")
        print("1. Cadastros")
        print("2. Listagens")
        print("3. Filtragens")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastros(lista_alunos, lista_professores, lista_disciplina, lista_turma)
        elif opcao == "2":
            listagens(lista_alunos, lista_professores, lista_disciplina, lista_turma)
        elif opcao == "3":
            filtros(lista_alunos, lista_professores, lista_disciplina, lista_turma)
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
############################################################################################################################################
menu()