import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n3) Alunos com nota2 maior que 8:")
cursor.execute("SELECT * FROM Aluno WHERE nota2 > 8;")

for linha in cursor.fetchall():
    print(linha)

conexao.close()