# Escreva uma função alterna_maiusculas(texto) que alterne as letras para maiúsculas e minúsculas.

def alterna_maiusculas(texto):
    print(texto.upper())
    print(texto.casefold())

texto = str(input("Escreva um texto: "))
alterna_maiusculas(texto)
