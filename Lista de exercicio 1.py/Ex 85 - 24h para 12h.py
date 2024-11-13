# Escreva uma função formato_24h_para_12h(hora_24h) que converta uma hora no formato 24h para 12h.

def formato_24h_para_12h(hora_24h):
    hora, minutos = map(int, hora_24h.split(':'))
    
    # Determina AM ou PM
    if hora == 0:
        hora_12h = 12
        periodo = 'AM'
    elif hora == 12:
        hora_12h = 12
        periodo = 'PM'
    elif hora > 12:
        hora_12h = hora - 12
        periodo = 'PM'
    else:
        hora_12h = hora
        periodo = 'AM'

    return f"{hora_12h}:{minutos:02d} {periodo}"

hora_24h = "14:30"
hora_12h = formato_24h_para_12h(hora_24h)
print(hora_12h)
