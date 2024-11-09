# é um código que só é executado quando é chamado
# geralmente serve para repetir tal parte, ao inves de fazer o código todo de novo, é só "chamar" esse código
# sintaxe: def nome ():
# {(o que estiver aqui dentro)}

def hello():
    print("OLÁ!!!")
# até aqui não vai acontecer nada
# para acontecer algo, chame pelo nome
hello()


# tem como fazer um parametro nessa função
# basicamente, o que for colocado dentro do parenteses vai virar uma variavel
def ola(nome):
    print("Olá" , nome)
# quando eu chamar a função tenho q colocar algo no parentes, e o que for colocado vai entrar na variavel
# se não colocar nada, vai dar erro
ola("Jhonathan")


# da para facilitar um pouco mais
# aqui basicamente o que esta dentro de uma variavel vai para dentro de outra variavel
def hello2(nome2):
    print("Seja Bem-Vindo",nome2)
# aqui o "a" esta sendo armazenada dentro do "nome" e que depois é chamada e mostrada
a = input("Digite seu nome: ")
hello2(a)


# da para ter mais de um parametro tambem, como a idade
def hello3 (nome3, idade3):
    print("Olá", nome3, "\nSua idade é: ",idade3)
a3 = input("Digite seu nome: ")
b3 = input("Digite sua idade: ")
hello3(a3,b3)


# não é possivel manipularmos o resultado do parametro, mas a um método...
def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas * taxa
    else:
        h_excd = horas - 40
        salario = 40 * taxa + (h_excd * (1.5 * taxa))
    print(salario)
qh = input("Digite a quantidade de horas do trabalho: ")
vh = input("Digite o valor da hora: ")
calcular_pagamento(qh,vh)


# return
# como ele sim podemos manipular o parametro
def soma(x,y):
    result = x + y
    return result
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
res = soma(a,b)
print("Soma", res)


# algo para brincar, inverter o nome
def inverte(nome, sobrenome):
    nomeInverso = sobrenome + " " + nome
    return nomeInverso
nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
invertido = inverte(nome,sobrenome)
print("Olá,", invertido)


# função com o return com o booleano
def par(x):
    if (x%2)==0:
        return True
    else:
        return False
while True:
    num = int(input("Insira um número: "))
    if par(num):
        print("É par")
    else:
        print("É impar")


# return com vários valores
def cadastro():
    name = input("Qual é o seu nome: ")
    age = input("Idade: ")
    return name, age
print("Iniciando cadastro...")
nome, idade = cadastro()
print("Cadastro realizado com sucesso:")
print(f"Seu nome é {nome} e você tem {idade} anos")


