import os
os.system('cls')

nome = str(input("Escreva seu nome: "))
cpf = str(input("Escreva seu cpf: "))
rg = str(input("Escreva seu rg: "))
nascimento = str(input("Escreva sua data de nascimento: "))
sexo = str(input("Escreva seu sexo: "))
peso = float(input("Escreva seu peso: "))
sangue = str(input("Escreva seu tipo sanguíneo: "))
renda = float(input("Escreva seu renda: "))
endereco = str(input("Escreva seu endereço: "))
telefone = int(input("Escreva seu telefone: "))
cidade = str(input("Escreva seu cidade: "))
estado = str(input("Escreva seu estado: "))

os.system('cls')

print(f"\nSeu nome é: {nome}")
print(f"Seu cpf é: {cpf}")
print(f"Seu rg é: {rg}")
print(f"Sua data de nascimento é: {nascimento}")
print(f"Seu sexo é: {sexo}")
print(f"Seu peso é: {peso}")
print(f"Seu tipo sanguíneo é: {sangue}")
print(f"Sua renda é: {renda}")
print(f"Seu endereço é: {endereco}")
print(f"Seu telefone é: {telefone}")
print(f"Sua cidade é: {cidade}")
print(f"Seu estado é: {estado}")
