# Crie uma função mcd(a, b) que calcule o máximo divisor comum de dois números 
# usando recursão.

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado = mcd(numero1, numero2)
print(f"O MDC de {numero1} e {numero2} é {resultado}")
