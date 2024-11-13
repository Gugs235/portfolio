# Escreva uma função conta_maiusculas(texto) que conta o número de letras maiúsculas 
# em um texto.

def conta_maiusculas(texto):
    count = 0
    for char in texto:
        if 'A' <= char <= 'Z':
            count += 1
    return count

texto = str(input("Digite um texto de exemplo: "))
resultado = conta_maiusculas(texto)
print(f"Número de maiúsculas: {resultado}")
