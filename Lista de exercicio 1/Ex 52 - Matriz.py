# Escreva uma função soma_diagonais(matriz) que retorne a soma dos elementos das 
# diagonais de uma matriz.

def soma_diagonais(matriz):
    n = len(matriz)
    soma = 0
    for i in range(n):
        soma += matriz[i][i]
        
        soma += matriz[i][n - i - 1]
    if n % 2 != 0:
        soma -= matriz[n // 2][n // 2]
    return soma

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
resultado = soma_diagonais(matriz)
print("Soma das diagonais:", resultado)
