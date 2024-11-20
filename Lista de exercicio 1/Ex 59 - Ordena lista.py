# Crie uma função ordena_lista(lista) que retorne a lista ordenada em ordem crescente.

def ordena_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista = [5, 2, 9, 1, 5, 6]
lista_ordenada = ordena_lista(lista)
print(lista_ordenada)
