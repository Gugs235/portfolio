from InquirerPy import inquirer


def valida_email(val):
    if '@' not in val:
        raise ValueError("Por favor, insira um e-mail válido.")
    return val


nome = inquirer.text("Qual é o seu nome?").execute()
cor = inquirer.select("Qual é a sua cor favorita?", choices = ["Azul", "Verde", "Vermelho"]).execute()
confirmar = inquirer.confirm("Você deseja continuar?").execute()
email = inquirer.text("Qual é o seu e-mail?" , validate = valida_email).execute()
idade = inquirer.number("Qual é a sua idade?").execute()

