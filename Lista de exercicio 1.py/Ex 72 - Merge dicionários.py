# Escreva uma função merge_dicionarios(d1, d2) que una dois dicionários, 
# somando os valores das chaves iguais.

def merge_dicionarios(d1, d2):
    resultado = d1.copy()

    for chave, valor in d2.items():
        if chave in resultado:
            resultado[chave] += valor
        else:
            resultado[chave] = valor

    return resultado

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 3, 'b': 1, 'd': 4}

dicionario_unido = merge_dicionarios(d1, d2)
print(dicionario_unido)
