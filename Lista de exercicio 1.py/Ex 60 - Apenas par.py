# Implemente uma função filtra_pares(lista) que retorne uma lista apenas com os números pares.

def filtra_pares(lista):
    pares = []
    
    for numero in lista:
        # Se o número for par (resto da divisão por 2 igual a 0)
        if numero % 2 == 0:
            # Adiciona o número par à nova lista
            pares.append(numero)
    
    return pares

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtra_pares(lista_original)
print(resultado)
