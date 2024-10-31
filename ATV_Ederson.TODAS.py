# 10)
h=int(input("digite a altura da torre:"))
d=int(input("digite a distancia da torre com a ponta do cabo:"))

h = h * h
d = d * d
x = h + d 
x = x**(1/2)

print (x)



# 03)
while True:
    vermelho = int(input("Escreva o primeiro número: "))
    amarelo = int(input("Escreva o segundo número: "))
    verde = int(input("Escreva o terceiro número: "))

    if vermelho == 1 and amarelo == 0 and verde == 0:
        print("Vermelho ON")
        print("Status: 1 0 0")

    elif vermelho == 0 and amarelo == 1 and verde == 0:
        print("Amarelo ON")
        print("Status: 0 1 0")

    elif vermelho == 0 and amarelo == 0 and verde == 1:
        print("Verde ON")
        print("Status: 0 0 1")

    elif vermelho == 0 and amarelo == 0 and verde == 0:
        print("Desligado!!!")
        print("Status: 0 0 0")


    else:
        print("Invalido")




# 08)
while True:
    total = 0
    print("\n========= Compra dos produtos =========")
    
    while True:
        nome = str(input("Nome do produto (ou digite '0' para encerrar ou ir para o caixa): "))
        
        if nome == '0':
            break
        
        preco = float(input("Preço do produto: "))
        
        total += preco
        print(f"Total parcial: R${total:.2f}")
    
    if total == 0:
        print("Nenhum produto foi adicionado. Encerrando compra.")
        break

    while True:
        print("\n========= Caixa registradora ==========")
        print(f"Total da compra é de R${total:.2f}")
        dinheiro = float(input("Quanto você vai pagar? "))
        
        if dinheiro >= total:
            troco = dinheiro - total
            print(f"Compra realizada com sucesso! Seu troco: R${troco:.2f}")
            break
        else:
            print("Dinheiro insuficiente. Tente novamente.")
    
    # Pergunta se o usuário deseja realizar outra compra
    nova_compra = input("Deseja realizar outra compra? (s/n): ").lower()
    
    if nova_compra != 's':
        print("Encerrando o programa.")
        break




