# Restante do salario
nome = input ("Escreva seu nome: ")
print(nome)
sal = float(input('salario? = '))
print(sal)
imposto = float(input('Digite o imposto = '))
total = sal - imposto
print(f"Restou R$ {total:.2f} do seu salario")