# Implemente a função fibonacci(n) que retorna o n-ésimo termo da sequência de Fibonacci.

def fibonacci(n):
    if n <= 0:
        return "Por favor, insira um número positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Exemplo de uso
n = int(input("Digite a posição desejada na sequência de Fibonacci: "))
print(f"O {n}-ésimo termo da sequência de Fibonacci é:", fibonacci(n))
