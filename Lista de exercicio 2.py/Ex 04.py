#4.	Concatenação de Listas: Crie uma função concatena_listas(lista1, lista2) que 
# recebe duas listas e retorna uma nova lista com os elementos de ambas as listas 
# concatenados.

def concatena_listas(lista1, lista2):
    return lista1 + lista2
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
resultado = concatena_listas(lista1, lista2)
print(resultado)  # Saída: [1, 2, 3, 4, 5, 6]
