import sqlite3

con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

# Pegando nome e média dos alunos
cursor.execute("SELECT nome, (nota1 + nota2) / 2 AS media FROM Aluno ORDER BY media DESC LIMIT 10")
medias = cursor.fetchall()

print("Top 10 médias:")
print(medias)

con.close()