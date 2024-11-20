# Escreva uma função bin2dec(binario) que converte um número binário para decimal.

def bin2dec(binario):
    if not isinstance(binario, str):
        raise ValueError("O número binário deve ser uma string.")
    
    decimal = 0
    potencia = 0

    for digito in reversed(binario):
        if digito == '1':
            decimal += 2 ** potencia
        elif digito == '0':
            pass
        else:
            raise ValueError("O valor fornecido não é um número binário válido.")
        potencia += 1
    return decimal

binario = str(input("Digite o número binario para converter: "))
resultado = bin2dec(binario)
print(f"O número binário {binario} em decimal é {resultado}")
