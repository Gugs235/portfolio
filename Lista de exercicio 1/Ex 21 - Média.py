# Crie uma função media_lista(lista) que receba uma lista de números e retorne a média.

def media_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

numeros = [10, 20, 30, 40, 50]
resultado = media_lista(numeros)
print(f"A média dos números é: {resultado}")
