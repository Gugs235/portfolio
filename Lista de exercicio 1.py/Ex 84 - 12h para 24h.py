# Crie uma função formato_12h_para_24h(hora_12h) que converta uma hora no formato 12h para 24h.

def formato_12h_para_24h(hora_12h):
    # Separa a hora, os minutos e o período (AM/PM)
    partes = hora_12h.split()
    hora_minutos = partes[0].split(':')
    hora = int(hora_minutos[0])
    minutos = hora_minutos[1]
    periodo = partes[1].upper() 

    if periodo == "AM":
        if hora == 12:  # Caso 12 AM é 00 no formato 24h
            hora_24h = "00"
        else:
            hora_24h = str(hora).zfill(2)
    elif periodo == "PM":
        if hora == 12:
            hora_24h = str(hora)
        else:
            hora_24h = str(hora + 12) 

    return f"{hora_24h}:{minutos}"

hora_12h = "07:30 PM"
hora_24h = formato_12h_para_24h(hora_12h)
print(f"Hora no formato 12h: {hora_12h}")
print(f"Hora no formato 24h: {hora_24h}")
