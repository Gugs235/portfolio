from veiculo import Carro, Moto, Caminhao


def cadastrar_veiculos():
    veiculos = []

    while True:
        print("\n--- Cadastro de Veículos ---")
        print("1. Carro")
        print("2. Moto")
        print("3. Caminhão")
        print("4. Exibir veículos cadastrados e sair")
        opcao = input("Escolha o tipo de veículo para cadastrar: ")

        if opcao == "4":
            break

        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")

        if opcao == "1":
            veiculos.append(Carro(marca, modelo))
        elif opcao == "2":
            veiculos.append(Moto(marca, modelo))
        elif opcao == "3":
            veiculos.append(Caminhao(marca, modelo))
        else:
            print("Opção inválida. Tente novamente.")

    return veiculos


def exibir_veiculos(veiculos):
    print("\n--- Veículos Cadastrados ---")
    if not veiculos:
        print("Nenhum veículo cadastrado.")
    for veiculo in veiculos:
        print(f"\nMarca: {veiculo.marca}")
        print(f"Modelo: {veiculo.modelo}")
        print(f"Tipo de Combustível: {veiculo.tipo_combustivel()}")
        print(f"Capacidade de Passageiros: {veiculo.capacidade_passageiros()}")
        print("-" * 40)
