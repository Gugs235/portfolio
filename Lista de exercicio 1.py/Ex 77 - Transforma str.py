# Crie uma função le_arquivo(nome_arquivo) que leia o conteúdo de um arquivo e retorne uma string.

def le_arquivo(nome_arquivo):
    conteudo = ""
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

nome_arquivo = "exemplo.txt"
conteudo = le_arquivo(nome_arquivo)
print(conteudo)
