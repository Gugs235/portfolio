# Crie uma função conta_elementos(lista) que retorne um dicionário com a contagem de 
# cada elemento na lista.

def conta_elementos(lista):
    contagem = {}
    
    for item in lista:
        if item in contagem:
            contagem[item] += 1
        else:
            contagem[item] = 1
    
    return contagem

lista_exemplo = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
resultado = conta_elementos(lista_exemplo)
print(resultado)
