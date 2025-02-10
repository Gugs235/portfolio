# 2️⃣ Arquivo: funcoes.py (Funcionalidades do Sistema)
# Aqui colocamos as funções de login e troca de tela.


from PySide6.QtWidgets import QMessageBox
from designer import CadastroWindow


def check_login(window):
    """Verifica o login e troca de tela se for bem-sucedido."""
    correct_username = "Jss"
    correct_password = "jss235"

    username = window.input_username.text()
    password = window.input_password.text()

    if username == correct_username and password == correct_password:
        QMessageBox.information(window, "Login feito com sucesso", f"Bem-vindo, {username}!")
        open_cadastro_window(window)
    else:
        QMessageBox.warning(window, "Erro no Login", "Usuário ou senha incorretos.")


def open_cadastro_window(window):
    """Abre a tela de cadastro e fecha a tela de login."""
    window.cadastro_window = CadastroWindow()
    window.cadastro_window.showMaximized()
    window.close()

