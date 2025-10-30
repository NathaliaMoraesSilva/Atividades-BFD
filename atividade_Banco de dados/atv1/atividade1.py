import sqlite3


conexao = sqlite3.connect("tabela_alunos.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Aluno(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TXT,
    nota1 REAL,
    nota2 REAL,
    data_nascimento TEXT,
    turma_id INTEGER
)
""")

conexao.commit()
conexao.close()

conexao = sqlite3.connect("tabela_alunos.db")
cursor = conexao.cursor()


cursor.execute("INSERT INTO Aluno (nome, nota1, nota2, data_nascimento, turma_id) VALUES ('Maria', 9.0, 8.5, '2001-10-16', 1)")
cursor.execute("INSERT INTO Aluno(nome, nota1, nota2, data_nascimento, turma_id) VALUES ('João', 10, 9.5, '2001-8-12', 1)")
cursor.execute("INSERT INTO Aluno(nome, nota1, nota2, data_nascimento, turma_id) VALUES ('Ana', 8.2, 9.1, '2003-10-10', 2)")

conexao.commit()
conexao.close()

print("Tabela criada e alunos inseridos com sucesso!")
