# Crie uma função raiz_quadrada(n) que retorne a raiz quadrada de um número.

def raiz_quadrada(n):
    if n < 0:
        return "Número inválido. Não é possível calcular a raiz quadrada de um número negativo."
    aproximacao = 0.0
    incremento = 0.0001
    while aproximacao * aproximacao < n:
        aproximacao += incremento
    
    return aproximacao

numero = int(input("Escreva o número: "))
resultado = raiz_quadrada(numero)
print(f"A raiz quadrada de {numero} é aproximadamente {resultado:.4f}")

