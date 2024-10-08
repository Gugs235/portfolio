a = int(input("Escreva o primeiro valor: "))
b = int(input("Escreva o segundo valor: "))
c = int(input("Escreva o terceiro valor: "))
if a > b and b > c:
        print(c, b, a)

if a > c and c > b:
        print(b, c, a)

if b > a and a > c:
        print(c, a, b)

if b > c and c > a:
        print(a, c, b)

if c > a and a > b:
        print(b, a, c)

if c > b and b > a:
        print(a, b, c)
        