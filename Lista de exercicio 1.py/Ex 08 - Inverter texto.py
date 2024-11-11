def inverte(nome):
    nomeInverso = nome [::-1]
    return nomeInverso
nome = input("Nome: ")
invertido = inverte(nome)
print("Olá,", invertido)
