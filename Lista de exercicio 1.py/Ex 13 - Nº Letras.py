def conta_letras(s, letra):
    return s.count(letra)

texto = str(input("Escreva um texto: "))
letra = str(input("Escolha uma letra: "))
resultado = conta_letras(texto, letra)
print(f"A letra '{letra}' aparece {resultado} vezes na string.")
