# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# Importando as bibliotecas necessárias do PySide6
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSplitter,
    QVBoxLayout, QWidget, QMessageBox)
import imagemTeste1_rc  # Importando recursos de imagem
from database import insert_user  # Importando a função para inserir usuário no banco de dados
from datetime import datetime  # Importando a classe datetime para manipulação de datas
import re  # Importando a biblioteca para expressões regulares


class Ui_Cadastro(object):
    def setupUi(self, MainWindow):
        # Configurando a janela principal
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1235, 567)  # Definindo o tamanho da janela

        # Criando o widget central
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(19, 41, 61);")  # Definindo a cor de fundo

        # Criando um layout de grade para o widget central
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # Criando um frame para conter todos os elementos do cadastro
        self.gp_Tudo = QFrame(self.centralwidget)
        self.gp_Tudo.setObjectName(u"gp_Tudo")
        font = QFont()
        font.setPointSize(10)
        self.gp_Tudo.setFont(font)
        self.gp_Tudo.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_Tudo.setFrameShadow(QFrame.Shadow.Raised)

        # Criando um layout de grade para o frame
        self.gridLayout_10 = QGridLayout(self.gp_Tudo)
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        # Criando o frame para o campo de nome
        self.Nome = QFrame(self.gp_Tudo)
        self.Nome.setObjectName(u"Nome")
        self.Nome.setFrameShape(QFrame.Shape.StyledPanel)
        self.Nome.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Nome)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # Criando o rótulo para o campo de nome
        self.txt_nome = QLabel(self.Nome)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(52, 25))
        self.txt_nome.setMaximumSize(QSize(60, 30))
        font1 = QFont()
        font1.setPointSize(13)
        self.txt_nome.setFont(font1)
        self.txt_nome.setStyleSheet(u"color: rgb(232, 241, 242);")

        # Adicionando o rótulo ao layout vertical
        self.verticalLayout.addWidget(self.txt_nome)

        # Criando o campo de entrada para nome
        self.imp_nome = QLineEdit(self.Nome)
        self.imp_nome.setObjectName(u"imp_nome")
        self.imp_nome.setMinimumSize(QSize(400, 30))
        self.imp_nome.setMaximumSize(QSize(600, 30))
        font2 = QFont()
        font2.setPointSize(17)
        self.imp_nome.setFont(font2)
        self.imp_nome.setStyleSheet(u"color: rgb(255, 255, 255);")

        # Adicionando o campo de entrada ao layout vertical
        self.verticalLayout.addWidget(self.imp_nome)

        # Adicionando o frame de nome ao layout de grade
        self.gridLayout_10.addWidget(self.Nome, 1, 2, 1, 1)

        # Criando o frame para o campo de email
        self.Email = QFrame(self.gp_Tudo)
        self.Email.setObjectName(u"Email")
        self.Email.setFrameShape(QFrame.Shape.StyledPanel)
        self.Email.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Email)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        # Criando o rótulo para o campo de email
        self.txt_Email = QLabel(self.Email)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setMinimumSize(QSize(52, 25))
        self.txt_Email.setMaximumSize(QSize(60, 30))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.txt_Email.setFont(font1)
        self.txt_Email.setStyleSheet(u"color: rgb(232, 241, 242);")

        # Adicionando o rótulo ao layout vertical
        self.verticalLayout_8.addWidget(self.txt_Email)

        # Criando o campo de entrada para email
        self.imp_Email = QLineEdit(self.Email)
        self.imp_Email.setObjectName(u"imp_Email")
        self.imp_Email.setEnabled(True)
        self.imp_Email.setMinimumSize(QSize(400, 30))
        self.imp_Email.setMaximumSize(QSize(600, 30))
        font2 = QFont()
        font2.setPointSize(17)
        self.imp_Email.setFont(font2)
        self.imp_Email.setStyleSheet(u"color: rgb(255, 255, 255);")

        # Adicionando o campo de entrada ao layout vertical
        self.verticalLayout_8.addWidget(self.imp_Email)

        # Adicionando o frame de email ao layout de grade
        self.gridLayout_10.addWidget(self.Email, 1, 7, 1, 1)

        # Criando o frame para o campo de endereço
        self.Endereco = QFrame(self.gp_Tudo)
        self.Endereco.setObjectName(u"Endereco")
        self.Endereco.setFrameShape(QFrame.Shape.StyledPanel)
        self.Endereco.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Endereco)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        # Criando o rótulo para o campo de endereço
        self.txt_Endereco = QLabel(self.Endereco)
        self.txt_Endereco.setObjectName(u"txt_Endereco")
        self.txt_Endereco.setMinimumSize(QSize(120, 20))
        self.txt_Endereco.setMaximumSize(QSize(125, 30))
        self.txt_Endereco.setFont(font1)
        self.txt_Endereco.setStyleSheet(u"color: rgb(232, 241, 242);")

        # Adicionando o rótulo ao layout vertical
        self.verticalLayout_9.addWidget(self.txt_Endereco)

        # Criando o campo de entrada para endereço
        self.imp_endereco = QLineEdit(self.Endereco)
        self.imp_endereco.setObjectName(u"imp_endereco")
        self.imp_endereco.setMinimumSize(QSize(325, 30))
        self.imp_endereco.setMaximumSize(QSize(300, 30))
        self.imp_endereco.setFont(font2)
        self.imp_endereco.setStyleSheet(u"color: rgb(255, 255, 255);")

        # Adicionando o campo de entrada ao layout vertical
        self.verticalLayout_9.addWidget(self.imp_endereco)

        # Adicionando o frame de endereço ao layout de grade
        self.gridLayout_10.addWidget(self.Endereco, 1, 8, 1, 1)

        # Criando o frame para o campo de data de nascimento
        self.Data_Nascimento = QFrame(self.gp_Tudo)
        self.Data_Nascimento.setObjectName(u"Data_Nascimento")
        self.Data_Nascimento.setFrameShape(QFrame.Shape.StyledPanel)
        self.Data_Nascimento.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Data_Nascimento)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        # Criando o rótulo para o campo de data de nascimento
        self.txt_Data = QLabel(self.Data_Nascimento)
        self.txt_Data.setObjectName(u"txt_Data")
        self.txt_Data.setMinimumSize(QSize(172, 20))
        self.txt_Data.setMaximumSize(QSize(180, 30))
        font1.setPointSize(13)
        self.txt_Data.setFont(font1)
        self.txt_Data.setStyleSheet(u"color: rgb(232, 241, 242);")

        # Adicionando o rótulo ao layout vertical
        self.verticalLayout_5.addWidget(self.txt_Data)

        # Criando o campo de entrada para data de nascimento
        self.date_data_nascimento = QDateEdit(self.Data_Nascimento)
        self.date_data_nascimento.setObjectName(u"date_data_nascimento")
        self.date_data_nascimento.setMinimumSize(QSize(100, 30))
        self.date_data_nascimento.setMaximumSize(QSize(200, 30))
        font5 = QFont()
        font5.setPointSize(11)
        self.date_data_nascimento.setFont(font5)
        self.date_data_nascimento.setStyleSheet(u"color: rgb(255, 255, 255);")

        #definir uma data padrão (a data de hoje) para a caixa date_data_nascimento
        self.date_data_nascimento.setDate(datetime.now())

        # Adicionando o campo de entrada ao layout vertical
        self.verticalLayout_5.addWidget(self.date_data_nascimento)

        # Adicionando o frame de data de nascimento ao layout de grade
        self.gridLayout_10.addWidget(self.Data_Nascimento, 6, 2, 1, 1)

        # Criando o frame para o campo de telefone
        self.Telefone = QFrame(self.gp_Tudo)
        self.Telefone.setObjectName(u"Telefone")
        self.Telefone.setMaximumSize(QSize(16777215, 100))
        self.Telefone.setFrameShape(QFrame.Shape.StyledPanel)
        self.Telefone.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Telefone)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        # Criando o rótulo para o campo de telefone
        self.txt_telefone = QLabel(self.Telefone)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setMinimumSize(QSize(52, 20))
        self.txt_telefone.setMaximumSize(QSize(76, 30))
        self.txt_telefone.setFont(font1)
        self.txt_telefone.setStyleSheet(u"color: rgb(232, 241, 242);")

        # Adicionando o rótulo ao layout vertical
        self.verticalLayout_4.addWidget(self.txt_telefone)

        # Criando o campo de entrada para telefone
        self.imp_telefone = QLineEdit(self.Telefone)
        self.imp_telefone.setObjectName(u"imp_telefone")
        self.imp_telefone.setMinimumSize(QSize(100, 30))
        self.imp_telefone.setMaximumSize(QSize(250, 30))
        self.imp_telefone.setFont(font2)
        self.imp_telefone.setStyleSheet(u"color: rgb(255, 255, 255);")

        # Adicionando o campo de entrada ao layout vertical
        self.verticalLayout_4.addWidget(self.imp_telefone)

        # Adicionando o frame de telefone ao layout de grade
        self.gridLayout_10.addWidget(self.Telefone, 6, 7, 1, 1)

        # Criando o frame para o campo CPF
        self.CPF = QFrame(self.gp_Tudo)
        self.CPF.setObjectName(u"CPF")
        self.CPF.setFrameShape(QFrame.Shape.StyledPanel)
        self.CPF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.CPF)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        # Criando o rótulo para o campo CPF
        self.txt_CPF = QLabel(self.CPF)
        self.txt_CPF.setObjectName(u"txt_CPF")
        self.txt_CPF.setMinimumSize(QSize(52, 25))
        self.txt_CPF.setMaximumSize(QSize(60, 30))
        font1 = QFont()
        font1.setPointSize(13)
        self.txt_CPF.setFont(font1)
        self.txt_CPF.setStyleSheet(u"color: rgb(232, 241, 242);")  # Definindo a cor do texto

        # Adicionando o rótulo ao layout vertical
        self.verticalLayout_3.addWidget(self.txt_CPF)

        # Criando o campo de entrada para CPF
        self.imp_CPF = QLineEdit(self.CPF)
        self.imp_CPF.setObjectName(u"imp_CPF")
        self.imp_CPF.setMinimumSize(QSize(100, 30))
        self.imp_CPF.setMaximumSize(QSize(250, 30))
        font2 = QFont()
        font2.setPointSize(17)
        self.imp_CPF.setFont(font2)
        self.imp_CPF.setStyleSheet(u"color: rgb(255, 255, 255);")  # Definindo a cor do texto

        # Adicionando o campo de entrada ao layout vertical
        self.verticalLayout_3.addWidget(self.imp_CPF)

        # Adicionando o frame CPF ao layout de grade
        self.gridLayout_10.addWidget(self.CPF, 6, 8, 1, 1)

        # Criando o frame para o campo de senha
        self.Nova_Senha = QFrame(self.gp_Tudo)
        self.Nova_Senha.setObjectName(u"Nova_Senha")
        self.Nova_Senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.Nova_Senha.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Nova_Senha)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        # Criando o rótulo para o campo de nova senha
        self.txt_Nova_Senha = QLabel(self.Nova_Senha)
        self.txt_Nova_Senha.setObjectName(u"txt_Nova_Senha")
        self.txt_Nova_Senha.setMinimumSize(QSize(110, 25))
        self.txt_Nova_Senha.setMaximumSize(QSize(110, 30))
        font4 = QFont()
        font4.setPointSize(13)
        self.txt_Nova_Senha.setFont(font4)
        self.txt_Nova_Senha.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout_6.addWidget(self.txt_Nova_Senha)

        # Criando o campo de entrada para nova senha
        self.Input_Nova_Senha = QLineEdit(self.Nova_Senha)
        self.Input_Nova_Senha.setObjectName(u"Input_Nova_Senha")
        self.Input_Nova_Senha.setMinimumSize(QSize(400, 30))
        self.Input_Nova_Senha.setMaximumSize(QSize(600, 30))
        self.Input_Nova_Senha.setFont(font2)
        self.Input_Nova_Senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Input_Nova_Senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.verticalLayout_6.addWidget(self.Input_Nova_Senha)

        # Adicionando o frame de nova senha ao layout de grade
        self.gridLayout_10.addWidget(self.Nova_Senha, 9, 2, 1, 1)

        # Criando o frame para o campo de confirmar senha
        self.Confirmar_Senha = QFrame(self.gp_Tudo)
        self.Confirmar_Senha.setObjectName(u"Confirmar_Senha")
        self.Confirmar_Senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.Confirmar_Senha.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Confirmar_Senha)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        # Criando o rótulo para o campo de confirmar senha
        self.txt_Confirmar_Senha = QLabel(self.Confirmar_Senha)
        self.txt_Confirmar_Senha.setObjectName(u"txt_Confirmar_Senha")
        self.txt_Confirmar_Senha.setMinimumSize(QSize(135, 25))
        self.txt_Confirmar_Senha.setMaximumSize(QSize(150, 30))
        self.txt_Confirmar_Senha.setFont(font4)
        self.txt_Confirmar_Senha.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout_7.addWidget(self.txt_Confirmar_Senha)

        # Criando o campo de entrada para confirmar senha
        self.Input_Confirmar_Senha = QLineEdit(self.Confirmar_Senha)
        self.Input_Confirmar_Senha.setObjectName(u"Input_Confirmar_Senha")
        self.Input_Confirmar_Senha.setMinimumSize(QSize(400, 30))
        self.Input_Confirmar_Senha.setMaximumSize(QSize(600, 30))
        self.Input_Confirmar_Senha.setFont(font2)
        self.Input_Confirmar_Senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Input_Confirmar_Senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.verticalLayout_7.addWidget(self.Input_Confirmar_Senha)

        # Adicionando o frame de confirmar senha ao layout de grade
        self.gridLayout_10.addWidget(self.Confirmar_Senha, 9, 7, 1, 1)

        # Criando o frame para o campo de sexo
        self.Sexo = QFrame(self.gp_Tudo)
        self.Sexo.setObjectName(u"Sexo")
        self.Sexo.setMaximumSize(QSize(16777215, 100))
        self.Sexo.setStyleSheet(u"color: rgb(232, 241, 242);")
        self.Sexo.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sexo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Sexo)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        # Criando o rótulo para o campo de sexo
        self.txt_Sexo = QLabel(self.Sexo)
        self.txt_Sexo.setObjectName(u"txt_Sexo")
        self.txt_Sexo.setMinimumSize(QSize(52, 25))
        self.txt_Sexo.setMaximumSize(QSize(60, 30))
        font4 = QFont()
        font4.setPointSize(13)
        self.txt_Sexo.setFont(font4)

        # Adicionando o rótulo ao layout vertical
        self.verticalLayout_11.addWidget(self.txt_Sexo)

        # Criando as opções de sexo
        self.splitter = QSplitter(self.Sexo)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.opc_Femi = QRadioButton(self.splitter)
        self.opc_Femi.setObjectName(u"opc_Femi")
        self.opc_Femi.setMinimumSize(QSize(100, 25))
        self.opc_Femi.setMaximumSize(QSize(80, 30))
        self.opc_Femi.setFont(font4)
        font4.setPointSize(13)
        self.splitter.addWidget(self.opc_Femi)
        self.opc_Masc = QRadioButton(self.splitter)
        self.opc_Masc.setObjectName(u"opc_Masc")
        self.opc_Masc.setMinimumSize(QSize(110, 30))
        self.opc_Masc.setMaximumSize(QSize(110, 30))
        self.opc_Masc.setFont(font4)
        font4.setPointSize(13)
        self.opc_Masc.setIconSize(QSize(16, 16))
        self.splitter.addWidget(self.opc_Masc)
        self.opc_Outro = QRadioButton(self.splitter)
        self.opc_Outro.setObjectName(u"opc_Outro")
        self.opc_Outro.setMinimumSize(QSize(80, 30))
        self.opc_Outro.setMaximumSize(QSize(110, 30))
        self.opc_Outro.setFont(font4)
        font4.setPointSize(13)
        self.splitter.addWidget(self.opc_Outro)

        self.verticalLayout_11.addWidget(self.splitter)

        # Adicionando o frame de sexo ao layout de grade
        self.gridLayout_10.addWidget(self.Sexo, 9, 8, 1, 1)

        # Criando o frame para o botão de adicionar foto
        self.Foto = QFrame(self.gp_Tudo)
        self.Foto.setObjectName(u"Foto")
        self.Foto.setFrameShape(QFrame.Shape.StyledPanel)
        self.Foto.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Foto)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Botao_Add_Foto = QPushButton(self.Foto)
        self.Botao_Add_Foto.setObjectName(u"Botao_Add_Foto")
        self.Botao_Add_Foto.setMinimumSize(QSize(200, 25))
        self.Botao_Add_Foto.setMaximumSize(QSize(300, 35))
        font6 = QFont()
        self.Botao_Add_Foto.setFont(font6)
        font6.setPointSize(13)
        self.Botao_Add_Foto.setStyleSheet(u"#Botao_Add_Foto {\n"
"    background-color: #0b3c58; /* Cor normal */\n"
"    color: #e8f1f2;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: none; /* Remove a borda padr\u00e3o, se houver */\n"
"    cursor: pointer; /* Muda o cursor para indicar que \u00e9 clic\u00e1vel */\n"
"    transition: background-color 0.3s, transform 0.1s; /* Efeito suave */\n"
"}\n"
"\n"
"#Botao_Add_Foto:hover {\n"
"    background-color: #1B98E0; /* Cor quando o mouse estiver sobre o bot\u00e3o */\n"
"}\n"
"\n"
"#Botao_Add_Foto:pressed {\n"
"    background-color: #0a2a3f; /* Cor quando o bot\u00e3o for pressionado */\n"
"    transform: scale(0.95); /* Efeito de leve redu\u00e7\u00e3o para parecer um clique */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.Botao_Add_Foto)

        self.pos_img = QLabel(self.Foto)
        self.pos_img.setObjectName(u"pos_img")

        self.horizontalLayout.addWidget(self.pos_img)

        # Adicionando o frame da foto ao layout de grade
        self.gridLayout_10.addWidget(self.Foto, 10, 2, 1, 1)

        self.gridLayout.addWidget(self.gp_Tudo, 0, 0, 1, 1)

        # Criando o frame para o botão de entrar
        self.Entrar = QFrame(self.gp_Tudo)
        self.Entrar.setObjectName(u"Entrar")
        self.Entrar.setMinimumSize(QSize(150, 25))
        self.Entrar.setMaximumSize(QSize(300, 50))
        self.Entrar.setFrameShape(QFrame.Shape.StyledPanel)
        self.Entrar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Entrar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        # Criando o botão de entrar
        self.Botao_entrar = QPushButton(self.Entrar)
        self.Botao_entrar.setObjectName(u"Botao_entrar")
        self.Botao_entrar.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Botao_entrar.sizePolicy().hasHeightForWidth())
        self.Botao_entrar.setSizePolicy(sizePolicy)
        self.Botao_entrar.setMinimumSize(QSize(150, 25))
        self.Botao_entrar.setMaximumSize(QSize(300, 50))
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        self.Botao_entrar.setFont(font6)
        self.Botao_entrar.setMouseTracking(True)
        self.Botao_entrar.setStyleSheet(u"#Botao_entrar {\n"
"    background-color: #0b3c58; /* Cor normal */\n"
"    color: #e8f1f2;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"#Botao_entrar:hover {\n"
"    background-color: #1B98E0; /* Cor quando o mouse estiver sobre o bot\u00e3o */\n"
"}\n"
"\n"
"#Botao_entrar:pressed {\n"
"    background-color: #0a2a3f; /* Cor quando o bot\u00e3o for pressionado */\n"
"    transform: scale(0.95); /* Efeito de leve redu\u00e7\u00e3o para parecer um clique */\n"
"}\n"
"")
        self.Botao_entrar.setIconSize(QSize(16, 16))
        self.Botao_entrar.setAutoDefault(False)
        self.Botao_entrar.setFlat(False)

        # Adicionando o botão ao layout vertical
        self.verticalLayout_2.addWidget(self.Botao_entrar)

        # Adicionando o frame do botão ao layout de grade
        self.gridLayout_10.addWidget(self.Entrar, 10, 7, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        # Criando o frame para o título do cadastro
        self.Cadastro = QFrame(self.gp_Tudo)
        self.Cadastro.setObjectName(u"Cadastro")
        self.Cadastro.setFrameShape(QFrame.Shape.StyledPanel)
        self.Cadastro.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Cadastro)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        # Criando o rótulo para o título do cadastro
        self.txt_Cadastro = QLabel(self.Cadastro)
        self.txt_Cadastro.setObjectName(u"txt_Cadastro")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.txt_Cadastro.setFont(font3)
        self.txt_Cadastro.setStyleSheet(u"color: rgb(232, 241, 242);")

        # Adicionando o rótulo ao layout vertical
        self.verticalLayout_10.addWidget(self.txt_Cadastro)

        # Adicionando o frame do título ao layout de grade
        self.gridLayout_10.addWidget(self.Cadastro, 0, 7, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        # Adicionando o frame principal ao layout de grade
        self.gridLayout.addWidget(self.gp_Tudo, 1, 0, 1, 1)

        # Definindo o widget central da janela principal
        MainWindow.setCentralWidget(self.centralwidget)

        # Chamando a função para traduzir os textos da interface
        self.retranslateUi(MainWindow)

        # Conectando o botão de entrar a funções
        self.Botao_entrar.setDefault(False)
        self.Botao_entrar.clicked.connect(self.cadastrar_usuario)  # Conecta a função de cadastro

        # Conectando slots
        QMetaObject.connectSlotsByName(MainWindow)    
    
    # setupUi

    def retranslateUi(self, MainWindow):
        # Traduzindo os textos da interface
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_CPF.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.imp_CPF.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.imp_CPF.setText(QCoreApplication.translate("MainWindow", u"..-", None))
        self.txt_Endereco.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.Botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.txt_telefone.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.imp_telefone.setInputMask(QCoreApplication.translate("MainWindow", u"(00)00000-0000", None))
        self.txt_Email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.txt_nome.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.txt_Cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.txt_Data.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento:", None))
        self.txt_Nova_Senha.setText(QCoreApplication.translate("MainWindow", u"Nova Senha:", None))
        self.txt_Confirmar_Senha.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha:", None))
        self.txt_Sexo.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.opc_Femi.setText(QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.opc_Masc.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.opc_Outro.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.pos_img.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.Botao_Add_Foto.setText(QCoreApplication.translate("MainWindow", u"Adicionar foto", None))

    def cadastrar_usuario(self):
        # Coletando os dados do formulário
        nome = self.imp_nome.text().strip()
        email = self.imp_Email.text().strip()
        cpf = self.imp_CPF.text().strip()
        telefone = self.imp_telefone.text().strip()
        endereco = self.imp_endereco.text().strip()
        data_nascimento = self.date_data_nascimento.text().strip()
        senha = self.Input_Nova_Senha.text().strip()
        confirmar_senha = self.Input_Confirmar_Senha.text().strip()
        sexo = "Masculino" if self.opc_Masc.isChecked() else "Feminino" if self.opc_Femi.isChecked() else "Outro"
        data_hora_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Validações
        if not nome or not nome.isalpha():
            self.mostrar_mensagem_alerta("Por favor, insira um nome válido.")
            return
        if not email or not self.validar_email(email):
            self.mostrar_mensagem_alerta("Por favor, insira um e-mail válido.")
            return
        if not endereco:
            self.mostrar_mensagem_alerta("O campo Endereço é obrigatório.")
            return
        if not data_nascimento:
            self.mostrar_mensagem_alerta("O campo Data de Nascimento é obrigatório.")
            return
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        idade = datetime.now().year - data_nascimento.year - ((datetime.now().month, datetime.now().day) < (data_nascimento.month, data_nascimento.day))
        if idade < 18:
            self.mostrar_mensagem_alerta("Você precisa ter mais de 18 anos para se cadastrar.")
            return
        if not telefone or not self.validar_telefone(telefone):
            self.mostrar_mensagem_alerta("O campo Telefone é obrigatório.")
            return
        if not cpf or not self.validar_cpf(cpf):
            self.mostrar_mensagem_alerta("Por favor, insira um CPF válido.")
            return
        if not senha:
            self.mostrar_mensagem_alerta("O campo Nova Senha é obrigatório.")
            return
        if senha != confirmar_senha:
            self.mostrar_mensagem_alerta("As senhas não coincidem.")
            return
        if not sexo or not self.opc_Femi.isChecked() and not self.opc_Masc.isChecked() and not self.opc_Outro.isChecked():
            self.mostrar_mensagem_alerta("O campo Sexo é obrigatório.")
            return

        # Exibindo os dados que estão sendo cadastrados
        print("Tentando cadastrar:", nome, email, cpf, telefone, endereco, data_nascimento, sexo, data_hora_cadastro)

        try:
            # Insere o usuário no banco de dados
            insert_user(nome, email, cpf, telefone, endereco, data_nascimento, sexo, data_hora_cadastro)
            self.limpar_campos()  # Limpa os campos após o cadastro
            self.mostrar_mensagem_e_fechar()  # Chama a função para mostrar a mensagem de sucesso
        except Exception as e:
            self.mostrar_mensagem_alerta(f"Erro ao cadastrar usuário: {str(e)}")

    def limpar_campos(self):
        self.imp_nome.clear()
        self.imp_Email.clear()
        self.imp_CPF.clear()
        self.imp_telefone.clear()
        self.imp_endereco.clear()
        self.date_data_nascimento.clear()
        self.Input_Nova_Senha.clear()
        self.Input_Confirmar_Senha.clear()
        self.opc_Masc.setChecked(False)
        self.opc_Femi.setChecked(False)
        self.opc_Outro.setChecked(False)

        # Exibe uma mensagem de sucesso
        self.mostrar_mensagem_e_fechar()  # Chama a função para mostrar a mensagem de sucesso

    def validar_email(self, email):
        # Usando uma expressão regular para validar o formato do e-mail
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def validar_cpf(self, cpf):
        # Remover caracteres não numéricos
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11:
            return False
        # Validação simples do CPF (não é a validação completa)
        # Aqui você pode implementar uma validação mais robusta se necessário
        return True

    def validar_telefone(self, telefone):
        # Remover caracteres não numéricos
        telefone = re.sub(r'\D', '', telefone)
        if len(telefone) != 11:
            return False
        # Validação simples do telefone (não é a validação completa)
        # Aqui você pode implementar uma validação mais robusta se necessário
        return True

    def mostrar_mensagem_alerta(self, mensagem):
        # Mostra uma mensagem de alerta
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(mensagem)
        msg.setWindowTitle("Atenção")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()  # Exibe a mensagem

    def mostrar_mensagem_aviso(self, mensagem):
        # Mostra uma mensagem de informação
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(mensagem)
        msg.setWindowTitle("Atenção")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()  # Exibe a mensagem


    def mostrar_mensagem_e_fechar(self):
        # Mostra uma mensagem de sucesso após o cadastro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Cadastro realizado com sucesso!")
        msg.setWindowTitle("Sucesso")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        resposta = msg.exec() # Exibe a mensagem e espera resposta
        
        # if resposta == QMessageBox.StandardButton.Ok:
        #     QCoreApplication.quit()  # Fecha a aplicação


# Código principal para executar a aplicação
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # Cria a aplicação
    MainWindow = QMainWindow()  # Cria a janela principal
    ui = Ui_Cadastro()  # Cria a interface de cadastro
    ui.setupUi(MainWindow)  # Configura a interface na janela principal
    MainWindow.show()  # Exibe a janela
    sys.exit(app.exec())  # Executa a aplicação
