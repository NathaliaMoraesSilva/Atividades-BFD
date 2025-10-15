# 6 - Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.).
# Cada Comodo deve ser criado dentro da Casa.

class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto")
        ]

# Exemplo
casa = Casa()
print("A casa possui os seguintes cômodos:")
for c in casa.comodos:
    print(f"- {c.nome}")
