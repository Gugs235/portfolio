#3.	Conta Consoantes: Implemente uma função conta_consoantes(texto) que conta o 
# número de consoantes em uma string.

def conta_consoantes(texto):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0
    for letra in texto:
        if letra in consoantes:
            contador += 1
    return contador
texto = "Olá, Mundo!"
resultado = conta_consoantes(texto)
print(resultado)  # Saída: 5
