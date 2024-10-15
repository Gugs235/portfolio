nota1 = float(input("Escreva sua nota 1: "))
nota2 = float(input("Escreva sua nota 2: "))
nota3 = float(input("Escreva sua nota 3: "))
nota4 = float(input("Escreva sua nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Sua nota foi de {media:.2f}")

if media == 10:
    print("APROVADO COM DISTINÇÃO")
elif media >= 7:
    print("APROVADO")
else:
    print("REPROVADO")
