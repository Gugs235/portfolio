# Crie um gerador fibonacci_gen(n) que gere os primeiros n termos da sequência de Fibonacci.

def fibonacci_gen(n):
    a, b = 0, 1 
    for _ in range(n):
        yield a 
        a, b = b, a + b 

n = int(input("Quantos termos da sequência de Fibonacci você quer gerar? "))
for termo in fibonacci_gen(n):
    print(termo)
