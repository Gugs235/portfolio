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

        # Nome centralizado
        self.nome_label = QLabel("Mudando de imagem", self)
        self.nome_label.setAlignment(Qt.AlignCenter)
        self.nome_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.nome_label)

        # Botão para mudar para a primeira imagem
        self.button1 = QPushButton("Imagem 1")
        self.button1.clicked.connect(lambda: self.carregar_imagem(0))
        self.layout.addWidget(self.button1)

        # Botão para mudar para a segunda imagem
        self.button2 = QPushButton("Imagem 2")
        self.button2.clicked.connect(lambda: self.carregar_imagem(1))
        self.layout.addWidget(self.button2)


        # Imagem inicial
        self.imagem_label = QLabel(self)
        self.imagems = [
            r"C:\Users\suporte\Documents\GitHub\portfolio\PySide6\PandaSamurai.png",
            r"C:\Users\suporte\Documents\GitHub\portfolio\PySide6\PandaSamurai2.png"
        ]
        self.layout.addWidget(self.imagem_label)

        # Ajusta o layout
        self.layout.addStretch(1)

    def carregar_imagem(self, index):
        """Atualiza a imagem do QLabel."""
        pixmap = QPixmap(self.imagems[index])
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)  # Redimensionar a foto
        self.imagem_label.setPixmap(pixmap)
        self.imagem_label.setAlignment(Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela()
    window.show()
    sys.exit(app.exec())
