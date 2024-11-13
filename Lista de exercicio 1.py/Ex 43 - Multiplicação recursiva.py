# Escreva uma função recursiva produto(a, b) que multiplica dois números inteiros a e b.

def produto(a, b):
    if b == 0:
        return 0
    elif b > 0:
        return a + produto(a, b - 1)
    else:
        return -produto(a, -b)


a = int(input("Digite um número para a: "))
b = int(input("Digite um número para b: "))
print(produto(a, b))
