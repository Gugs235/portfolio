import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget

class NameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inverter Texto")

        # Criando os widgets
        self.label_name = QLabel("Digite seu nome:")
        self.input_name = QLineEdit()
        self.button = QPushButton("Inverter")
        self.result_name = QLabel("")

        # Conectando o botão à função
        self.button.clicked.connect(self.reverse_name)

        # Criando o layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.input_name)
        layout.addWidget(self.button)
        layout.addWidget(self.result_name)

        # Criando um widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def reverse_name(self):
        name = self.input_name.text()
        reversed_name = "" 

        for i in range(len(name) - 1, -1, -1):
            reversed_name += name[i]

        self.result_name.setText(f"Nome invertido: {reversed_name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NameWindow()
    window.show()
    sys.exit(app.exec())
