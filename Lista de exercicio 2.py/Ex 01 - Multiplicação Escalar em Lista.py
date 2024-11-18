#1.	Multiplicação Escalar em Lista: Crie uma função multiplica_escalar(lista, escalar) 
# que recebe uma lista de números e um escalar, e multiplica cada elemento da lista pelo 
# escalar, retornando a nova lista.

def multiplica_escalar(lista, escalar):
    return [elemento * escalar for elemento in lista]

numeros = [1, 2, 3, 4]
escalar = 3
resultado = multiplica_escalar(numeros, escalar)
print(resultado)  # Saída: [3, 6, 9, 12]
