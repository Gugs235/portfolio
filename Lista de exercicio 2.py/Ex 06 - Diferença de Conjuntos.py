#6.	Diferença de Conjuntos: Implemente uma função diferenca_conjuntos(lista1, lista2) 
# que retorna os elementos presentes em lista1 que não estão em lista2.

def diferenca_conjuntos(lista1, lista2):
    return [elemento for elemento in lista1 if elemento not in lista2]
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
resultado = diferenca_conjuntos(lista1, lista2)
print(resultado)  # Saída: [1, 2]
