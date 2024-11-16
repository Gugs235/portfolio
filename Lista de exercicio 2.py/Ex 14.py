#14.	Desvio Padrão de Lista: Implemente uma função desvio_padrao(lista) que 
# calcula o desvio padrão dos elementos em uma lista de números.

def desvio_padrao(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)
    
    soma_diferencas = 0
    for num in lista:
        diferenca = num - media
        soma_diferencas += diferenca ** 2
    
    variancia = soma_diferencas / len(lista)
    
    raiz = variancia ** 0.5
    
    return raiz

numeros = [10, 15, 23, 9, 17]
resultado = desvio_padrao(numeros)
print(f"Desvio padrão: {resultado:.2f}")
