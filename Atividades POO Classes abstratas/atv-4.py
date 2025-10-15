from abc import ABC, abstractmethod
# 4- Herança parcial
#Crie uma classe abstrata Transporte
#com dois métodos abstratos: mover() e parar().
#Depois, crie uma subclasse Carro
#que implemente apenas o método mover().
#O que acontece quando você tenta instanciar Carro?
#Corrija implementando o segundo método.

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

# Tentativa parcial (gera erro se tentar instanciar)
class Carro(Transporte):
    def mover(self):
        return "O carro está se movendo"

    def parar(self):
        return "O carro parou"

# Testando
carro = Carro()
print(carro.mover())
print(carro.parar())
