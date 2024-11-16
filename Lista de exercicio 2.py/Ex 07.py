#7.	Ordenação com Selection Sort: Crie uma função selection_sort(lista) que ordena 
# uma lista usando o algoritmo de Selection Sort.

def selection_sort(lista):
    n = len(lista)
    for i in range(n):

        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
numeros = [64, 25, 12, 22, 11]
resultado = selection_sort(numeros)
print(resultado)  # Saída: [11, 12, 22, 25, 64]
