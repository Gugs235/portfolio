#5.	Soma dos N primeiros Naturais: Escreva uma função soma_naturais(n) que retorna 
# a soma dos N primeiros números naturais.

def soma_naturais(n):
    return n * (n + 1) // 2
n = 5
resultado = soma_naturais(n)
print(resultado)  # Saída: 15 (1 + 2 + 3 + 4 + 5)
