# Crie uma função substitui_texto_arquivo(nome_arquivo, palavra_antiga, palavra_nova) que substitua todas as ocorrências de uma 
# palavra em um arquivo por outra.

def substitui_texto_arquivo(nome_arquivo, palavra_antiga, palavra_nova):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    
    conteudo_modificado = conteudo.replace(palavra_antiga, palavra_nova)
    
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo_modificado)

substitui_texto_arquivo("meu_arquivo.txt", "antiga", "nova")
