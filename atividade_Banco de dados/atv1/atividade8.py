import sqlite3

conexao = sqlite3.connect('../tabela_alunos.db')
cursor = conexao.cursor()

print("\n8) Média da nota1 dos alunos por turma_id:")
cursor.execute("SELECT turma_id, AVG(nota1) FROM Aluno GROUP BY turma_id;")

for linha in cursor.fetchall():
    print(linha)

conexao.close()