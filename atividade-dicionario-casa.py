# 1-Crie um dicionário simples
# Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.
aluno = {"nome ": "carlos", "idade": 25, "nota": 8.0}

# 2-Acessando valores
#Dado o dicionário:
#produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
#Imprima o nome do produto e a quantidade em estoque.
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print(produto["nome"])
print(produto["estoque"])
# 3-Adicionando novos pares chave-valor
#Dado o dicionário:
#pessoa = {"nome": "Carlos", "idade": 30}
#Adicione uma nova chave "cidade" com valor "São Paulo".
pessoa = {"nome": "Carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"
print(pessoa)

# 4-Removendo elementos
#Dado o dicionário:
#carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
#Remova a chave "ano" do dicionário.
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
carro.pop("ano")
print(carro)

# 5-Verificando existência de uma chave
#Verifique se a chave "telefone" existe no dicionário:
#contato = {"nome": "Ana", "email": "ana@email.com"}
contato = {"nome": "Ana", "email": "ana@email.com"}
print(contato.get("telefone"))

#6-Contando frequência de palavras
#Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
#palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
contagem = {}
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)

#7- Invertendo um dicionário
#Dado o dicionário:
#d = {"a": 1, "b": 2, "c": 3}
#Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
d = {"a": 1, "b": 2, "c": 3}
print(d)
invertido = {}
for letra, numero in d.items():
    invertido[numero] = letra
print(f"invertida",invertido)

# 8- Dicionário com alunos e suas 3 notas
#Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
notas_alunos = {"Ana": [8, 7, 9],"João": [6, 7, 5],"Carla": [9, 10, 10]}
for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    print(f"A média de {aluno} é {media:.2f}")

# 9- Mesclando dois dicionários
# Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
def mesclar_dicts(dict1, dict2):
    dict_resultado = dict1.copy()
    dict_resultado.update(dict2)
    return dict_resultado
grupo1 = {'Aria': 8, 'Bruna': 6}
grupo2 = {'Bruna': 10, 'Catia': 9}
resultado_final = mesclar_dicts(grupo1, grupo2)
print(resultado_final)

# 10-Ordenando dicionário por valor
# Dado o dicionário:
# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
ordenado = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)
for nome, pontos in ordenado:
    print(f"{nome}: {pontos}")
