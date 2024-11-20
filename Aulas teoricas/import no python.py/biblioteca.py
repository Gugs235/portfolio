# # os system, sistema usado no prompt de comando
# # os.system('cls') - limpa o CMD
# # os.system('pause') - pausa o CMD

# # math
# # biblioteca usada na matematica


# import math

# # math.cell(x) - arredonda para o maximo, ex, 3.5 = 4
# print("\nmath.ceil")
# num = 3.5
# print(math.ceil(num))

# # Retorna o valor absoluto de x
# print("\nmath.fabs")
# x = -3
# print(math.fabs(x))

# # fatorial
# print("\nmath.factorial")
# y = 3
# print(math.factorial(y))

# # math.floor(z) - arredonda para o minimo, ex, 3.5 = 3
# print("\nmath.floor")
# z = 3.5
# print(math.floor(z))

# # math.isqrt(a) - Retorna a raiz quadrada inteira
# print("\nmath.isqrt")
# a = 81
# print(math.isqrt(a))

# # math.pow(b) - Retorna x elevado a potencia de y
# print("\nmath.pow")
# x = 2
# y = 10
# print(math.pow(x,y))


# # manupulação de datas e horas
# import datetime

# print("\ndate time")
# # mostra o ano, mes, e dia
# print(datetime.date.today())

# print("\ndate time formatado")
# # formatando datas em strings usando o método strftime()
# print(datetime.date.today().strftime("%d/%m/%y"))

# print("\ndate time com o tempo")
# print(datetime.datetime.now())

# print("\ndate time com o tempo formatado")
# print(datetime.datetime.now().strftime("%d/%m/%y %H:%M"))

import time
a = 0
x = time.perf_counter()
while a < 10000:
    print(a)
    a+=1
y = time.perf_counter()
print(y-x)

