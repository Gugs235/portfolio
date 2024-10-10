# validador de senha
# se a senha for 1234 ele permitira senão ele negara
senha2 = 1234
resposta = int
estrato = float
estrato = 1000.00

senha = int(input("Escreva sua senha: "))

while resposta != 5 and senha == senha2:
        print("\n")
        if senha == senha2:
            print("ACESSO PERMITIDO")
            print("1 - Estrato")
            print("2 - Deposito")
            print("3 - Saque")
            print("4 - ADM")
            print("5 - Sair")
            resposta = int(input("O que você deseja? "))

            if resposta == 1:
                print(f"você tem R${estrato:.2f}")
                

            elif resposta == 2:
                deposito = float(input("Quantos reais você vai depositar? "))
                deposito2 = deposito + estrato
                print(f"você tem R${deposito2:.2f}")

            elif resposta == 3:
                saque = float(input("Quantos reais você vai sacar? "))
                sacar2 = estrato - saque
                print(f"você tem R${sacar2:.2f}")

            elif resposta == 4:
                print("1 - Cadastro")
                print("2 - Editar Cadastro")
                resposta2 = int(input("O que você deseja? "))
                if resposta2 == 1:
                    nome = str(input("Insira seu nome: "))
                    cpf = str(input("Insira seu cpf: "))
                    telefone = int(input("Incira seu telefone: "))
                    sexo = str(input("Insira seu sexo: "))

                elif resposta2 == 2:
                    print(f"o nome do usuario é: {nome}")
                    print(f"o cpf do usuario é: {cpf}")
                    print(f"o telefone do usuario é: {telefone}")
                    print(f"o sexo do usuario é: {sexo}")
                    nome = str(input("Insira o novo nome: "))
                    cpf = str(input("Insira o novo cpf: "))
                    telefone = int(input("Insira o novo telefone: "))
                    sexo = str(input("Insira o novo sexo: "))
                    print(f"o novo nome do usuario é: {nome}")
                    print(f"o novo cpf do usuario é: {cpf}")
                    print(f"o novo telefone do usuario é: {telefone}")
                    print(f"o novo sexo do usuario é: {sexo}")

            elif resposta == 5:
                print("Saindo...")

            else:
                print("RESPOSTA INVALIDA")

else:
    print("ACESSO BLOQUEADO")
