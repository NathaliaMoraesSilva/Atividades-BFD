class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
##2-Expanda a classe Pessoa para incluir um método apresentar()
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
