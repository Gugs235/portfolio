# Escreva uma função remove_duplicados(lista) que retorne uma lista sem elementos duplicados.

def remove_duplicados(lista):
    return list(set(lista))

lista = [2, 1, 2, 3, 2, 4, 1, 5, 5, 3, 2, 6, 8, 8, 5, 4]
lista_sem_duplicados = remove_duplicados(lista)
print(lista_sem_duplicados)
