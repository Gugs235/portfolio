#15.	Multiplicação de Matrizes 2x2: Crie uma função 
# multiplica_matrizes(matriz1, matriz2) que recebe duas matrizes 2x2 e retorna o 
# resultado da multiplicação entre elas.

def multiplica_matrizes(matriz1, matriz2):
    if len(matriz1) != 2 or len(matriz2) != 2 or len(matriz1[0]) != 2 or len(matriz2[0]) != 2:
        raise ValueError("Ambas as matrizes devem ser 2x2")

    resultado = [
        [
            matriz1[0][0] * matriz2[0][0] + matriz1[0][1] * matriz2[1][0],
            matriz1[0][0] * matriz2[0][1] + matriz1[0][1] * matriz2[1][1]
        ],
        [
            matriz1[1][0] * matriz2[0][0] + matriz1[1][1] * matriz2[1][0],
            matriz1[1][0] * matriz2[0][1] + matriz1[1][1] * matriz2[1][1] 
        ]
    ]
    return resultado
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplica_matrizes(matriz1, matriz2)
print(resultado)
# Saída: [[19, 22], [43, 50]]
