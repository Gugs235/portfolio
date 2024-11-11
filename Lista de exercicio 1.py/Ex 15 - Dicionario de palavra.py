# 15. Escreva uma função ocorrencias_palavras(texto) que retorne um dicionário com a contagem de cada palavra em um texto.

def ocorrencias_palavras(texto):
    texto = texto.lower()

    texto = ''.join(caracter for caracter in texto if caracter.isalnum() or caracter.isspace())

    palavras = texto.split()

    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    
    return contagem

texto = str(input("Escreva um texto: "))
resultado = ocorrencias_palavras(texto)
print(resultado)
