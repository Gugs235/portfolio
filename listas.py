lista = ["Ederson", 37, 1.56]
print(lista)
y = ["jhonathan" , 16]
print(y)

# Criamos uma lista com o [], se escrevermos um numero com aspas vira str
lista1 = [10, 20, 30, 40]
lista2 = ["abacate" , "azedo" , "chocolate"]
print(lista1, lista2)

# Lista alinhada
listaA = ["oi", 2.0, 5, [10, 20]]
print(listaA)

# Len - conta quantos elementos tem na lista. OBS: se tiver uma sublista ele não conta o que tem la dentro
listaL = ["ola", 3, 6, 4.5, [12, 43]]
print (len(listaL))

# Substring - mostra o elemento apartir de um número
listaS = ["ola", 3, 6, 4.5, 12, 43, "abacate"]
print(listaS[2])
# Esse caso é uma operação matematica 9-8=1 ou seja, mostra o 3
print(listaS[9-8]) 
print(listaS[-2])
print(listaS[-1])
# mas da para colocar dois números, print(listaS[0][2]) o primeiro colchete é o elemento, o segunto colchete é o número dele
print(listaS[0][2])

# in - checa se tem o elemento na lista
frutas = ["maca", "banana", "laranja", "melancia", "cereja"]
print("maca" in frutas)
print("pera" in frutas)

# 
frutas = ["maca", "banana", "laranja", "melancia", "cereja"]
print([1, 2] + [3, 4])
print(frutas + [6, 7, 8, 9])
print([] * 4)
print([1, 2, ["olá", "adeus"]] * 2)

# max, min e sum 
# maximo, minimo e soma
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)
print(max(a))
print(min(a))
print(sum(a))

# Fatias de lista
# 
# 
listaF = ["a", "b", "c", "d", "e", "f"]
print(listaF[1:3])
print(listaF[:4])
print(listaF[3:])
print(listaF[:])
print(listaF[0:6])
