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
