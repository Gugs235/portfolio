# -*- coding: utf-8 -*-

################################################################################
## Form gerado a partir da leitura do arquivo UI 'Login_e_cadastro.ui'
##
## Criado pelo: Qt User Interface Compiler versão 6.8.1
##
## AVISO! Todas as alterações feitas neste arquivo serão perdidas ao recompilar o arquivo UI!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont, QCursor)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox)

import imgn_rc  # Importa recursos da interface, como imagens

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Define um nome para a janela principal caso ainda não tenha sido atribuído
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        
        # Define o tamanho da janela principal
        MainWindow.resize(800, 600)
        
        # Define o background da janela principal
        MainWindow.setStyleSheet(u"background-color: rgb(19, 41, 61);")

        # Criação do widget central que contém todos os elementos da interface
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # Define um background alternativo para o widget central
        self.centralwidget.setStyleSheet(u"alternate-background-color: rgb(85, 255, 255);")

        # Layout principal em grade
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        # Criação de um frame que contém os elementos do login
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        # Layout do frame de login
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        # Botão de login
        self.Botao_entrar = QPushButton(self.frame_3)
        self.Botao_entrar.setObjectName(u"Botao_entrar")
        self.Botao_entrar.setEnabled(True)
        self.Botao_entrar.setMaximumSize(300, 50)
        self.Botao_entrar.clicked.connect(self.Cadastro)


        # Define a fonte do botão
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Botao_entrar.setFont(font)

        # Define o estilo do botão (cor de fundo e texto)
        self.Botao_entrar.setStyleSheet(u"color: rgb(11, 60, 88);\n"
                                        "background-color: rgb(36, 123, 160);")

        self.Botao_entrar.setAutoDefault(False)
        self.Botao_entrar.setFlat(False)

        # Adiciona o botão ao layout do frame
        self.gridLayout_4.addWidget(self.Botao_entrar, 2, 0, 1, 1)

        # Grupo para o campo de senha
        self.gp_senha = QFrame(self.frame_3)
        self.gp_senha.setObjectName(u"gp_senha")
        self.gp_senha.setEnabled(True)
        self.gp_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_senha.setFrameShadow(QFrame.Shadow.Raised)

        # Layout do campo de senha
        self.gridLayout = QGridLayout(self.gp_senha)
        self.gridLayout.setObjectName(u"gridLayout")

        # Campo de entrada para senha
        self.lineEdit_senha = QLineEdit(self.gp_senha)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setEnabled(True)
        self.lineEdit_senha.setMinimumSize(170, 30)
        self.lineEdit_senha.setMaximumSize(400, 50)
        self.lineEdit_senha.text()


        # Define a fonte do campo de senha
        font1 = QFont()
        font1.setPointSize(17)
        self.lineEdit_senha.setFont(font1)

        # Define o cursor para a caixa de senha
        self.lineEdit_senha.setCursor(QCursor(Qt.CursorShape.SizeHorCursor))

        # Define a cor do texto da senha
        self.lineEdit_senha.setStyleSheet(u"color: rgb(255, 255, 255);")

        # Define o modo de entrada para ocultar o texto da senha
        self.lineEdit_senha.setEchoMode(QLineEdit.EchoMode.Password)

        # Adiciona o campo de senha ao layout
        self.gridLayout.addWidget(self.lineEdit_senha, 1, 0, 1, 1)

        # Texto do campo de senha
        self.txt_senha = QLabel(self.gp_senha)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEnabled(True)

        # Define a fonte do texto "Senha"
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.txt_senha.setFont(font2)

        # Define a cor do texto "Senha"
        self.txt_senha.setStyleSheet(u"color: rgb(232, 241, 242);")
        self.txt_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Adiciona o texto ao layout do campo de senha
        self.gridLayout.addWidget(self.txt_senha, 0, 0, 1, 1)

        # Adiciona o grupo de senha ao layout principal do frame
        self.gridLayout_4.addWidget(self.gp_senha, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        # Grupo para o campo de usuário
        self.gp_user = QFrame(self.frame_3)
        self.gp_user.setObjectName(u"gp_user")
        self.gp_user.setEnabled(True)
        self.gp_user.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_user.setFrameShadow(QFrame.Shadow.Raised)

        # Layout do campo de usuário
        self.gridLayout_2 = QGridLayout(self.gp_user)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        # Campo de entrada para usuário
        self.lineEdit_user = QLineEdit(self.gp_user)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setEnabled(True)
        self.lineEdit_user.setMinimumSize(150, 30)
        self.lineEdit_user.setMaximumSize(400, 50)
        self.lineEdit_user.setFont(font1)
        self.lineEdit_user.text()


        # Define a cor do texto do usuário
        self.lineEdit_user.setStyleSheet(u"color: rgb(255, 255, 255);")

        # Adiciona o campo ao layout do usuário
        self.gridLayout_2.addWidget(self.lineEdit_user, 1, 0, 1, 1)

        # Texto do campo de usuário
        self.txt_user = QLabel(self.gp_user)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setEnabled(True)
        self.txt_user.setFont(font2)

        # Define a cor do texto "Usuário"
        self.txt_user.setStyleSheet(u"color: rgb(232, 241, 242);")
        self.txt_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Adiciona o texto ao layout do usuário
        self.gridLayout_2.addWidget(self.txt_user, 0, 0, 1, 1)

        # Adiciona o grupo de usuário ao layout principal do frame
        self.gridLayout_4.addWidget(self.gp_user, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        # Adiciona o frame ao layout principal
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        # Define o widget central da janela principal
        MainWindow.setCentralWidget(self.centralwidget)

        # Define os textos exibidos na interface
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Login")
        self.Botao_entrar.setText("Entrar")
        self.txt_senha.setText("Senha")
        self.txt_user.setText("Usuário")

    def Cadastro(self):
        user_correto = "Jss"
        senha_correta = "jss235"

        user = self.lineEdit_user.text()
        senha = self.lineEdit_senha.text()

        if user == user_correto and senha == senha_correta:
            QMessageBox.information(self, "Login feito com sucesso", f"Bem-vindo, {user}!")
            self.open_cadastro_window()
        else:    
            QMessageBox.warning(self, "Erro no Login", "Usuário ou senha incorretos.")


# Executa a aplicação
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
