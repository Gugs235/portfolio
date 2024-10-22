cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0

while True:
    print("0 - Sair")
    print("1 - Jhonathan")
    print("2 - Cristian")
    print("3 - Reinaldo")
    print("4 - Arthur")
    print("5 - Voto nulo")
    print("6 - Voto em branco")
    voto = int(input("Qual é a sua escolha? "))

    if voto == 0:
        print("Encerrando...")
        break  # Adicionado para sair do loop
    elif voto == 1:
        print("Voto registrado")
        cont1 += 1
    elif voto == 2:
        print("Voto registrado")
        cont2 += 1
    elif voto == 3:
        print("Voto registrado")
        cont3 += 1
    elif voto == 4:
        print("Voto registrado")
        cont4 += 1
    elif voto == 5:
        print("Voto registrado")
        cont5 += 1
    elif voto == 6:
        print("Voto registrado")
        cont6 += 1
    else:
        print("Opção inválida. Tente novamente.")  # Para lidar com entradas inválidas

    total = cont1 + cont2 + cont3 + cont4 + cont5 + cont6
    print(f"O total de votos {total}")

    # Verifica se o total é maior que zero antes de calcular porcentagens
    if total > 0:
        print(f"O total de votos para Jhonathan é de {cont1}")
        porc1 = (cont1 / total) * 100
        print(f"A porcentagem de votos foi de {porc1:.2f}%")  # Formatado para 2 casas decimais

        print(f"O total de votos para Cristian é de {cont2}")
        porc2 = (cont2 / total) * 100
        print(f"A porcentagem de votos foi de {porc2:.2f}%")

        print(f"O total de votos para Reinaldo é de {cont3}")
        porc3 = (cont3 / total) * 100
        print(f"A porcentagem de votos foi de {porc3:.2f}%")

        print(f"O total de votos para Arthur é de {cont4}")
        porc4 = (cont4 / total) * 100
        print(f"A porcentagem de votos foi de {porc4:.2f}%")

        print(f"O total de votos para Voto nulo é de {cont5}")
        porc5 = (cont5 / total) * 100
        print(f"A porcentagem de votos foi de {porc5:.2f}%")

        print(f"O total de votos para Voto em branco é de {cont6}")
        porc6 = (cont6 / total) * 100
        print(f"A porcentagem de votos foi de {porc6:.2f}%")
    else:
        print("Nenhum voto registrado ainda.")
