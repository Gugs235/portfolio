# n = número de doces disponiveis
# x = numero de doces nessesarios para evoluir
# y= numero de doces necessarios para o segundo po que maão evoluir
# z= numero de doces necessarios para o terceiro po que maão evoluir
n=0
x=0
y=0
z=0
doce=0

n=int(input('numero de doces disponiveis: '))


x=int(input('numero de doces necessarios para evoluir 1: '))
doce = n - x
if n >= x:
    cont = 1

y=int(input('numero de doces necessarios para evoluir 2: '))
doce = doce - y
if doce >= y:
    cont = 2

z=int(input('numero de doces necessarios para evoluir 3: '))
doce = doce - z
if doce >= z:
    cont = 3


print(cont)