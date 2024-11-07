# uma função que necessite de tres argumentos e que forneça a soma dos dois primeiros argumentos e multiplicado pelo terceiro

def conta(x,y,z):
    result = (x + y) * z
    return result
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
res = conta(a,b,c)
print("Resultado", res)
