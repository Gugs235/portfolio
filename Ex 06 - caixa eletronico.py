# validador de senha
# se a senha for 1234 ele permitira senão ele negara
senha2 = 1234
resposta = int
estrato = float
estrato = 1000.00

senha = int(input("Escreva sua senha: "))

while resposta != 4 and senha == senha2:
        print("\n")
        if senha == senha2:
            print("ACESSO PERMITIDO")
            print("1 - Estrato")
            print("2 - Deposito")
            print("3 - Saque")
            print("4 - Sair")
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
                print("Obrigado por entrar, tenha um bom dia :-)")
            
            else:
                print("RESPOSTA INVALIDA")

else:
    print("ACESSO BLOQUEADO")
    