import sqlite3

# Conexão com o banco
con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

# Pegando todos os alunos
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()

print("Tabela Aluno completa:")
print(alunos)

con.close()
