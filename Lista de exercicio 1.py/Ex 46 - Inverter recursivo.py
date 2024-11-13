# Escreva uma função inverte_string_recursiva(s) que inverta uma string recursivamente.

def inverte_string_recursiva(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + inverte_string_recursiva(s[:-1])

texto = str(input("Escreva algo: "))
print(inverte_string_recursiva(texto))
