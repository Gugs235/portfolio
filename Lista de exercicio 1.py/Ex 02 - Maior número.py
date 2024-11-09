def maior (a,b):
    if a > b:
        print(f"O maior número é o A {a}")
    elif b > a:
        print(f"O maior número é o B {b}")
    return a,b
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
maior(a,b)