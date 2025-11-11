import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n4) Alunos nascidos após o ano de 2000:")
cursor.execute("SELECT * FROM Aluno WHERE data_nascimento > '2000-12-31';")

for linha in cursor.fetchall():
    print(linha)

conexao.close()