#5-Primeira letra maiúscula (map + lambda)
#Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].
nomes = ["ana", "pedro", "maria"]
resultado = list(map(lambda x: x.capitalize(), nomes))
print(resultado)
