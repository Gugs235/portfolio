# Implemente uma função dec2bin(n) que converte um número decimal para binário.

def dec2bin(n):
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario  # Adiciona o resto da divisão à esquerda
        n = n // 2  # Divide o número por 2 e arredonda para baixo
    
    return binario

numero = int(input("Digite o número decimal para converter: "))
resultado = dec2bin(numero)
print(f"O número decimal {numero} em binário é {resultado}")
