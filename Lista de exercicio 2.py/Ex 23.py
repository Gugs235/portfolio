#23.	Multiplicação de Valores Pares: Implemente uma função 
# multiplica_pares(lista) que multiplica todos os números pares em uma lista.

def multiplica_pares(lista):
    resultado = 1
    encontrou_par = False

    for numero in lista:
        if numero % 2 == 0:
            resultado *= numero
            encontrou_par = True

    if not encontrou_par:
        return 0

    return resultado
lista = [1, 2, 3, 4, 5, 6]
resultado = multiplica_pares(lista)
print(resultado)  # Saída: 48 (2 * 4 * 6)
