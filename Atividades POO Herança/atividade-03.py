#3-Na classe Usuario,
# crie um método saudacao()
#  que retorna "Olá, usuário". Na classe Cliente,
#  sobrescreva esse método para retornar "Olá, cliente".
#   Mostre como funciona a chamada.

class Usuario:
    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def saudacao(self):
        return "Olá, cliente"

cliente1 = Cliente()
print(cliente1.saudacao())
