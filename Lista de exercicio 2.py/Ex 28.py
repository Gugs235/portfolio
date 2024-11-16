#28.	Remove Múltiplos de um Número: Escreva uma função remove_multiplos(lista, n) 
# que remove todos os múltiplos de n de uma lista.

def remove_multiplos(lista, n):
    return [x for x in lista if x % n != 0]
lista = [10, 15, 20, 25, 30, 35]
n = 5
resultado = remove_multiplos(lista, n)
print(resultado)  # Saída: [25, 35]
