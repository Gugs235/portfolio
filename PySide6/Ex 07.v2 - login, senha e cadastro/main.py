# 3️⃣ Arquivo: main.py (Ponto de Entrada do Programa)
# Esse arquivo inicializa o sistema e conecta os botões às funções.


import sys
from PySide6.QtWidgets import QApplication
from designer import LoginWindow
from funcoes import check_login

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginWindow()
    window.button_login.clicked.connect(lambda: check_login(window))  # Conecta o botão à função

    window.showMaximized()
    sys.exit(app.exec())
