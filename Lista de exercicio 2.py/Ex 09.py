#9.	Ordenação com Quick Sort: Escreva uma função quick_sort(lista) que ordena uma 
# lista usando o algoritmo de Quick Sort (versão não recursiva).

def quick_sort(lista):
    pilha = [(0, len(lista) - 1)]

    while pilha:
        inicio, fim = pilha.pop()
        if inicio < fim:

            piv = particao(lista, inicio, fim)

            pilha.append((inicio, piv - 1))
            pilha.append((piv + 1, fim))
    return lista

def particao(lista, inicio, fim):
    piv = lista[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if lista[j] < piv:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1
numeros = [10, 7, 8, 9, 1, 5]
resultado = quick_sort(numeros)
print(resultado)  # Saída: [1, 5, 7, 8, 9, 10]
