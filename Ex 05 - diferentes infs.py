while True:
    nome = str(input("Digite seu nome: "))
    if len(nome) < 3:
        print("\n")
        print("nome invalido, tente novamente")
        continue
    else:
        break

while True:
    idade = int(input("Digite sua idade: "))
    if idade <= 0 or idade >= 150:
        print("\n")
        print("idade invalida, tente novamente")
        continue
    else:
        break

while True:
    salario = float(input("Digite seu salario: "))
    if salario <= 0:
        print("\n")
        print("salario invalido, tente novamente")
        continue
    else:
        break

while True:
    print("\n")
    print("f - feminino")
    print("m - masculino")
    print("o - outro")
    sexo = str(input("Digite seu sexo: "))
    if sexo == "F" or sexo == "M" or sexo == "O":
        print("\n")
        print("sexo invalido, tente novamente")
        continue
    else:
        break

while True:
    print("\n")
    print("s - solteiro")
    print("c - casado")
    print("v - viuvo")
    print("d - divorciado")
    civil = str(input("Digite seu estado civil: "))
    if civil == "S" or civil == "C" or civil == "V" or civil == "D":
        print("\n")
        print("sexo invalido, tente novamente")
        continue
    else:
        break
print("\nObrigado pelas informações (>°_°<)")

