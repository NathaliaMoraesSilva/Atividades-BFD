# 5-Crie uma classe ContaBancaria com os atributos titular e saldo.
# Adicione um método depositar(valor)
#  que aumenta o saldo e um método sacar(valor)
# que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False


# Testando
conta = ContaBancaria("João", 100)

if conta.sacar(50):
    print("Saque de 50 realizado com sucesso!")
else:
    print("Falha no saque de 50")

if conta.sacar(100):
    print("Saque de 100 realizado com sucesso!")
else:
    print("Falha no saque de 100")

print("Saldo final:", conta.saldo)
