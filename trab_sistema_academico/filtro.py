from cadastro_dados import menu, cadastrar_aluno, cadastrar_disciplina, cadastrar_prof, cadastrar_turma, lista_professores

def filtro_professor_disciplina():
    if not cadastrar_prof:
        print("Esse professor não está cadastrado")
        return
    
    disciplica_consultada = [

    ]

    professores_filtrados = [
         professor for professor in lista_professores if professor['disciplina'].lower() == disciplica_consultada.lower()

    ]


    if professores_filtrados:
        print(f"\nProfessores que ensinam a disciplina '{disciplica_consultada}':")
        for professor in professores_filtrados:
            print(f"Nome: {professor['nome']}, Matricula: {professor['matricula']}, E-mail: {professor['email']}")
    else:
        print(f"Nenhum professor encontrado para a disciplina '{disciplica_consultada}'.")
       


    