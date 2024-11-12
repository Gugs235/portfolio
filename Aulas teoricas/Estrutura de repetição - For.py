# for = para 
# for "item" in "sequencia":
    # bloco de código a ser executado
print("\nTeste 1")
nomes = ["Pedro" , "Jhonathan", "Cristian", "Arthur"]
for n in nomes:
    print(n)

print("\nTeste 2")
nome = "Jhonathan"
for m in nome:
    print(m)

# break = parar (vai mostrar o cristian e parar nele)
print("\nBreak - imprimir")
nomes = ["Pedro" , "Jhonathan", "Cristian", "Arthur"]
for n in nomes:
    print(n)
    if n == "Cristian":
        break

# eu não quero impimir o cristian
print("\nbreak - não imprir")
nomes = ["Pedro" , "Jhonathan", "Cristian", "Arthur"]
for n in nomes:
    if n == "Cristian":
        break
    print(n)

# continue (a forma q esta vai pular o cristian)
print("\nContinue")
nomes = ["Pedro" , "Jhonathan", "Cristian", "Arthur"]
for n in nomes:
    if n == "Cristian":
        continue
    print(n)

# range - repete o tanto de vezes determinadas 
print("\nRange")
for x in range(2,10,2): # o primeiro número é o "apartir de" o segundo é "até onde vai" e o terceiro é "de dois em dois" (não é necessario)
    print(x)

# loop alinhado
print("\nloop alinhado")
for i in range(1,5):
    for j in range(1,6):
        print(i,j)
