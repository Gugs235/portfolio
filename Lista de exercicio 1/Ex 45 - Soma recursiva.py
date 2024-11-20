# Crie uma função somatorio_lista_recursivo(lista) que retorne a soma dos elementos de uma lista recursivamente.

def somatorio_lista_recursivo(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somatorio_lista_recursivo(lista[1:])

lista = [1, 2, 3, 4, 5]
resultado = somatorio_lista_recursivo(lista)
print(resultado)  # Saída: 15
