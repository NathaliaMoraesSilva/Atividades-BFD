from abc import ABC, abstractmethod
# 3- Múltiplos métodos abstratos
# Defina uma classe abstrata FormaGeometrica
# com dois métodos abstratos: area() e perimetro().
# Crie uma classe concreta Retangulo
# que herde de FormaGeometrica e implemente os dois métodos.
# Teste criando um objeto e calculando sua área e perímetro.
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

# Testando
r = Retangulo(5, 3)
print("Área do retângulo:", r.area())
print("Perímetro do retângulo:", r.perimetro())