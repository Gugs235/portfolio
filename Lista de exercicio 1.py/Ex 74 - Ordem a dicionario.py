# Crie uma função ordena_por_valores(dic) que ordene um dicionário por seus valores e retorne o resultado.

def ordena_por_valores(dic):
    itens = list(dic.items())

    for i in range(len(itens)):
        for j in range(0, len(itens) - i - 1):
            # Compara os valores das tuplas (itens[j][1] e itens[j + 1][1])
            if itens[j][1] > itens[j + 1][1]:
                itens[j], itens[j + 1] = itens[j + 1], itens[j]

    # Converte a lista de tuplas de volta para um dicionário ordenado
    return {chave: valor for chave, valor in itens}

meu_dicionario = {'a': 3, 'b': 1, 'c': 2}
dicionario_ordenado = ordena_por_valores(meu_dicionario)
print(dicionario_ordenado)
