# Crie uma função gera_senha(tamanho) que gere uma senha aleatória de um tamanho específico.

import random
def gera_senha(tamanho):
    senha = ""
    for _ in range(tamanho):
        # Gerando números aleatórios entre 33 e 126 para caracteres imprimíveis
        char = chr(random.randint(33, 126))  # intervalo de caracteres visíveis
        senha += char
    return senha

tamanho = int(input("Digite quantos caracteres tem a senha: "))
print(gera_senha(tamanho))
