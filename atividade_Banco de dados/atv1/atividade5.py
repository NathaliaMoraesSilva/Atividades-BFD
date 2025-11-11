import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n5) Nome e mensalidade dos cursos que custam mais de 600 reais:")
cursor.execute("SELECT nome, mensalidade FROM Curso WHERE mensalidade > 600;")

for linha in cursor.fetchall():
    print(linha)

conexao.close()