# Escreva uma função inverte_dicionario(dic) que inverta as chaves e valores de um dicionário.

def inverte_dicionario(dic):
    dic_invertido = {}
    for chave, valor in dic.items():
        dic_invertido[valor] = chave
    return dic_invertido

dicionario = {
    "a": 1,
    "b": 2,
    "c": 3
}
dicionario_invertido = inverte_dicionario(dicionario)
print(f"Antes {dicionario}")
print(f"Depois {dicionario_invertido}")
