# Escreva uma função conta_linhas(nome_arquivo) que retorne o número de linhas de um arquivo.

def conta_linhas(nome_arquivo):
    contador = 0
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            contador += 1
    return contador

nome_do_arquivo = "exemplo.txt"
numero_de_linhas = conta_linhas(nome_do_arquivo)
print(f"O arquivo '{nome_do_arquivo}' possui {numero_de_linhas} linhas.")
