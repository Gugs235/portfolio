# Implemente um gerador pares(n) que gere todos os números pares de 1 até n.

def pares(n):
    i = 2 
    while i <= n:
        yield i  # "yield" devolve o próximo valor na sequência
        i += 2 

n = int(input("Escolha o número em que deseja parar: "))
for numero in pares(n):
    print(numero)
