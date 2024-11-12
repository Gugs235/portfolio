# Função len (conta quantas letras tem na variavel)
a = "Chocolate azedo"
print("Função len")
print(a)
print(len(a))

# Função capitalize - capitalizar (transforma a primeira letra da primeira palavra em maiúscula)
a = "chocolate azedo"
print("\nFunção capitalize")
print(a)
print(a.capitalize())

# Função upper (transforma todo o texto em MAIUSCULO)
a = "chocolate azedo"
print("\nFunção upper")
print(a)
print(a.upper())

# Função casefold (transforma todo o texto em minusculo)
a = "ChOcOlAtE aZeDo"
print("\nFunção casefold")
print(a)
print(a.casefold())

# Função lower (transforma todo o texto em minusculo)
a = "ChOcOlAtE aZeDo"
print("\nFunção lower")
print(a)
print(a.lower())

# Função islower (identifica se todo o texto esta em minusculo)
a = "ChOcOlAtE aZeDo"
print("\nFunção islower")
print(a)
print(a.islower())
a = "chocolate azedo"
print(a)
print(a.islower())

# Função isupper (identifica se todo o texto esta em MAIUSCULO)
a = "ChOcOlAtE aZeDo"
print("\nFunção isupper")
print(a)
print(a.isupper())
a = "CHOCOLATE AZEDO"
print(a)
print(a.isupper())

# Função replace (serve para trocar todas as ocorrencias de uma string por outra em uma string)
a = "Chocolate Azedo"
print("\nFunção replace")
print(a)
print(a.replace("Chocolate" , "Abacate"))

# Função split (separa uma string usando sep como separador)
a = "Abacate-Azedo-com-Chocolate-que-vira-Maracuja"
print("\nFunção split")
print(a)
print(a.split("-"))

# Função find (retorna onde a substring começa na string ("Primeira"))
a = "Abacate-Azedo-com-Chocolate-que-vira-Maracuja"
print("\nFunção find")
print(a)
print(a.find("Chocolate"))

# Função in (verifica se uma substring é parte de uma outra string)
a = "Abacate Azedo com Chocolate"
print("\nFunção in")
print(a)
print("tem a palavra azedo? " , "Azedo" in a)
print(a)
print("tem a palavra maracuja? " , "maracuja" in a)

# Função count (mostra o número de letras ou palavras)
a = "abacate"
print("\nFunção count")
print(a)
print(a.count("b"))

# Substring - direita (Pega as letras conforme os números q eu escrevo)
a = "Abacate Azedo"
print("\nFunção Substring")
print("Abacate Azedo")
print(a[5])
print(a[0])
print(a[2])

# Substring - Esquerda (Pega as letras conforme os números q eu escrevo)
a = "Abacate Azedo"
print("\nFunção Substring")
print("Abacate Azedo")
print(a[-5])
print(a[-0])
print(a[-2])

# Substring - Pegar "Fatias" (Pega as letras formandop uma "fatia" conforme os números q escrevo)
a = "Abacate Azedo"
print("\nFunção Substring")
print("Abacate Azedo")
print(a[3:7])

