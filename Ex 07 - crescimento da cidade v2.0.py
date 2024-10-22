a = int(input("Escreva o número da população do país A: "))
porc1 = float(input("Escreva a porcentagem em decimal do crescimento da população do país A: "))
b = int(input("Escreva o número da população do país B: "))
porc2 = float(input("Escreva a porcentagem em decimal do crescimento da população do país B: "))
cont = 0

while a <= b:
    a += int(a * porc1)  # Crescimento de 3% da população A (mantendo o número inteiro)
    b += int(b * porc2)  # Crescimento de 1.5% da população B (mantendo o número inteiro)
    cont += 1

print(f"População de A: {a}")
print(f"População de B: {b}")
print(f"Para A passar B vai precisar de {cont} anos")
