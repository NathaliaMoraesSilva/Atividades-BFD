#1-Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.
def saudacao():
    return "Bem vindo ao Python"
print(saudacao())

#2-Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. Teste chamando a função com diferentes valores.
def dobro (m):
    m = m*2
    return m
print(dobro(3))

#3-Crie uma função chamada soma que receba dois números e retorne a soma deles. Depois, use a função para somar 10 + 20.
def soma(a,b):
    s = a + b
    return s
print(soma(10,20,))

#4Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:
#"Olá, [nome]!"
#Caso o nome não seja informado, mostre "Olá, visitante!".
def mensagem(nome):
    n =  "nome"
    if n == nome:
        return "Olá nome"
    elif n != nome:
        return "Olá visitante"
    else :
        print("")
print(mensagem("maria"))
print(mensagem("nome"))

#5-Crie uma função chamada operacoes que receba dois números e retorne a soma, a subtração e a multiplicação deles.
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    return soma, subtracao, multiplicacao
print(operacoes(10,20))

#6- Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. Teste com 3, 5 e 7 valores diferentes.
def media(*numeros):
    return sum(numeros) / len(numeros)
print(media(3, 4, 5))
print(media(1, 2, 3, 4, 5))
print(media(2, 4, 6, 8, 10, 12, 14))

#7-Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:
def dados_pessoais(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
dados_pessoais(nome="Ana", idade=25, cidade="Recife")

#8-Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.
def calculadora():
    n1 =int (input("Digite o primero número"))
    n2 =int (input ("Digite o segundo número"))
    operacao = input("Escolha a operação: ")
    r1=n1+n2
    r2=n1-n2
    r3=n1*n2
    if operacao == "somar":
         return r1
    elif operacao == "subtrair":
         return r2
    elif operacao == "multiplicar":
         return r3
print("O Resultado foi :",calculadora())


#9Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação).
# Exemplo:
#def soma(a, b): return a + b
#aplicar_operacao(3, 4, soma)
def aplicar_operacao(a, b, func):
    return func(a, b)
def soma(x, y):
    return x + y
def multiplicacao(x, y):
    return x * y
print(aplicar_operacao(3, 4, soma))          # 7
print(aplicar_operacao(3, 4, multiplicacao)) # 12












