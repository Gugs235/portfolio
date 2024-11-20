# Crie uma função conta_ocorrencias(lista, elemento) que conta quantas vezes um elemento aparece em uma lista.

def conta_ocorrencias(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador
lista = [1, 2, 3, 4, 1, 1, 5, 1, 2, 2, 3, 5, 4, 7, 7, 9]
elemento = 1
resultado = conta_ocorrencias(lista, elemento)
print(resultado)
