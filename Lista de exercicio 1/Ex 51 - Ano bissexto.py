# Crie uma função verifica_ano_bissexto(ano) que retorna True se o ano for bissexto.

def verifica_ano_bissexto(ano):
    # Um ano é bissexto se for divisível por 4, mas não divisível por 100,
    # ou se for divisível por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input("Digite o ano para verificar se é bissexto: "))
if verifica_ano_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
