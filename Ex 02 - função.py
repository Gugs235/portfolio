# Uma função que necessita de um argumento. A função retorna o valor 'P' se seu argumento for positivo, 
# 'N' se seu argumento for negativo e '0' se seu argumento for zero.

# função com o return com o booleano
def palavra(x):
    if x<0:
        print("N") 
    elif x>0:
        print("P") 
    elif x==0:
        print("0") 
while True:
    num = int(input("Insira um número: "))
    palavra(num)
