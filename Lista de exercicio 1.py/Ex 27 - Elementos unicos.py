# Implemente uma função elementos_unicos(lista) que retorne uma lista com os elementos únicos.

def elementos_unicos(lista):
    unicos = set(lista)
    return list(unicos)

lista = [1, 7, 2, 6, 2, 3, 4, 4, 5]
print(elementos_unicos(lista))
