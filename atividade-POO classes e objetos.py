class pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade


    def apresentacao (self):
        return f"olá meu {self.nome} e tenho {self.idade}"

pessoa1 = pessoa("pedro", 23)
pessoa2 = pessoa("Joao", 24)
print(pessoa1.apresentacao())
print(pessoa2.aprese)