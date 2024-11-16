#20.	Conta Números em Intervalo: Crie uma função 
# conta_intervalo(lista, inicio, fim) que conta quantos números em uma lista 
# estão dentro de um intervalo [inicio, fim].

def conta_intervalo(lista, inicio, fim):
    contador = 0
    for numero in lista:
        if inicio <= numero <= fim:
            contador += 1
    return contador
lista = [1, 3, 5, 7, 9, 11, 13]
inicio = 5
fim = 10
resultado = conta_intervalo(lista, inicio, fim)
print(resultado)  # Saída: 4 (números dentro do intervalo: 5, 7, 9, 10)
