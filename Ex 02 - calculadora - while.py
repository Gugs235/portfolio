resposta = 0  # Inicializar com 0 para entrar no loop

while resposta != 5:
    print("\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    resposta = int(input("O que você deseja? "))
    
    if resposta == 1:
        print("Soma foi escolhida")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado foi de {resultado}")
    
    elif resposta == 2:
        print("Subtração foi escolhida")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado foi de {resultado}")
    
    elif resposta == 3:
        print("Multiplicação foi escolhida")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado foi de {resultado}")
    
    elif resposta == 4:
        print("Divisão foi escolhida")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado foi de {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    
    elif resposta == 5:
        print("Saindo...")
    
    else:
        print("Opção inválida")
        
print("Desconectado")
