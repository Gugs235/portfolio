while True:
    user = str(input("Escreva seu usuario: "))
    senha = str(input("Escreva sua senha: "))
    if senha == user:
        print("Senha invalida, tente novamente")
    else:
        print(f"Senha valida")
        print(f"BEM-VINDO {user}")
        break