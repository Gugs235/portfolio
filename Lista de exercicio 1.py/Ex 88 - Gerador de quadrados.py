# Escreva um gerador quadrados(n) que gere os quadrados dos números de 1 até n

def quadrados(n):
    for i in range(1, n+1):
        yield i * i

n = int(input("Escolha o número: "))
for quadrado in quadrados(n):
    print(quadrado)
