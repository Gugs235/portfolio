# Crie uma função capitaliza_palavras(texto) que capitaliza a primeira letra de cada palavra em um texto.

def capitaliza_palavras(texto):
    return texto.title()

texto = str(input("Escreva um texto: "))
texto_capitalizado = capitaliza_palavras(texto)
print(texto_capitalizado)
