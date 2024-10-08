# validador de senha
# se a senha for 1234 ele permitira senão ele negara
senha2 = 1234
senha = int(input("Escreva sua senha: "))


if senha == senha2:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")
