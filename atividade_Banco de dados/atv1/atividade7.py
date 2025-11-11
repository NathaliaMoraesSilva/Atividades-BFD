import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n7) Ano das turmas e quantidade de turmas por ano:")
cursor.execute("SELECT ano, COUNT(*) FROM Turma GROUP BY ano;")

for linha in cursor.fetchall():
    print(linha)

conexao.close()
