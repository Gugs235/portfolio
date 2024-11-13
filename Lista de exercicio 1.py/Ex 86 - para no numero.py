# Crie uma função geradora conta_ate_n(n) que gere números de 1 até n.

def conta_ate_n(n):
    contador = 1
    while contador <= n:
        yield contador
        contador += 1

n = int(input("Escolha o número em que deseja parar: "))

for numero in conta_ate_n(n):
    print(numero)
