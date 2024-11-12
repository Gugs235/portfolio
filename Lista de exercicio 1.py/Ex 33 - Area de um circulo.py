# Implemente uma função area_circulo(raio) que calcule a área de um círculo de raio r.

def area_circulo(raio):
    pi = 3.14159
    return pi * (raio ** 2)

raio = int(input("Escreva o raio do circulo: "))
print(f"A área do círculo com raio {raio} é: {area_circulo(raio):.2f}")
