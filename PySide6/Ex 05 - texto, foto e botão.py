# 5) faça um programa abra uma janela com um texto com seu nome centralizado, uma foto e um button e quando apertar o botão a imagem muda

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minha Janela")
        self.setGeometry(300, 100, 500, 500)  # Define posição e tamanho da janela

        # Cria o widget central e define o layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Nome
        self.nome_label = QLabel("Jhonathan Souza Soares", self)
        self.nome_label.setAlignment(Qt.AlignCenter)
        self.nome_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.nome_label)

        # Imagem inicial
        self.imagem_label = QLabel(self)
        self.imagens = [
            r"C:\Users\Reinaldo\OneDrive\Documentos\GitHub\portfolio\PySide6\PandaSamurai.png",
            r"C:\Users\Reinaldo\OneDrive\Documentos\GitHub\portfolio\PySide6\PandaSamurai2.png",
            r"C:\Users\Reinaldo\OneDrive\Documentos\GitHub\portfolio\PySide6\PandaSamurai3.png"
        ]
        self.imagem_atual = 0  # Índice da imagem atual
        self.carregar_imagem()
        self.layout.addWidget(self.imagem_label)

        # Botão
        self.button = QPushButton("Trocar Imagem")
        self.button.clicked.connect(self.muda_imagem)
        self.layout.addWidget(self.button)

        # Ajusta o layout
        self.layout.addStretch(1)

    def carregar_imagem(self):
        """Carrega a imagem atual no QLabel."""
        pixmap = QPixmap(self.imagens[self.imagem_atual])
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)
        self.imagem_label.setPixmap(pixmap)
        self.imagem_label.setAlignment(Qt.AlignCenter)

    def muda_imagem(self):
        """Altera a imagem exibida ao pressionar o botão."""
        self.imagem_atual = (self.imagem_atual + 1) % len(self.imagens)  # Avança ciclicamente
        self.carregar_imagem()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela()
    window.show()
    sys.exit(app.exec())
