# Crie uma função bubblesort(lista) que ordene uma lista usando o algoritmo Bubble Sort.

def bubblesort(lista):
    n = len(lista)
    
    for i in range(n):
        trocou = False
        
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        # Se não houve troca, a lista já está ordenada, então podemos parar
        if not trocou:
            break
    
    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = bubblesort(lista)
print("Lista ordenada:", lista_ordenada)
