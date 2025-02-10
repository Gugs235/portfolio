import sys
from PySide6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Login")
        self.resize(400, 300)  # Tamanho inicial da janela

        self.label_username = QLabel("Usuário:")
        self.label_username.setAlignment(Qt.AlignCenter)
        self.label_username.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.input_username = QLineEdit()
        self.input_username.setStyleSheet("font-size: 18px; padding: 5px;")  
        self.input_username.setMinimumSize(150, 30)
        self.input_username.setMaximumSize(400, 50)

        self.label_password = QLabel("Senha:")
        self.label_password.setAlignment(Qt.AlignCenter)
        self.label_password.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setStyleSheet("font-size: 18px; padding: 5px;")  
        self.input_password.setMinimumSize(150, 30)
        self.input_password.setMaximumSize(400, 50)

        self.button_login = QPushButton("Entrar")
        self.button_login.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.button_login.clicked.connect(self.check_login)

        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

    def check_login(self):
        correct_username = "Jss"
        correct_password = "jss235"

        username = self.input_username.text()
        password = self.input_password.text()

        if username == correct_username and password == correct_password:
            QMessageBox.information(self, "Login feito com sucesso", f"Bem-vindo, {username}!")
            self.open_cadastro_window()
        else:    
            QMessageBox.warning(self, "Erro no Login", "Usuário ou senha incorretos.")

    def open_cadastro_window(self):
        """Abre a janela de cadastro e fecha a de login"""
        self.cadastro_window = CadastroWindow()
        self.cadastro_window.showMaximized()
        self.close()  # Fecha a janela de login


class CadastroWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Cadastro")
        self.resize(400, 300)

        self.label = QLabel("Bem-vindo à Tela de Cadastro!", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.button_close = QPushButton("Fechar")
        self.button_close.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.button_close.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_close)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.showMaximized()
    sys.exit(app.exec())
