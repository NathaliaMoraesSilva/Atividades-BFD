# 1-Crie um dicionário simples
#Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.
aluno ={"nome":"João", "idade":30, "nota":6.00}

# 2- Acessando valores
# Dado o dicionário:
# produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
# Imprima o nome do produto e a quantidade em estoque.
produto = {"nome": "Caneta","preço":2.5, "estoque": 100}
print(produto["nome"])
print(produto["estoque"])

# 3-Adicionando novos pares chave-valor
# Dado o dicionário:
# pessoa = {"nome": "Carlos", "idade": 30}
# Adicione uma nova chave "cidade" com valor "São Paulo".
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"]="Recife"
print(pessoa)

# 4-Removendo elementos
# Dado o dicionário:
# carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# Remova a chave "ano" do dicionário.
carro={"marca":"Ford", "modelo":"Fiesta","ano":2010}
carro.pop("ano")
print(carro)

# 5-Verificando existência de uma chave
# Verifique se a chave "telefone" existe no dicionário:
# contato = {"nome": "Ana", "email": "ana@email.com"}
contato={"nome":"Ana", "email":"ana@email.com"}
print(contato.get("telefone"))

# 6-Contando frequência de palavras
# Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
palavras =["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
contagem ={}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
print(contagem)

# 7-Invertendo um dicionário
# Dado o dicionário:
# d = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
d = {"a:":1, "b":2, "c":3}
d = {1: "a", 2: "b", 3: "c"}

#8 Dicionário com listas
#Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
# Dicionário com alunos e suas notas
alunos = {
    "Ana": [8, 7, 9],
    "Bruno": [6, 9, 7],
    "Carla": [10, 9, 8]
}
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"A média de {nome} é {media:.2f}")

# 9- Mesclando dois dicionários
#Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
def mesclar_dict(d1, d2):
    # Cria um novo dicionário copiando o primeiro
    resultado = d1.copy()
# Exemplo
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

novo_dict = mesclar_dict(dict1, dict2)
print(novo_dict)



