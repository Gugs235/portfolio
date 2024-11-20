# Escreva uma função maior_elemento(lista) que retorne o maior número de uma lista.

def maior_elemento(lista):
    if not lista:
        return None
    return max(lista)

numeros = [3, 5, 7, 2, 8]
print(maior_elemento(numeros))
