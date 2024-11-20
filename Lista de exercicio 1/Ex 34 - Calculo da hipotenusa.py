# Escreva uma função hipotenusa(a, b) que calcule a hipotenusa de um triângulo retângulo.

def hipotenusa(a, b):
    return (a**2 + b**2)**0.5

cateto1 = int(input("Escreva o tamanho do cateto 1: "))
cateto2 = int(input("Escreva o tamanho do cateto 2: "))
resultado = hipotenusa(cateto1, cateto2)
print(f"A hipotenusa é: {resultado:.4f}")
