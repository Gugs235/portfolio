# Escreva uma função converte_segundos(h, m, s) que converte horas, minutos e 
# segundos em segundos.

def converte_segundos(h, m, s):
    total_segundos = (h * 3600) + (m * 60) + s
    return total_segundos

# Testando a função
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))
resultado = converte_segundos(horas, minutos, segundos)
print(f"{horas} horas, {minutos} minutos e {segundos} segundos equivalem a {resultado} segundos.")
