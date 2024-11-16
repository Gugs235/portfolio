#24.	Números Primos até N: Escreva uma função numeros_primos(n) que retorna uma 
# lista de todos os números primos até um número n dado.

def numeros_primos(n):
    primos = []

    for numero in range(2, n+1):
        is_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                is_primo = False
                break
        if is_primo:
            primos.append(numero)

    return primos
n = 20
primos = numeros_primos(n)
print(primos)  # Saída: [2, 3, 5, 7, 11, 13, 17, 19]
