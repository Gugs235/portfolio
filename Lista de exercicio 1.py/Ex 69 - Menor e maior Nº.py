# Escreva uma função minimax(lista) que retorne o menor e o maior número de uma lista.

def minimax(lista):
    if len(lista) == 0:
        return None, None

    menor = maior = lista[0]

    for num in lista[1:]:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

    return menor, maior

lista = [10, 5, 20, 8, 15]
menor, maior = minimax(lista)
print(f"Menor número: {menor}, Maior número: {maior}")
