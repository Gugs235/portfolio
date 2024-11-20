# Crie uma função data_atual() que retorne a data atual no formato "dd/mm/aaaa".

def data_atual(dia, mes, ano):
    return f"{dia:02}/{mes:02}/{ano}"

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

print(data_atual(dia, mes, ano))
