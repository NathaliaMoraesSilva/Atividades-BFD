import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n6) Nome das turmas e o ano, ordenados pelo ano (crescente):")
cursor.execute("SELECT nome, ano FROM Turma ORDER BY ano ASC;")

for linha in cursor.fetchall():
    print(linha)

conexao.close()