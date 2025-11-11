import sqlite3

con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

# LEFT JOIN
cursor.execute("""
SELECT *
FROM Aluno
LEFT JOIN Turma
ON Aluno.idTurma = Turma.idTurma
""")

resultado = cursor.fetchall()

print("LEFT JOIN Aluno + Turma:")
print(resultado)

con.close()
