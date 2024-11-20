#30.	Histograma de Ocorrências em Lista: Crie uma função histograma(lista) que 
# recebe uma lista e retorna um dicionário com o número de ocorrências de cada 
# elemento da lista. 

def histograma(lista):
    ocorrencias = {}
    for item in lista:
        if item in ocorrencias:
            ocorrencias[item] += 1
        else:
            ocorrencias[item] = 1
    return ocorrencias
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
resultado = histograma(lista)
print(resultado)  # Saída: {1: 1, 2: 2, 3: 3, 4: 4}
