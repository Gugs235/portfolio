#10.	Diferença entre Máximo e Mínimo: Crie uma função diferenca_max_min(lista) 
# que retorna a diferença entre o maior e o menor elemento de uma lista.

def diferenca_max_min(lista):
    if not lista:
        return 0
    return max(lista) - min(lista)
numeros = [10, 7, 8, 9, 1, 5]
resultado = diferenca_max_min(numeros)
print(resultado)  # Saída: 9 (10 - 1)
