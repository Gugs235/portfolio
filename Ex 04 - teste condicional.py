# se a quantidade de fruta for uma é um valor
# se for outra quantidade é outro valor

quant = float(input("Quantas maçãs você comprou? "))
if quant < 12:
    frut = quant * 0.30
    print(f"O valor total das suas frutas sera de R$ {frut:.2f}")
elif quant >= 12:
    frut = quant * 0.25
    print(f"O valor total das suas frutas sera de R$ {frut:.2f}")
