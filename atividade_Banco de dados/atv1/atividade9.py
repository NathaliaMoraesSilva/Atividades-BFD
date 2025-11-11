import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n9) Anos com mais de 2 turmas:")
cursor.execute("SELECT ano, COUNT(*) FROM Turma GROUP BY ano HAVING COUNT(*) > 2;")

for linha in cursor.fetchall():
    print(linha)

conexao.close()