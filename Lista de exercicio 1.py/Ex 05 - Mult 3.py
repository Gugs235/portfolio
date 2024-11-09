def mult_tres_numeros(a,b,c):
    d = a * b  * c
    return d
a = int(input("Escreva o primeiro número: "))
b = int(input("Escreva o segundo número: "))
c = int(input("Escreva o terceiro número: "))
res = mult_tres_numeros(a,b,c)
print(f"A resposta da soma é {res}")
