# try
# se ele gerar erro faça isso
try:
    a = int(input("Digite uma palavra "))
# apenas "except", sozinho é generico, cerve basiacmente para todos os erros.
# por isso tem q especificar o erro
except ValueError: # Erro de valor, (a variavel é inteira mas escrevo strings)
    print("Digite apenas números")
except:
    print("Erro desconhecido")

# finally
# independente de erros
try:
    b =  int(input("Digite uma palavra = "))
except ValueError:
    print("Digite apenas números")
except:
    print("Erro desconhecido")
finally:
    print('final do algoritimo')


# tipos de erros
# NameError = eu errei o código
# SyntaxError = eu errei o código
# ZeroDivisionError = quando o usuario seleciona 0 para dividir (10 * (1/0))
# TypeError = ("2" + 2)