# Implemente uma função uniao_listas(lista1, lista2) que retorne a união de duas listas.

def uniao_listas(lista1, lista2):
    return list(set(lista1) | set(lista2))

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
resultado = uniao_listas(lista1, lista2)
print("União das listas:", resultado)
