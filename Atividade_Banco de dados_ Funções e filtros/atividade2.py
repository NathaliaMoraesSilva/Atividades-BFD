import sqlite3

con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

cursor.execute("SELECT MIN(mensalidade) FROM Curso;")
menor_mensalidade = cursor.fetchone()[0]

print("Menor mensalidade:", menor_mensalidade)

con.close()