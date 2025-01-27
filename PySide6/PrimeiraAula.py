from PySide6.QtWidgets import QApplication,QLabel, QMainWindow
from PySide6.QtCore import Qt
import sys

class HelloWordWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Olá Mundo")
        self.setGeometry(150,80,100,30)  # Define a posição e tamanho inicial da janela

        label = QLabel("hello Word!", self)
        label.setGeometry(150,80,100,30)
        label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWordWindow()
    window.show()
    sys.exit(app.exec())

