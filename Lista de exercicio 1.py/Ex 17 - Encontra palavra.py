# Implemente uma função encontra_palavra(texto, palavra) que retorne o índice da primeira ocorrência de uma palavra em uma string.


def encontra_palavra(texto, palavra):
    return texto.find(palavra)

texto = str(input("Escreva um texto: "))
palavra = str(input("Escreva a palavra para procurar: "))
indice = encontra_palavra(texto, palavra)
print(indice)
