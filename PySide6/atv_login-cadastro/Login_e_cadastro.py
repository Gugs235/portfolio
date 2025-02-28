# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QCursor, QPixmap
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox)
from Cadastro import Ui_Cadastro
import imgn_rc
from database import get_user
import os

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(19, 41, 61);")

        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("alternate-background-color: rgb(85, 255, 255);")

        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # Definindo font1 antes de usá-lo
        font1 = QFont()
        font1.setPointSize(17)

        self.Botao_entrar = QPushButton(self.frame_3)
        self.Botao_entrar.setObjectName("Botao_entrar")
        self.Botao_entrar.setMaximumSize(300, 50)
        self.Botao_entrar.clicked.connect(self.validar_login)

        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Botao_entrar.setFont(font)
        self.Botao_entrar.setStyleSheet(u"#Botao_entrar {\n"
"    background-color: #0b3c58;\n"
"    color: #e8f1f2;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"#Botao_entrar:hover {\n"
"    background-color: #1B98E0;\n"
"}\n"
"#Botao_entrar:pressed {\n"
"    background-color: #0a2a3f;\n"
"    transform: scale(0.95);\n"
"}")
        self.gridLayout_4.addWidget(self.Botao_entrar, 2, 0, 1, 1)

        self.gp_user = QFrame(self.frame_3)
        self.gp_user.setObjectName("gp_user")
        self.gp_user.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_user.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2 = QGridLayout(self.gp_user)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.lineEdit_user = QLineEdit(self.gp_user)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_user.setMinimumSize(150, 30)
        self.lineEdit_user.setMaximumSize(400, 50)
        self.lineEdit_user.setFont(font1)  # Usando font1 aqui
        self.lineEdit_user.setStyleSheet("color: rgb(255, 255, 255);")
        self.gridLayout_2.addWidget(self.lineEdit_user, 1, 0, 1, 1)

        self.txt_user = QLabel(self.gp_user)
        self.txt_user.setObjectName("txt_user")
        self.txt_user.setFont(font1)  # Usando font1 aqui
        self.txt_user.setStyleSheet("color: rgb(232, 241, 242);")
        self.txt_user.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2.addWidget(self.txt_user, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.gp_user, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.gp_senha = QFrame(self.frame_3)
        self.gp_senha.setObjectName("gp_senha")
        self.gp_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_senha.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout = QGridLayout(self.gp_senha)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit_senha = QLineEdit(self.gp_senha)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.lineEdit_senha.setMinimumSize(170, 30)
        self.lineEdit_senha.setMaximumSize(400, 50)
        self.lineEdit_senha.setFont(font1)  # Usando font1 aqui
        self.lineEdit_senha.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lineEdit_senha.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.gridLayout.addWidget(self.lineEdit_senha, 1, 0, 1, 1)

        self.txt_senha = QLabel(self.gp_senha)
        self.txt_senha.setObjectName("txt_senha")
        self.txt_senha.setFont(font1)  # Usando font1 aqui
        self.txt_senha.setStyleSheet("color: rgb(232, 241, 242);")
        self.txt_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.txt_senha, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.gp_senha, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle("Login")
        self.Botao_entrar.setText("Entrar")
        self.txt_senha.setText("Senha")
        self.txt_user.setText("Usuário")

    def validar_login(self):
        nome = self.lineEdit_user.text().strip()
        senha = self.lineEdit_senha.text()

        usuario = get_user(nome, senha)
        msg_box = QMessageBox(self)
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #2C3E50;
                color: #ECF0F1;
                font-size: 14pt;
                border: 2px solid #3498DB;
            }
            QLabel {
                background-color: transparent;
                color: #ECF0F1;
            }
            QPushButton {
                background-color: #3498DB;
                color: white;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)

        if usuario:
            nome_usuario = usuario["nome"]
            foto = usuario["foto"]
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("Login Bem-Sucedido")
            msg_box.setText(f"Bem-vindo, {nome_usuario}!")
            msg_box.exec()
            self.abrir_tela_cadastro(nome_usuario, foto)
            self.close()
        else:
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle("Erro no Login")
            msg_box.setText("Nome de usuário ou senha incorretos.")
            msg_box.exec()

    def abrir_tela_cadastro(self, nome, foto):
        self.cadastro_window = QMainWindow()
        self.ui_cadastro = Ui_Cadastro()
        self.ui_cadastro.setupUi(self.cadastro_window)
        
        if foto and os.path.exists(foto):
            pixmap = QPixmap(foto)
            self.ui_cadastro.pos_img.setPixmap(pixmap)
            self.ui_cadastro.pos_img.setScaledContents(True)
        
        self.ui_cadastro.txt_Cadastro.setText(f"Bem-vindo, {nome}!")
        self.cadastro_window.showMaximized()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.showMaximized()
    sys.exit(app.exec())