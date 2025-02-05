# 5) faça um programa abra uma janela com um texto com seu nome centralizado, uma foto e um button e quando apertar o botão a imagem muda

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.hello = ["Jhonathan", "Jhonathan Souza", "Jhonathan Souza Soares"]
        self.button = QtWidgets.QPushButton("Botão")
        self.setWindowTitle("Minha Janela")
        self.setGeometry(300, 100, 500, 500)  # Define posição e tamanho da janela

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # espaço antes do nome
        layout.addStretch(1)

        # Texto
        nome_label = QLabel("Jhonathan Souza Soares", self)
        nome_label.setAlignment(Qt.AlignCenter)
        nome_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Imagem
        imagem_label = QLabel(self)
        pixmap = QPixmap(r"C:\Users\suporte\Documents\GitHub\portfolio\PySide6\PandaSamurai.png")  
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)  # Redimensionar a foto
        imagem_label.setPixmap(pixmap)
        imagem_label.setAlignment(Qt.AlignCenter)

        # Tela
        layout.addWidget(nome_label)
        layout.addWidget(imagem_label)
        layout.addWidget(self.button)

        layout.addStretch(1)  # espaço em baixo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela()
    window.show()
    sys.exit(app.exec())
