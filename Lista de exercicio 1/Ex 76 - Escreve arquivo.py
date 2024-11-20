# Implemente uma função escreve_arquivo(nome_arquivo, texto) que crie um arquivo com um texto.

def escreve_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(texto)

escreve_arquivo("meu_arquivo.txt", "Este é o conteúdo do arquivo.")
