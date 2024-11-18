#13.	Diferença Absoluta entre Elementos de Lista: Crie uma função 
# diferença_elementos_lista(lista) que retorna uma lista com a diferença 
# absoluta entre cada par consecutivo de elementos da lista original.

def diferenca_elementos_lista(lista):
    return [abs(lista[i] - lista[i + 1]) for i in range(len(lista) - 1)]
numeros = [10, 7, 3, 15]
resultado = diferenca_elementos_lista(numeros)
print(resultado)  # Saída: [3, 4, 12]
