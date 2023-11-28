def insert(file, dic):
    arquivo = open(file, "a")
    arquivo.write(f"{dic['nome']};")
    arquivo.write(f"{dic['disciplina']};")
    arquivo.write(f"{dic['nota']}\n")
    arquivo.close()

def listar(file):
    arquivo = open(file, "r")
    linhas = arquivo.readlines()
    vetor = [""] * len(linhas)
    for c in range(0, len(vetor)):
        dados = linhas[c].replace("\n","")
        dados = dados.split(";")
        vetor[c] = {}
        vetor[c]["nome"] = dados[0]
        vetor[c]["disciplina"] = dados[1]
        vetor[c]["nota"] = float(dados[2])

    arquivo.close()
    return vetor

def infNota(nome, disc):
    alunos = listar("arq.txt")
    for aluno in alunos:
        if(aluno['nome'] == nome and aluno['disciplina'] == disc):
            return aluno
    print("Aluno não encontrado na disciplina")

def media(disciplina):
    alunos  = listar("arq.txt")
    cont = med = 0
    for aluno in alunos:
        if(aluno['disciplina'] == disciplina):
            med += aluno['nota']
            cont += 1
    
    medi = med/cont
    return medi

    