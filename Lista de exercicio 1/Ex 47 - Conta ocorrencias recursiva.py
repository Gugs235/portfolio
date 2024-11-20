# Implemente uma função conta_ocorrencias_recursiva(lista, elem) que conte o número de
# ocorrências de um elemento em uma lista de forma recursiva.

def conta_ocorrencias_recursiva(lista, elem):
    if not lista:
        return 0
    elif lista[0] == elem:
        return 1 + conta_ocorrencias_recursiva(lista[1:], elem)
    else:
        return conta_ocorrencias_recursiva(lista[1:], elem)

lista = [1, 2, 3, 4, 2, 2, 5]
elemento = 2
resultado = conta_ocorrencias_recursiva(lista, elemento)
print(f"O elemento {elemento} ocorre {resultado} vezes na lista.")
