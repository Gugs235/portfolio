# Implemente uma função conta_palavras_arquivo(nome_arquivo) que retorne o número total de palavras em um arquivo.

def conta_palavras_arquivo(nome_arquivo):
    total_palavras = 0
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                palavras = linha.split()
                total_palavras += len(palavras)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    
    return total_palavras
