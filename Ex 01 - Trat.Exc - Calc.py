resposta = 0  # Inicializar com 0 para entrar no loop

while resposta != 5:
    print("\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    try:
        resposta = int(input("O que você deseja? "))
    except ValueError: # Erro de valor, (a variavel é inteira mas escrevo strings)
        print("Digite apenas números")
    except:
        print("Erro desconhecido")

    
    if resposta == 1:
        print("Soma foi escolhida")
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print(f"O resultado foi de {resultado}")
        except ValueError: # Erro de valor, (a variavel é inteira mas escrevo strings)
            print("Digite apenas números")
        except:
            print("Erro desconhecido")
    
    elif resposta == 2:
        print("Subtração foi escolhida")
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print(f"O resultado foi de {resultado}")
        except ValueError: # Erro de valor, (a variavel é inteira mas escrevo strings)
            print("Digite apenas números")
        except:
            print("Erro desconhecido")

    
    elif resposta == 3:
        print("Multiplicação foi escolhida")
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 * num2
            print(f"O resultado foi de {resultado}")
        except ValueError: # Erro de valor, (a variavel é inteira mas escrevo strings)
            print("Digite apenas números")
        except:
            print("Erro desconhecido")

    
    elif resposta == 4:
        print("Divisão foi escolhida")
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 / num2
        except ZeroDivisionError:
            print("Não é possivel fazer divisão com 0")
        
        except ValueError: # Erro de valor, (a variavel é inteira mas escrevo strings)
            print("Digite apenas números")
        except:
            print("Erro desconhecido")
        else:
            print(f"O resultado foi de {resultado}")

    
    elif resposta == 5:
        print("Saindo...")
    
    else:
        print("Opção inválida")
        
print("Desconectado")
