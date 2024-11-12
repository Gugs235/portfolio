# Escreva uma função mediana(lista) que retorne a mediana de uma lista de números.

def mediana(lista):
    lista.sort()

    n = len(lista)
    if n % 2 == 1:
        return lista[n // 2]
    else:
        meio_esquerdo = lista[(n // 2) - 1]
        meio_direito = lista[n // 2]
        return (meio_esquerdo + meio_direito) / 2

numeros = [3, 1, 2, 5, 4]
print("Mediana:", mediana(numeros))  # Resultado: 3

numeros = [1, 2, 3, 4]
print("Mediana:", mediana(numeros))  # Resultado: 2.5
