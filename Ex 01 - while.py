# Número inicial
numero = 202

# Contar as reduções
contador = 0

# Enquanto o número for maior que zero, continue subtraindo
while numero > 0:
    numero -= 1
    contador += 1

# Exibe o número de reduções
print(f"O número pode ser reduzido {contador} vezes até chegar a zero.")
