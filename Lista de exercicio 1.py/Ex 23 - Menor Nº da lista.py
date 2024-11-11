# Implemente uma função menor_elemento(lista) que retorne o menor número de uma lista.

def menor_elemento(lista):
    if not lista:
        return None
    return min(lista)

numeros = [3, 5, 7, 2, 8]
print(menor_elemento(numeros))
