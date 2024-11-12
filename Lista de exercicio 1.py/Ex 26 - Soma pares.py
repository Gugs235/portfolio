# Crie uma função soma_pares(lista) que retorne a soma de todos os números pares em uma lista.

def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

numeros = [1, 2, 3, 4, 5, 6, 5, 2, 8, 9, 7, 0]
resultado = soma_pares(numeros)
print(resultado)

