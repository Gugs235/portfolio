print("G - Gasolina")
print("A - Álcool")
resp = str(input("digite o que você deseja? "))

if resp == "G":
    print("Sua escolha foi gasolina")
    litros = float(input("Quantos litros você deseja? "))
    
    preco = litros * 2.50

    if litros <= 20:
        desc = preco * 0.03
        final = preco - desc
    elif litros > 20:
        desc = preco * 0.05
        final = preco - desc
    print(litros)
    print(final)


elif resp == "A":
    print("Sua escolha foi álcool")
    litros = float(input("Quantos litros você deseja? "))
