#2-Filtrar pares (filter + lambda)
#Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pare
l = [10, 15, 20, 25, 30]
par = list(filter(lambda x: x %  2 == 0, l))
print(par)