# Escreva uma função dias_entre_datas(data1 data2) que retorne a diferença em dias entre duas datas

def dias_entre_datas(dia1, mes1, ano1, dia2, mes2, ano2):
    def ano_bissexto(ano):
        return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

    def dias_no_mes(mes, ano):
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if mes == 2 and ano_bissexto(ano):
            return 29
        return dias_por_mes[mes - 1]

    def total_dias(dia, mes, ano):
        dias = 0
        for a in range(1, ano):
            dias += 366 if ano_bissexto(a) else 365
        for m in range(1, mes):
            dias += dias_no_mes(m, ano)
        dias += dia
        return dias

    return abs(total_dias(dia2, mes2, ano2) - total_dias(dia1, mes1, ano1))

dia1, mes1, ano1 = map(int, input("Digite a primeira data (dia mês ano): ").split())
dia2, mes2, ano2 = map(int, input("Digite a segunda data (dia mês ano): ").split())

print(f'Diferença em dias: {dias_entre_datas(dia1, mes1, ano1, dia2, mes2, ano2)}')
