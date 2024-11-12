# Implemente uma função eh_perfeito(n) que verifica se um número é um número perfeito.

def eh_perfeito(n):
    if n <= 1:
        return False
    soma_divisores = 0

    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i

    if soma_divisores == n:
        return True
    else:
        return False

numero = int(input("Digite um número para verificar se é perfeito: "))
if eh_perfeito(numero):
    print(f"{numero:.4f} é um número perfeito.")
else:
    print(f"{numero:.4f} não é um número perfeito.")
