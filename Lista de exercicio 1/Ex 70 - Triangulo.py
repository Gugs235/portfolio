# Crie uma função classifica_triangulo(a, b, c) que classifique um 
# triângulo com base em seus lados.

def classifica_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Valores inválidos para os lados de um triângulo."
    
    # Condição de existência de triângulo 
    # (A soma de dois lados deve ser maior que o terceiro)
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo."
    
    # Classificação do triângulo
    if a == b == c:
        return "Triângulo equilátero"
    elif a == b or b == c or a == c:
        return "Triângulo isósceles"
    else:
        return "Triângulo escaleno"

print(classifica_triangulo(3, 3, 3))  # Triângulo equilátero
print(classifica_triangulo(3, 3, 5))  # Triângulo isósceles
print(classifica_triangulo(3, 4, 5))  # Triângulo escaleno
print(classifica_triangulo(1, 2, 3))  # Não é um triângulo
