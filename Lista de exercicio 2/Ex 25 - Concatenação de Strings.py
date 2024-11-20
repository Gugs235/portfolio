#25.	Concatenação de Strings: Crie uma função concatena_strings(lista_strings) 
# que recebe uma lista de strings e retorna uma única string com todas as strings 
# concatenadas.

def concatena_strings(lista_strings):
    return ''.join(lista_strings)
lista = ["Olá", " ", "mundo", "!", " ", "Como", " ", "vai?"]
resultado = concatena_strings(lista)
print(resultado)  # Saída: "Olá mundo! Como vai?"
