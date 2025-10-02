#7-Ordenar por último caractere (sorted + lambda)
#Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.
frutas = ["banana", "uva", "maçã", "laranja"]
reverso = sorted(frutas, key=lambda x: x[-1])
print(reverso)
