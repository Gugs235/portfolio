# Implemente uma função substitui_espaco(texto, simbolo) que substitua todos os 
# espaços em uma string por um símbolo específico.

def substitui_espaco(texto, simbolo):
    texto_modificado = ""
    
    for caractere in texto:
        if caractere == " ":
            texto_modificado += simbolo
        else:
            texto_modificado += caractere
    
    return texto_modificado

texto_original = str(input("Digite um texto de exemplo: "))
simbolo = str(input("Digite o simbolo: "))
texto_resultado = substitui_espaco(texto_original, simbolo)
print(texto_resultado)
