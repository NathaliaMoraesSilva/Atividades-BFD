#5-Crie uma classe Funcionario
# que herda de Usuario e, em seguida,
# crie uma classe Gerente que herda de Funcionario.
# Mostre como instanciar um gerente e
# acessar seus atributos.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

class Gerente(Funcionario):
    def __init__(self, nome, email, setor):
        super().__init__(nome, email, "Gerente")
        self.setor = setor

gerente1 = Gerente("Carlos", "carlos@email.com", "TI")
print(gerente1.nome, gerente1.email, gerente1.cargo, gerente1.setor)
