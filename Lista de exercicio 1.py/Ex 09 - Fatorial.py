def fatorial(f):
    resultado = 1
    for i in range(1, f + 1):
        resultado *= i
    return resultado

# Teste
n = int(input("Digite um número: "))
print(f"O fatorial de {n} é {fatorial(n)}")
