import sqlite3

con = sqlite3.connect("escola_v2.db")
cursor = con.cursor()

# LEFT JOIN só da turma 2
cursor.execute("""
SELECT *
FROM Aluno
LEFT JOIN Turma
ON Aluno.idTurma = Turma.idTurma
WHERE Aluno.idTurma = 2
""")

turma2 = cursor.fetchall()

print("Alunos da turma 2:")
print(turma2)

con.close()
