# Crie uma função soma_recursiva(n) que soma todos os números de 1 até n recursivamente.

def soma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)

n = int(input("Digite um número: "))
resultado = soma_recursiva(n)
print(f"A soma de todos os números de 1 até {n} é: {resultado}")
