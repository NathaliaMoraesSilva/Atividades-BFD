import sqlite3

con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

cursor.execute("SELECT AVG(nota2) FROM Aluno;")
media_nota2 = cursor.fetchone()[0]

print("Média da nota2:", media_nota2)

con.close()