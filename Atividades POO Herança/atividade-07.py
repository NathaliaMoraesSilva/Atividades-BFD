#07-Usando o exemplo anterior, adicione um método status()
# em Autenticacao
#e também em Permissao.
#Se a classe Administrador herda das duas,
# qual versão de status() será chamada?
# Use Administrador.__mro__ para mostrar a ordem.

class Autenticacao:
    def status(self):
        return "Status da Autenticação"

class Permissao:
    def status(self):
        return "Status da Permissão"

class Administrador(Autenticacao, Permissao):
    pass

adm = Administrador()
print(adm.status())  # Qual será chamado? (Autenticacao vem primeiro)

# Ordem de resolução de métodos (MRO) com quebra de linha
print("Ordem de resolução de métodos (MRO):")
for classe in Administrador.__mro__:
    print(classe)
