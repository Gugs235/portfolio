# Crie uma função gera_fibonacci_lista(n) que gera uma lista com os n primeiros 
# números de Fibonacci.

def gera_fibonacci_lista(n):
    fibonacci = [0, 1]
    
    for i in range(2, n):
        # O próximo número é a soma dos dois anteriores
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    
    return fibonacci[:n]

n = int(input("Digite o número de termos de Fibonacci desejados: "))
fibonacci_lista = gera_fibonacci_lista(n)
print(f"Os {n} primeiros números de Fibonacci são: {fibonacci_lista}")
