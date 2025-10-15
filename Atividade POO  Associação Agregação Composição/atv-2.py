#  2- Crie as classes Aluno e Onibus.
#  Crie um método em Aluno que use a classe Onibus.

class Onibus:
    def __init__(self, linha):
        self.linha = linha

    def ir_para_escola(self):
        return f"indo para a escola na linha {self.linha}"

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def ir_para_escola(self, onibus: Onibus):
        print(f"{self.nome} {onibus.ir_para_escola()}")

# Exemplo
onibus = Onibus("205B")
aluno = Aluno("João")
aluno.ir_para_escola(onibus)
