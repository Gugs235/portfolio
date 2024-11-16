#16.	Busca Binária: Implemente uma função busca_binaria(lista, elemento) que 
# realiza uma busca binária em uma lista ordenada e retorna o índice do 
# elemento, ou -1 se não for encontrado.

def busca_binaria(lista, elemento):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1
lista = [1, 3, 5, 7, 9, 11, 13, 15]
elemento = 7
resultado = busca_binaria(lista, elemento)
print(resultado)  # Saída: 3 (índice do elemento 7)
