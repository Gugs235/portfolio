# 19. Crie uma função apaga_vogais(s) que remova todas as vogais de uma string.

def apaga_vogais(s):
    vogais = "aeiouAEIOU"
    
    return ''.join([char for char in s if char not in vogais])

texto = str(input("Escreva um texto: "))
resultado = apaga_vogais(texto)
print(resultado)
