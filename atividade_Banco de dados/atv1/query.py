import sqlite3

conexao = sqlite3.connect("tabela_alunos.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM Aluno")

alunos = cursor.fetchall()

for aluno in alunos:
    print(aluno)

cursor.execute("SELECT nome, nota1 FROM Aluno")

alunos1 = cursor.fetchall()

for aluno in alunos1:
    print(aluno)

cursor.execute("SELECT * FROM Aluno WHERE nota2 > 8 ")

alunos2 = cursor.fetchall()

for aluno in alunos2:
    print(aluno)



