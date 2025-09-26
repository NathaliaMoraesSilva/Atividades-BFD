# 9- Crie uma classe Cachorro
# com um atributo de classe especie = "Canis familiaris"
# e atributos de instância nome e idade.
# Mostre a diferença entre acessar especie pelo objeto e pela classe.

class Cachorro:
    especie = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


dog1 = Cachorro("Rex", 5)
dog2 = Cachorro("Luna", 3)

print("Acessando pelo objeto:", dog1.especie)
print("Acessando pela classe:", Cachorro.especie)
