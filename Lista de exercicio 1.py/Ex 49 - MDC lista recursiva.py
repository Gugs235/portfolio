# Escreva uma função mdc_lista(lista) que retorne o maior divisor comum entre os 
# números de uma lista.

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mdc_lista(lista):
    resultado = lista[0]
    for numero in lista[1:]:
        resultado = mdc(resultado, numero)
    return resultado

lista = [48, 64, 80]
print("O MDC da lista é:", mdc_lista(lista))
