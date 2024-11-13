# Implemente uma função potencia_recursiva(base, exp) que calcula a potência de forma recursiva.

def potencia_recursiva(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / potencia_recursiva(base, -exp)
    else:
        return base * potencia_recursiva(base, exp - 1)

base = float(input("Digite a base: "))
exp = int(input("Digite o expoente: "))

resultado = potencia_recursiva(base, exp)
print(f"{base} elevado a {exp} é igual a {resultado}")
