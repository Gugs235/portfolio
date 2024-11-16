#18.	Média Ponderada: Escreva uma função media_ponderada(lista_valores, lista_pesos) 
# que calcula a média ponderada de uma lista de valores com uma lista de pesos 
# correspondente.

def media_ponderada(lista_valores, lista_pesos):
    if len(lista_valores) != len(lista_pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")

    soma_valores_pesos = sum(valor * peso for valor, peso in zip(lista_valores, lista_pesos))
    soma_pesos = sum(lista_pesos)

    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")

    return soma_valores_pesos / soma_pesos
valores = [10, 8, 7, 9]
pesos = [2, 1, 3, 4]
resultado = media_ponderada(valores, pesos)
print(resultado)  # Saída: 8.25
