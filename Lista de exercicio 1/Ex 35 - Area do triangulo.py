# Crie uma função area_triangulo(base, altura) que calcule a área de um triângulo.

def area_triangulo(base, altura):
    return (base * altura) / 2


base = int(input("Escreva o tamanho da base: "))
altura = int(input("Escreva o tamanho da altura: "))
area = area_triangulo(base, altura)
print(f"A área do triângulo é: {area:.4f}")
