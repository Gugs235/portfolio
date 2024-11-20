#2.	Produto de uma Lista: Escreva uma função produto_lista(lista) que calcula o 
# produto (multiplicação) de todos os elementos de uma lista.

def produto_lista(lista):
    produto = 1
    for elemento in lista:
        produto *= elemento
    return produto
numeros = [2, 3, 4]
resultado = produto_lista(numeros)
print(resultado)  # Saída: 24
