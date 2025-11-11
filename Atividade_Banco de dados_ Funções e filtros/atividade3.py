import sqlite3

con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

cursor.execute("SELECT MAX(nota1) FROM Aluno;")
maior_nota1 = cursor.fetchone()[0]

print("Maior nota1:", maior_nota1)

con.close()
