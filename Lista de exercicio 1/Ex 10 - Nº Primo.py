def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Exemplo de uso
n = int(input("Digite um número: "))
if eh_primo(n):
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")
