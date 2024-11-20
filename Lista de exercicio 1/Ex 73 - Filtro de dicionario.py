# Implemente uma função filtro_dicionario(dic, valor) que retorne um novo 
# dicionário apenas com as chaves onde os valores são maiores que valor.

def filtro_dicionario(dic, valor):
    novo_dic = {}
    for chave in dic:
        if dic[chave] > valor:
            novo_dic[chave] = dic[chave]
    return novo_dic

dicionario = {'a': 5, 'b': 8, 'c': 2, 'd': 10}
valor_filtro = 6
dicionario_filtrado = filtro_dicionario(dicionario, valor_filtro)
print(dicionario_filtrado)
