from abc import ABC, abstractmethod
# 3-Interface em herança múltipla
# Crie uma interface Imprimivel com o método imprimir().
# Crie outra interface Exportavel com o método exportar().
# Implemente uma classe Relatorio que herde de ambas e implemente os métodos.
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return "Imprimindo relatório..."

    def exportar(self):
        return "Exportando relatório para PDF..."

# Testando
rel = Relatorio()
print(rel.imprimir())
print(rel.exportar())
