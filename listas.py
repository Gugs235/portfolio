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

# substituir elementos na lista
frutas1 = ["banana", "maça", "cereja"]
print(frutas1)
# agr eu escrevo o número do elemento e o novo nome do elemento para acontecer a substituição
frutas1[0] = "pera"
frutas1[-1] = "laranja"
print(frutas1)

# para substituir varios elementos
uma_lista = ["a", "b", "c", "d", "e", "f"]
print(uma_lista)
# agr eu escrevo os números dos elementos e os novos nomes dos elementos para acontecer as substituições
uma_lista[1:3] = ["x", "y"]
print(uma_lista)

# removendo um elemento da lista (não é a melhor forma)
uma_lista = ["a", "b", "c", "d", "e", "f"]
print(uma_lista)
print(len(uma_lista))

uma_lista[1:3] = []
print(uma_lista)
print(len(uma_lista))

print("\n")
# inserir 1 elemento em uma area especifica na lista
# quando fizer isso o elemnto q estava la vai para o lado
# a = 4 posição
# se eu colocar o b na 4 posição tambem, o vai para o lado ficando na 5 posição e o b no 4
uma_lista = ["a", "d", "f"]
uma_lista[1:1] = ["b" , "c"]
print(uma_lista)
uma_lista[4:4] = ["e"]
print(uma_lista)

print("\n")
# segundo metodo para deletar (mais recomendado e simples)
a = ['um', 'dois', 'três']
del a[1]
print(a)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
del lista[1:5]
print(lista)

print("\n")
# Operador . (ponto) - append
# adiciona elementos no final da lista
a = [81, 82, 83]
a.append(5)
print(a)

print("\n")
# sort
# ordena a lista da variavel em crescente
# a variavel toda fica ordenada
a = [81, 70, 80, 82, 83, 72, 77]
a.sort()
print(a)

print("\n")
# a.sort(reverse = True)
# ordena a lista da variavel em decrescente
# a variavel toda fica ordenada
a = [81, 70, 80, 82, 83, 72, 77]
a.sort(reverse = True)
print(a)

print("\n")
# mostra em que posição esta um elemento
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (a.index(4))

print("\n")
# inserir elemento (segunda forma)
# o primeiro elemento (antes da virgula) é a posição q eu quero 
# o segundo elemento (depois da virgula) é o elemento q eu quero adicionar
a = [88, 81, 82, 83]
print(a)
a.insert(1,100)
print(a)

print("\n")
# count
# mostra quantas vezes o elemento aparece na lista
a = [88, 81, 82, 83, 88, 85, 88, 86]
print(a)
print (a.count(88))

print("\n")
# pop
# outro metodo para apagar
a = [88, 81, 82, 83, 88, 85, 88, 86]
print(a)
a.pop()
print(a)
a.pop(0)
print(a)

print("\n")
# extend
# unifica duas listas
lista = [1, 2]
lista.extend([3,4])
print(lista)