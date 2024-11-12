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
