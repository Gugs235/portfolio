import arrow

# Cria um objeto Arrow para a data e hora atuais
hoje = arrow.now()

# Formata a data e hora em um formato legível
formatado = hoje.format('YYYY-MM-DD HH:mm:ss')
print(f"Data e hora atual: {formatado}")

# Adiciona 7 dias à data atual
futuro = hoje.shift(days=7)
print(f"Data após 7 dias: {futuro.format('YYYY-MM-DD HH:mm:ss')}")

# Subtrai 2 horas da data atual
passado = hoje.shift(hours=-2)
print(f"Data 2 horas atrás: {passado.format('YYYY-MM-DD HH:mm:ss')}")

# Converte a data para um fuso horário diferente
nova_york = hoje.to('America/New_York')
print(f"Data e hora em Nova York: {nova_york.format('YYYY-MM-DD HH:mm:ss')}")


# Atividade: mostre o horario de Campo Grande
campo_grande = hoje.to('America/Campo_Grande')
print(f"Data e hora em Campo Grande MS: {campo_grande.format('YYYY-MM-DD HH:mm:ss')}")

