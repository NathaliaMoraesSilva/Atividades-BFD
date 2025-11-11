import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n10) Cursos ordenados pela mensalidade (decrescente):")
cursor.execute("SELECT nome, mensalidade FROM Curso ORDER BY mensalidade DESC;")

for linha in cursor.fetchall():
    print(linha)

conexao.close()