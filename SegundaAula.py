nome = input ("Escreva seu nome: ")
print(nome)

sal = float(input('salario? = '))
print(sal)
imposto = float(input('Digite o imposto = '))

# %S str = string = texto
# %D int = inteiro = número sem virgula
# %F float = real = número com virgula
# %B bool = boleando = lógicos

filhos = 3
idade1 = 15
idade2= 11
print("Eu tenho %d filhos, ambos de %d e %d anos" % (filhos, idade1, idade2))

# Concatenação - concatenar (juntar texto) abacate + azedo = abacate azedo

a = "jhonathan"
b = "Soares"
print("Prezado " +a+" "+b+ ". Olá!")

print(10*"Jhonathan\n")


# quadrado
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end = "")
print("+" + 10 * "-" + "+")

# retangulo
print("\n")
print("+" + 20 * "-" + "+")
print(("|" + " " * 20 + "|\n") * 5, end = "")
print("+" + 20 * "-" + "+")

# casa
print("\n")
print(5 * " " + "+" + 10 * "-" + "+" + 4 * " ")
print(4 * " " + "|" + 12 * " " + "|" + 4 * " ")
print(3 * " " + "|" + 14 * " " + "|" + 4 * " ")
print(2 * " " + "|" + 16 * " " + "|" + 4 * " ")
print(1 * " " + "|" + 18 * " " + "|" + 4 * " ")
print("+" + 20 * "-" + "+")
print(("|" + " " * 20 + "|\n") * 5, end = "")
print("+" + 20 * "-" + "+")

# carinha
print("\n")
print("+" + 20 * "-" + "+")
print(("|" + 4 * " " + "|" + 9 * " " + "|" + 5 * " " + "|\n") * 2, end = "")
print(("|" + " " * 20 + "|\n") * 5, end = "")
print("|" + 3 * " " + 15 * "#" +  3 * " " + "|")
print("+" + 21 * "-" + "+")

# Foramatação de strings 2
frase = "Um triangulo de base igual a {0} e altura igual a {1} possui área igual a {2}.".format(2,4,12)
print(frase)

# Foramatação de strings 3
linguagem = "Python"
frases=f"Programando em {linguagem}"
print(frases)