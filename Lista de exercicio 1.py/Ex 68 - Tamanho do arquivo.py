# Implemente uma função tamanho_arquivo(nome_arquivo) que retorne o tamanho de 
# um arquivo em bytes.

def tamanho_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:  # Abre o arquivo em modo binário
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            return len(conteudo)  # Retorna o número de bytes no arquivo
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
        return -1  # Retorna -1 em caso de erro

nome_arquivo = "exemplo.txt"
tamanho = tamanho_arquivo(nome_arquivo)
if tamanho != -1:
    print(f"O tamanho do arquivo '{nome_arquivo}' é {tamanho} bytes.")
