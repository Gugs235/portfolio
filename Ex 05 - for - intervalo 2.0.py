# agora vai somar o valor dos intervalos
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
a = a + 1
soma = 0
for i in range(a,b):
    print(i)
    soma += i
print(f"A soma é {soma}")
