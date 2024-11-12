# Escreva uma função eh_armstrong(n) que verifica se um número é um número de Armstrong.

def eh_armstrong(n):
    str_n = str(n)
    num_digitos = len(str_n)
    
    soma = sum(int(digito) ** num_digitos for digito in str_n)
    
    return soma == n

n = int(input("Digite um número para verificar se é de Armstrong: "))
if eh_armstrong(n):
    print(f"{n} é um número de Armstrong!")
else:
    print(f"{n} não é um número de Armstrong.")
