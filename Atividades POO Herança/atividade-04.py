#4-Na classe Cliente, adicione o atributo saldo.
# Adicione um método construtor em Cliente
# que inicialize também os atributos de Usuario
# usando super().

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)  # chama construtor de Usuario
        self.saldo = saldo

cliente1 = Cliente("Maria", "maria@email.com", 500)
print(cliente1.nome, cliente1.email, cliente1.saldo)
