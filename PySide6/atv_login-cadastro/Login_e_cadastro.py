# -*- coding: utf-8 -*-

################################################################################
## Form gerado a partir da leitura do arquivo UI 'Login_e_cadastro.ui'
##
## Criado pelo: Qt User Interface Compiler versão 6.8.1
##
## AVISO! Todas as alterações feitas neste arquivo serão perdidas ao recompilar o arquivo UI!
################################################################################

# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox)


from Cadastro import Ui_Cadastro  # Aqui, importa a tela de cadastro

import imgn_rc  # Importa recursos da interface, como imagens


class Ui_MainWindow(QMainWindow):  # Agora herda de QMainWindow
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

        # Botão de login
        self.Botao_entrar = QPushButton(self.frame_3)
        self.Botao_entrar.setObjectName("Botao_entrar")
        self.Botao_entrar.setMaximumSize(300, 50)
        self.Botao_entrar.clicked.connect(self.Cadastro)

        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Botao_entrar.setFont(font)
        self.Botao_entrar.setStyleSheet("color: rgb(11, 60, 88);\n"
                                        "background-color: rgb(36, 123, 160);")

        self.gridLayout_4.addWidget(self.Botao_entrar, 2, 0, 1, 1)

        # Campo de senha
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

        font1 = QFont()
        font1.setPointSize(17)
        self.lineEdit_senha.setFont(font1)
        self.lineEdit_senha.setCursor(QCursor(Qt.CursorShape.SizeHorCursor))
        self.lineEdit_senha.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_senha, 1, 0, 1, 1)

        self.txt_senha = QLabel(self.gp_senha)
        self.txt_senha.setObjectName("txt_senha")
        self.txt_senha.setFont(font1)
        self.txt_senha.setStyleSheet("color: rgb(232, 241, 242);")
        self.txt_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_senha, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.gp_senha, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # Campo de usuário
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
        self.lineEdit_user.setFont(font1)
        self.lineEdit_user.setStyleSheet("color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.lineEdit_user, 1, 0, 1, 1)

        self.txt_user = QLabel(self.gp_user)
        self.txt_user.setObjectName("txt_user")
        self.txt_user.setFont(font1)
        self.txt_user.setStyleSheet("color: rgb(232, 241, 242);")
        self.txt_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_user, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.gp_user, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle("Login")
        self.Botao_entrar.setText("Entrar")
        self.txt_senha.setText("Senha")
        self.txt_user.setText("Usuário")


    def Cadastro(self):
        user_correto = "Jss"
        senha_correta = "jss235"

        user = self.lineEdit_user.text()
        senha = self.lineEdit_senha.text()

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

        if user == user_correto and senha == senha_correta:
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("Login feito com sucesso")
            msg_box.setText(f"Bem-vindo, {user}!")
            msg_box.exec()
            self.abrir_tela_cadastro()
            self.close()  # Fecha a tela de login
        else:
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setWindowTitle("Erro no Login")
            msg_box.setText("Usuário ou senha incorretos.")
            msg_box.exec()

    def abrir_tela_cadastro(self):
        self.cadastro_window = QMainWindow()  # Cria uma nova janela para o cadastro
        self.ui_cadastro = Ui_Cadastro()  # Instancia a classe de Cadastro
        self.ui_cadastro.setupUi(self.cadastro_window)  # Configura a UI na nova janela
        self.cadastro_window.showMaximized()  # Exibe a tela de cadastro


# Executa a aplicação
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
