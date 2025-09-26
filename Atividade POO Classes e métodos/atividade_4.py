from carro import Carro
#4-Usando a classe Carro, crie um objeto
c1=Carro("Jeep", "Renagade", 2025)
#imprimindo antes da alteração
print("antes da alteração/n")
print(f"Marca: {c1.marca}, Modelo: {c1.modelo},Ano: {c1.ano},")
#imprimindo depois da alteração
c1.marca = "Ford"
print(f"Marca: {c1.marca}, Modelo: {c1.modelo},Ano: {c1.ano},")
