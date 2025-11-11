import sqlite3

con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

cursor.execute("SELECT COUNT(*) FROM Aluno;")
total_alunos = cursor.fetchone()[0]

print("Total de alunos:", total_alunos)

con.close()
