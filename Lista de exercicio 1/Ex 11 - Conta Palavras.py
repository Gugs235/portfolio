def conta_palavras(texto):
    palavras = texto.split()
    return len(palavras)

texto = str(input("Escreva algum texto: "))
contagem = conta_palavras(texto)
print(f"O texto contém {contagem} palavras.")
