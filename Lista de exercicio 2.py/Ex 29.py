#29.	Intervalo entre Elementos de uma Lista: Implemente uma 
# função intervalo_entre_elementos(lista) que calcula o intervalo (diferença) 
# entre o maior e o menor valor de uma lista.

def intervalo_entre_elementos(lista):
    if not lista:
        return 0
    return max(lista) - min(lista)
lista = [10, 20, 5, 30, 25]
resultado = intervalo_entre_elementos(lista)
print(resultado)  # Saída: 25
