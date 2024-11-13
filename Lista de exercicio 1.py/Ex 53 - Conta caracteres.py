# Implemente uma função conta_ocorrencias_caracteres(s) que retorne um dicionário 
# com a contagem de cada caractere em uma string.

def conta_ocorrencias_caracteres(s):
    contagem = {}
    
    for caractere in s:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    
    return contagem

texto = str(input("Digite um texto de exemplo: "))
resultado = conta_ocorrencias_caracteres(texto)
print(resultado)
