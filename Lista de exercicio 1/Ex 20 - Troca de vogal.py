# Implemente uma função troca_vogais(s, nova_letra) que substitua todas as vogais de uma string por uma nova letra.

def troca_vogais(s, nova_letra):
    vogais = "aeiouAEIOU"
    
    resultado = "".join([nova_letra if char in vogais else char for char in s])
    
    return resultado

texto = str(input("Escreva um texto: "))
nova_letra = "P"
texto_modificado = troca_vogais(texto, nova_letra)
print(texto_modificado)
