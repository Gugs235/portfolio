import os

class Conta():
    def __init__(self, nome, saldo, cpf, senha):
        self.nome = nome # publico
        self.__saldo = saldo # privado
        self.__cpf = cpf # privado
        self.__senha = senha # privado

    def extrato(self, senha):
        if senha == self.__senha:
            print(f"Seu saldo é: {self.__saldo}")
        else:
            print("Senha inválida")

    def depositar(self, senha, valor):
        if senha == self.__senha:
            self.__saldo += valor
            print(f"Seu saldo é: {self.__saldo}")
        else:
            print("Senha inválida")

    def sacar(self, senha, valor):
        if senha == self.__senha:
            self.__saldo -= valor
        else:
            print("Senha inválida")

while True:
    os.system('cls')
    print("PAGINA INICIAL")
    print("\n1 - Entrar/Cadastro")
    print("2 - Saque/Tirar")
    print("3 - Saldo/Estrato")
    print("4 - Deposito/Colocar")
    print("0 - Desligar")
    valor = 0
    opc = int(input("Digite o código do que você deseja: "))
    
    if opc == 1: # Entrar/Cadastro
        os.system('cls')
        print("1 - Entrar/Cadastro")
        cliente = input("\ndigite seu nome: ")
        cpf = input("digite seu cpf: ")
        senha = input("digite sua senha: ")
        saldo = float(input("digite seu saldo: "))
        conta = Conta(cliente, saldo, cpf, senha)
    
    elif opc == 2: # Saque/Tirar
        os.system('cls')
        print("2 - Saque/Tirar")
        senha = input("\ndigite sua senha: ")
        valor = float(input("digite seu valor: "))
        conta.sacar(senha, valor)
        print("Cadastro concluido")

    elif opc == 3: # Saldo/Estrato
        os.system('cls')
        print("3 - Saldo/Estrato")
        print("\n")
        senha = input("\ndigite sua senha: ")
        conta.extrato(senha)

    elif opc == 4: # Deposito/Colocar
        os.system('cls')
        print("4 - Deposito/Colocar")
        print("\n")
        senha = input("\ndigite sua senha: ")
        valor = float(input("digite seu valor: "))
        conta.depositar(senha,valor)

    elif opc == 0: # Desligar
        os.system('cls')
        print("0 - Desligar")
        print("Desliganto...")
        break

    else:
        os.system('cls')
        print("Código invalido")
