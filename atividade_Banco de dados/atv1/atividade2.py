import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n2) Nome e nota1 de todos os alunos:")
cursor.execute("SELECT nome, nota1 FROM Aluno;")

for linha in cursor.fetchall():
    print(linha)

conexao.close()
