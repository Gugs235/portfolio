# Escreva uma função potencia(base, expoente) que calcule base elevado a expoente.

def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado

base = int(input("Escreva o número da base: "))
expoente = int(input("Escreva o número do expoente: "))
print(potencia(base, expoente))
