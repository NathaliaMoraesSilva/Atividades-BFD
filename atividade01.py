#1-Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros = ["O Senhor das Moscas", "O Médico e o Monstro", "Biblia"]
print(livros)

#2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
print(livros[0])
print(livros[1])

#3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append("O Senhor dos aneis")
livros.append("Harry Potter")
print(livros)

#4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1,"Duna")
print(livros)

#5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")

#6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.
números = [1,2,3,2,4,2,5]
print("O 2 é mostrados", números.count(2),"vezes")

#7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
for livros in livros:
    print(f"O livro",{livros},"é interessante" )

#8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
idades = [12, 18, 25, 14, 30]

for idades in idades:
    if idades >= 18:
        print(idades)
    else:
        print("")


#9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
valores = [10, 20, 30 ,40]
soma = 0
for valores in valores:
    soma += valores
print(f"A soma dos números é", soma)

#10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
#notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.
aluno = []

for i  in range(0,2):
    notas=[]
    for j in range (0,3):
        nota = int (input("Digite as notas dos alunos"))
        notas.append(nota)
        aluno.append(notas)

print(aluno)
