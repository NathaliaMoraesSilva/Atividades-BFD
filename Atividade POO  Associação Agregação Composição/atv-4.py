# 4- Crie as classes Time e Jogador.
# Um Jogador tem nome e posição como atributos,
# enquanto Time agrega jogadores em uma lista.

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)

# Exemplo
j1 = Jogador("Neymar", "Atacante")
j2 = Jogador("Alisson", "Goleiro")

time = Time("Seleção Brasileira")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)

print(f"Time {time.nome} tem os jogadores:")
for j in time.jogadores:
    print(f"- {j.nome} ({j.posicao})")
