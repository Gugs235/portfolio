produto = str(input("Digite o nome do produto: "))
quantidade = int(input("Qual é a quantidade? "))
valor = float(input("Quanto custa? "))
desconto = float(input("Qual é o valor do desconto? "))

valor = quantidade * valor
desconto = valor * (desconto / 100)
total = valor - desconto

print(f"O valor pago sera de {total:.2f}")