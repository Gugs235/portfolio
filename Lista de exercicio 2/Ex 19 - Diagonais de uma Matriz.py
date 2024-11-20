#19.	Diagonais de uma Matriz: Implemente uma função diagonais_matriz(matriz) que 
# recebe uma matriz quadrada e retorna uma lista contendo os elementos das duas diagonais.

def diagonais_matriz(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("A matriz deve ser quadrada.")

    diagonal_principal = []
    diagonal_secundaria = []
    n = len(matriz)

    for i in range(n):
        diagonal_principal.append(matriz[i][i])
        diagonal_secundaria.append(matriz[i][n-i-1])

    return diagonal_principal, diagonal_secundaria
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonais = diagonais_matriz(matriz)
print(diagonais)  # Saída: ([1, 5, 9], [3, 5, 7])
