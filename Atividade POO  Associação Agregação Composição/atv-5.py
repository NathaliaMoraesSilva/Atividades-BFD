# 5- Crie a classe Carro que possui um Motor.
# O Motor deve ser criado dentro do Carro.
# Se o Carro deixar de existir, o Motor também deixa.
# Mostre isso criando e depois apagando o objeto.

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

# Exemplo
carro = Carro("Fusca", 120)
print(f"{carro.modelo} tem um motor de {carro.motor.potencia}cv")

# Apagando carro
del carro
# motor não existe mais fora do carro
