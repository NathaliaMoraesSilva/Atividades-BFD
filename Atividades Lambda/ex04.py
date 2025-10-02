#4- Ordenação por comprimento da palavra (sorted + lambda)
#Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.
frutas = ["uva", "banana", "maçã", "laranja",]
palavra=sorted(frutas, key=lambda x: len(x))
print(palavra)