
# 1- Crie as classes Pessoa e Livro
# e demonstre uma relação de associação entre eles.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

# Associação
pessoa1 = Pessoa("Alice")
livro1 = Livro("Python Básico")

print(f"{pessoa1.nome} está lendo o livro '{livro1.titulo}'")
