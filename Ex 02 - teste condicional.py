# checa sua idade e te fala se você pode ou não votar
idade = int(input("Digite seu ano de nascimento: " ))
ano = int(input("Em que ano estamos? "))

a = ano - idade

if a >= 16:
    print(f"Você tem {a} anos de idade \nEntão parabéns, você cresceu e agora pode votar ")
else:
    print(f"Você ainda tem {a} ano de idade e não podera votar \nMas parabéns, você ainda é jovem então continue estudando ")
