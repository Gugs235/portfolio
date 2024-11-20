# Implemente uma função adiciona_dias(data, n) que adicione n dias a uma data e retorne o novo valor.

def adiciona_dias(data, n):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia, mes, ano = map(int, data.split('/'))
    
    # Verifica se o ano é bissexto
    if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) and mes == 2:
        dias_por_mes[1] = 29
    
    dia += n
    while dia > dias_por_mes[mes - 1]:
        dia -= dias_por_mes[mes - 1]
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1
        if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) and mes == 2:
            dias_por_mes[1] = 29
        else:
            dias_por_mes[1] = 28
    
    return f"{dia:02d}/{mes:02d}/{ano}"

data_inicial = input("Digite a data no formato dd/mm/aaaa: ")
dias_para_adicionar = int(input("Digite o número de dias a adicionar: "))

print(f"A nova data é: {adiciona_dias(data_inicial, dias_para_adicionar)}")
