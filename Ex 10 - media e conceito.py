# recebe a nota
nota1 = float(input("Escreva sua nota 1: "))
nota2 = float(input("Escreva sua nota 2: "))
nota3 = float(input("Escreva sua nota 3: "))
nota4 = float(input("Escreva sua nota 4: "))

# media
media = (nota1 + nota2 + nota3 + nota4) / 4
conc = str

# critérios para o reajuste 
if media >= 9.1 and media <= 10.0:
    conc = "A"
elif media >= 7.6 and media < 9.1:
    conc = "B"
elif media >= 6 and media < 7.6:
    conc = "C"
elif media >= 4.1 and media < 6:
    conc = "D"
else:
    conc = "E"

# mostrar as notas
print(f"A nota 1 foi {nota1}")
print(f"A nota 2 foi {nota2}")
print(f"A nota 3 foi {nota3}")
print(f"A nota 4 foi {nota4}")

# mostrar a média
print(f"A média foi {media:.2f}")

# o conceito correspondente
print(f"O conceito foi de {conc}")

# mensagem
if conc == "A" or conc == "B" or conc == "C":
    print("APROVADO!!")
else:
    print("REPROVADO")
