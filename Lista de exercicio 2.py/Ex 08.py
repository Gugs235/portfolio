#8.	Ordenação com Insertion Sort: Implemente uma função insertion_sort(lista) que 
# ordena uma lista usando o algoritmo de Insertion Sort.

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista
numeros = [12, 11, 13, 5, 6]
resultado = insertion_sort(numeros)
print(resultado)  # Saída: [5, 6, 11, 12, 13]
