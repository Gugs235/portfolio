# Implemente uma função aproxima_pi(n) que calcula uma aproximação do número pi usando n termos da série de Leibniz.

def aproxima_pi(n):
    pi_aproximado = 0
    for i in range(n):
        # Fórmula da série de Leibniz
        pi_aproximado += ((-1) ** i) / (2 * i + 1)
    pi_aproximado *= 4
    return pi_aproximado

n = int(input("Digite o número de termos para aproximar o valor de pi: "))
pi = aproxima_pi(n)
print(f"Aproximação de pi com {n} termos: {pi}")
