# 3) faça um programa abra uma janela com um texto com seu nome centralizado e uma foto

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Celso Lucas", "Anne Primon", "Jhonathan Soares", "Vitor Galvão"]

        self.button = { text: "Click me"; Layout.alignment: Qt.AlignHCenter onClicked:  setText() }
        
        self.button = QtWidgets.QPushButton("Botão!")
        self.text = QtWidgets.QLabel("Esses são pessoas do meu curso :-)",
        alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

widget = MyWidget()
widget.resize(800, 800)
widget.show()

sys.exit(app.exec())

