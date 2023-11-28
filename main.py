import biblioteca as bib
while True:
    print("""
[1] Adicionar aluno
[2] Listar todos os alunos
[3] Informar a nota do aluno
[4] Média das notas""")
    esc = int(input(">> "))


    if(esc == 1):
        dic = {}

        dic["nome"] = input("Nome: ").capitalize()
        dic["disciplina"] = input("Disciplina: ")
        dic["nota"] = float(input("Nota: "))
        bib.insert("arq.txt", dic)
        print("Dados inseridos :)")

    elif(esc == 2):
        alunos = bib.listar("arq.txt")
        print("Alunos:")
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}")
            print(f"Disciplina: {aluno['disciplina']}")
            print(f"Nota: {aluno['nota']}")
            print("-" * 20)

    elif(esc == 3):
        nome = input("Nome: ").capitalize()
        disciplina = input("Disciplina: ")
        print(bib.infNota(nome, disciplina))

    elif(esc == 4):
        disciplina = input("Disciplina: ")
        print(bib.media(disciplina))
    else:
        break