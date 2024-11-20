from calculadora import Calculadora

def exibir_menu():
    print("\nCalculadora Simples")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

def main():
    calculadora = Calculadora()

    while True:
        exibir_menu()
        opcao = input("Escolha uma operação: ").strip()

        if opcao == "0":
            print("Encerrando o programa. Até mais!")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = calculadora.realizar_operacao("soma", num1, num2)
            elif opcao == "2":
                resultado = calculadora.realizar_operacao("subtracao", num1, num2)
            elif opcao == "3":
                resultado = calculadora.realizar_operacao("multiplicacao", num1, num2)
            elif opcao == "4":
                resultado = calculadora.realizar_operacao("divisao", num1, num2)

            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
