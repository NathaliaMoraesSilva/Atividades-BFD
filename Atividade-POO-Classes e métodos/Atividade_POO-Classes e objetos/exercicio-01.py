#1- Na classe, ContaBancaria, converta saldo para uma atributo privado.
# Crie um método setter e um getter para acessar e modificar essa atributo,
#  seguindo uma regra lógica (Ex: saldo não pode ser negativo)

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo if saldo >= 0 else 0

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo!")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            print("Saque não permitido!")
            return False


conta = ContaBancaria("Maria", 100)

print("Saldo inicial:", conta.get_saldo())

conta.depositar(50)
print("Depois de depositar 50:", conta.get_saldo())

conta.sacar(120)
print("Depois de sacar 120:", conta.get_saldo())

conta.set_saldo(-200)
print("Tentando saldo negativo:", conta.get_saldo())

conta.set_saldo(500)
print("Novo saldo atualizado pelo setter:", conta.get_saldo())
