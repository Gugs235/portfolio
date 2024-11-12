# Crie uma função média_harmonica(lista) que calcula a média harmônica de uma lista de números.

def media_harmonica(lista):
    if len(lista) == 0:
        return 0

    soma_inversos = 0
    for numero in lista:
        if numero == 0:
            return 0
        soma_inversos += 1 / numero
    
    n = len(lista)
    return n / soma_inversos

lista = [1, 2, 4]
resultado = media_harmonica(lista)
print(f"A média harmônica da lista é: {resultado}")
