# 2) faça um programa abra uma janela com um texto com seu nome centralizado

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
import sys

class HelloWordWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olá Mundo")
        self.setGeometry(300, 100, 500, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        label = QLabel("Jhonathan Souza Soares!", self)
        label.setAlignment(Qt.AlignCenter)  # Centraliza o texto
        label.setStyleSheet("font-size: 24px; font-weight: bold;")  # 4vw ajusta a fonte proporcional à tela
        

        layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWordWindow()
    window.show()
    sys.exit(app.exec())

