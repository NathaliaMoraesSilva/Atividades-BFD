from abc import ABC, abstractmethod


# 1-Criando uma interface
#
# Crie uma interface chamada Pagamento com um método abstrato processar(valor).
# Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface.
# Mostre como chamar processar() para cada uma.

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

# Implementações
class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento de R${valor} no cartão de crédito."

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Gerando boleto de R${valor}."

# Testando
cartao = CartaoCredito()
boleto = Boleto()

print(cartao.processar(150))
print(boleto.processar(150))
