#12. Listas Pares e Ímpares: Escreva uma função separa_pares_impares(lista) que 
# separa uma lista de números em duas listas: uma com os pares e outra com os ímpares.

def separa_pares_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares, impares = separa_pares_impares(numeros)
print("Pares:", pares)    # Saída: [2, 4, 6, 8]
print("Ímpares:", impares)  # Saída: [1, 3, 5, 7]
