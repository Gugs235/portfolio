a=(int(input("digite um valor:")))
b=(int(input("digite um valor:")))
c=(int(input("digite um valor:")))

b = b * b
delta = (b) * ( - 4*a*c)

if delta < 0 :
    print("Não possui raiz!")

else:

    delta = delta * delta
    bask1=( (-b) + delta / (2*a))
    bask1 = bask1 ** (1/2)
    print(f"{bask1}")

    bask=( (-b) - delta / (2*a))
    bask = bask ** (1/2)
    print(f"{bask}")
