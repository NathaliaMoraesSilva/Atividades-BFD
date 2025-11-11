import sqlite3

con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

cursor.execute("SELECT SUM(mensalidade) FROM Curso;")
soma_mensalidades = cursor.fetchone()[0]

print("Soma das mensalidades:", soma_mensalidades)

con.close()