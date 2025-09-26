#8- Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe,
# apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"


class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)


aluno1 = Aluno("Maria", 9.5)
aluno2 = Aluno("João", 8.0)
aluno3 = Aluno("Ana", 7.5)

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

for a in turma.alunos:
    print(a)
