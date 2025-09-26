#01-Crie uma classe Usuario com atributos
# nome e email. Depois, crie uma classe
# Cliente que herde de Usuario.
# Crie uma instancia de um cliente e acesse todos os atributos.
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    pass


cliente1 = Cliente("Ana", "ana@email.com")

print(cliente1.nome)
