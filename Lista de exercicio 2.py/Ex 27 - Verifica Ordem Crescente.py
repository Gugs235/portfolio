#27.	Verifica Ordem Crescente: Crie uma função esta_ordenada(lista) que 
# verifica se uma lista está ordenada em ordem crescente.

def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 3, 2, 4, 5]

print(esta_ordenada(lista1))  # Saída: True
print(esta_ordenada(lista2))  # Saída: False
