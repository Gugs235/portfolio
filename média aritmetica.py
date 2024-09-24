nome = str(input("Escreva seu nome: "))
idade = int(input("Escreva sua idade: "))
sexo = str(input("Você é masculino ou feminino? "))
nota1 = float(input("Qual é a sua nota um? "))
nota2 = float(input("Qual é a sua nota dois?? "))

media = (nota1 + nota2) / 2

print(f"{nome}, você tem {idade} de idade, você é {sexo}, e sua média foi {media:.2f}")