# 3 - Crie uma classe Funcionario e Departamento
# que contém uma lista de Funcionarios.
# Departamento deve agregar funcionários já criados.

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

# Criando funcionários
f1 = Funcionario("Carlos")
f2 = Funcionario("Mariana")

# Criando departamento e agregando funcionários
dep = Departamento("TI")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)

print(f"Departamento {dep.nome} possui:")
for f in dep.funcionarios:
    print(f"- {f.nome}")

