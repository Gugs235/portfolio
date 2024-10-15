# recebe o salario
salario = float(input("Digite o seu salário: "))

# criterios para o reajuste 
if salario <= 280.00:
    porc = 20
    reaju = salario + (salario * 0.20)
    dif = reaju - salario

elif salario > 280.00 and salario < 700.00:
    porc = 15
    reaju = salario + (salario * 0.15)
    dif = reaju - salario

elif salario >= 700.00 and salario < 1500.00:
    porc = 10
    reaju = salario + (salario * 0.10)
    dif = reaju - salario

else:
    porc = 5
    reaju = salario + (salario * 0.05)
    dif = reaju - salario

# informe o salario antes do reajuste
print(f"O salário digitado foi de: {salario:.2f}")

# o percentual de aumento aplicado
print(f"O percentual do reajuste é de: {porc:.2f}%")

# o valor do aumento
print(f"O valor do aumento será de: {dif:.2f}")

# o novo salario após o aumento
print(f"O novo salário será de: {reaju:.2f}")