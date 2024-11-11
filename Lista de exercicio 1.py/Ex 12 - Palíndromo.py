def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    texto_invertido = s[::-1]
    if s == texto_invertido:
        return True
    else:
        return False
texto = str(input("Digite um texto para verificar se é palíndromo: "))
if eh_palindromo(texto):
    print("O texto é um palíndromo!")
else:
    print("O texto não é um palíndromo.")
