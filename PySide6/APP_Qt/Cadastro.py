# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget, QMessageBox)
import imagemTeste1_rc
from database import insert_user

class Ui_Cadastro(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1235, 567)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(19, 41, 61);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gp_Tudo = QFrame(self.centralwidget)
        self.gp_Tudo.setObjectName(u"gp_Tudo")
        font = QFont()
        font.setPointSize(10)
        self.gp_Tudo.setFont(font)
        self.gp_Tudo.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_Tudo.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.gp_Tudo)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.CPF = QFrame(self.gp_Tudo)
        self.CPF.setObjectName(u"CPF")
        self.CPF.setFrameShape(QFrame.Shape.StyledPanel)
        self.CPF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.CPF)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_CPF = QLabel(self.CPF)
        self.txt_CPF.setObjectName(u"txt_CPF")
        self.txt_CPF.setMinimumSize(QSize(52, 25))
        self.txt_CPF.setMaximumSize(QSize(60, 30))
        font1 = QFont()
        font1.setPointSize(13)
        self.txt_CPF.setFont(font1)
        self.txt_CPF.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout_3.addWidget(self.txt_CPF)

        self.imp_CPF = QLineEdit(self.CPF)
        self.imp_CPF.setObjectName(u"imp_CPF")
        self.imp_CPF.setMinimumSize(QSize(100, 30))
        self.imp_CPF.setMaximumSize(QSize(250, 30))
        font2 = QFont()
        font2.setPointSize(17)
        self.imp_CPF.setFont(font2)
        self.imp_CPF.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.imp_CPF)


        self.gridLayout_10.addWidget(self.CPF, 6, 8, 1, 1)

        self.Entrar = QFrame(self.gp_Tudo)
        self.Entrar.setObjectName(u"Entrar")
        self.Entrar.setMinimumSize(QSize(150, 25))
        self.Entrar.setMaximumSize(QSize(300, 50))
        self.Entrar.setFrameShape(QFrame.Shape.StyledPanel)
        self.Entrar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Entrar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.Botao_entrar.setFont(font3)
        self.Botao_entrar.setStyleSheet(u"color: rgb(11, 60, 88);\n"
"background-color: rgb(36, 123, 160);")
        self.Botao_entrar.setIconSize(QSize(16, 16))
        self.Botao_entrar.setAutoDefault(False)
        self.Botao_entrar.setFlat(False)

        self.verticalLayout_2.addWidget(self.Botao_entrar)


        self.gridLayout_10.addWidget(self.Entrar, 9, 7, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.Email = QFrame(self.gp_Tudo)
        self.Email.setObjectName(u"Email")
        self.Email.setFrameShape(QFrame.Shape.StyledPanel)
        self.Email.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Email)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.txt_Email = QLabel(self.Email)
        self.txt_Email.setObjectName(u"txt_Email")
        self.txt_Email.setMinimumSize(QSize(52, 25))
        self.txt_Email.setMaximumSize(QSize(60, 30))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(False)
        self.txt_Email.setFont(font4)
        self.txt_Email.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout_8.addWidget(self.txt_Email)

        self.imp_Email = QLineEdit(self.Email)
        self.imp_Email.setObjectName(u"imp_Email")
        self.imp_Email.setEnabled(True)
        self.imp_Email.setMinimumSize(QSize(400, 30))
        self.imp_Email.setMaximumSize(QSize(600, 30))
        self.imp_Email.setFont(font2)
        self.imp_Email.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.imp_Email)


        self.gridLayout_10.addWidget(self.Email, 1, 7, 1, 1)

        self.Nome = QFrame(self.gp_Tudo)
        self.Nome.setObjectName(u"Nome")
        self.Nome.setFrameShape(QFrame.Shape.StyledPanel)
        self.Nome.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Nome)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_nome = QLabel(self.Nome)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(52, 25))
        self.txt_nome.setMaximumSize(QSize(60, 30))
        self.txt_nome.setFont(font4)
        self.txt_nome.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout.addWidget(self.txt_nome)

        self.imp_nome = QLineEdit(self.Nome)
        self.imp_nome.setObjectName(u"imp_nome")
        self.imp_nome.setMinimumSize(QSize(400, 30))
        self.imp_nome.setMaximumSize(QSize(600, 30))
        self.imp_nome.setFont(font2)
        self.imp_nome.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.imp_nome)


        self.gridLayout_10.addWidget(self.Nome, 1, 2, 1, 1)

        self.Cadastro = QFrame(self.gp_Tudo)
        self.Cadastro.setObjectName(u"Cadastro")
        self.Cadastro.setFrameShape(QFrame.Shape.StyledPanel)
        self.Cadastro.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Cadastro)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_Cadastro = QLabel(self.Cadastro)
        self.txt_Cadastro.setObjectName(u"txt_Cadastro")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        self.txt_Cadastro.setFont(font5)
        self.txt_Cadastro.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout_10.addWidget(self.txt_Cadastro)


        self.gridLayout_10.addWidget(self.Cadastro, 0, 7, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.Data_Nascimento = QFrame(self.gp_Tudo)
        self.Data_Nascimento.setObjectName(u"Data_Nascimento")
        self.Data_Nascimento.setFrameShape(QFrame.Shape.StyledPanel)
        self.Data_Nascimento.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Data_Nascimento)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.txt_Data = QLabel(self.Data_Nascimento)
        self.txt_Data.setObjectName(u"txt_Data")
        self.txt_Data.setMinimumSize(QSize(172, 20))
        self.txt_Data.setMaximumSize(QSize(172, 30))
        self.txt_Data.setFont(font4)
        self.txt_Data.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout_5.addWidget(self.txt_Data)

        self.date_data = QDateEdit(self.Data_Nascimento)
        self.date_data.setObjectName(u"date_data")
        self.date_data.setMinimumSize(QSize(100, 30))
        self.date_data.setMaximumSize(QSize(200, 30))
        font6 = QFont()
        font6.setPointSize(11)
        self.date_data.setFont(font6)
        self.date_data.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.date_data)


        self.gridLayout_10.addWidget(self.Data_Nascimento, 6, 2, 1, 1)

        self.Endereco = QFrame(self.gp_Tudo)
        self.Endereco.setObjectName(u"Endereco")
        self.Endereco.setFrameShape(QFrame.Shape.StyledPanel)
        self.Endereco.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Endereco)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.txt_Endereco = QLabel(self.Endereco)
        self.txt_Endereco.setObjectName(u"txt_Endereco")
        self.txt_Endereco.setMinimumSize(QSize(120, 20))
        self.txt_Endereco.setMaximumSize(QSize(125, 30))
        self.txt_Endereco.setFont(font4)
        self.txt_Endereco.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout_9.addWidget(self.txt_Endereco)

        self.imp_endereco = QLineEdit(self.Endereco)
        self.imp_endereco.setObjectName(u"imp_endereco")
        self.imp_endereco.setMinimumSize(QSize(325, 30))
        self.imp_endereco.setMaximumSize(QSize(300, 30))
        self.imp_endereco.setFont(font2)
        self.imp_endereco.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.imp_endereco)


        self.gridLayout_10.addWidget(self.Endereco, 1, 8, 1, 1)

        self.Telefone = QFrame(self.gp_Tudo)
        self.Telefone.setObjectName(u"Telefone")
        self.Telefone.setMaximumSize(QSize(16777215, 100))
        self.Telefone.setFrameShape(QFrame.Shape.StyledPanel)
        self.Telefone.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Telefone)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txt_telefone = QLabel(self.Telefone)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setMinimumSize(QSize(52, 20))
        self.txt_telefone.setMaximumSize(QSize(76, 30))
        self.txt_telefone.setFont(font4)
        self.txt_telefone.setStyleSheet(u"color: rgb(232, 241, 242);")

        self.verticalLayout_4.addWidget(self.txt_telefone)

        self.imp_telefone = QLineEdit(self.Telefone)
        self.imp_telefone.setObjectName(u"imp_telefone")
        self.imp_telefone.setMinimumSize(QSize(100, 30))
        self.imp_telefone.setMaximumSize(QSize(250, 30))
        self.imp_telefone.setFont(font2)
        self.imp_telefone.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.imp_telefone)


        self.gridLayout_10.addWidget(self.Telefone, 6, 7, 1, 1)

        self.Sexo = QFrame(self.gp_Tudo)
        self.Sexo.setObjectName(u"Sexo")
        self.Sexo.setMaximumSize(QSize(16777215, 100))
        self.Sexo.setStyleSheet(u"color: rgb(232, 241, 242);")
        self.Sexo.setFrameShape(QFrame.Shape.StyledPanel)
        self.Sexo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Sexo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_Sexo = QLabel(self.Sexo)
        self.txt_Sexo.setObjectName(u"txt_Sexo")
        self.txt_Sexo.setMinimumSize(QSize(52, 25))
        self.txt_Sexo.setMaximumSize(QSize(60, 30))
        self.txt_Sexo.setFont(font1)

        self.horizontalLayout.addWidget(self.txt_Sexo)

        self.opc_Outr = QRadioButton(self.Sexo)
        self.opc_Outr.setObjectName(u"opc_Outr")
        self.opc_Outr.setMinimumSize(QSize(80, 25))
        self.opc_Outr.setMaximumSize(QSize(80, 30))
        self.opc_Outr.setFont(font1)

        self.horizontalLayout.addWidget(self.opc_Outr)

        self.opc_Femi = QRadioButton(self.Sexo)
        self.opc_Femi.setObjectName(u"opc_Femi")
        self.opc_Femi.setMinimumSize(QSize(80, 30))
        self.opc_Femi.setMaximumSize(QSize(110, 30))
        self.opc_Femi.setFont(font1)

        self.horizontalLayout.addWidget(self.opc_Femi)

        self.opc_Masc = QRadioButton(self.Sexo)
        self.opc_Masc.setObjectName(u"opc_Masc")
        self.opc_Masc.setMinimumSize(QSize(110, 30))
        self.opc_Masc.setMaximumSize(QSize(110, 30))
        self.opc_Masc.setFont(font1)
        self.opc_Masc.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.opc_Masc)


        self.gridLayout_10.addWidget(self.Sexo, 8, 2, 2, 1)


        self.gridLayout.addWidget(self.gp_Tudo, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Botao_entrar.setDefault(False)
        self.Botao_entrar.clicked.connect(self.mostrar_mensagem_e_fechar)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_CPF.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.imp_CPF.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000-00", None))
        self.imp_CPF.setText(QCoreApplication.translate("MainWindow", u"..-", None))
        self.Botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.txt_Email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.txt_nome.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.txt_Cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.txt_Data.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento:", None))
        self.txt_Endereco.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.txt_telefone.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.imp_telefone.setInputMask(QCoreApplication.translate("MainWindow", u"(00)00000-0000", None))
        self.txt_Sexo.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.opc_Outr.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.opc_Femi.setText(QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.opc_Masc.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
    # retranslateUi

    def cadastrar_usuario(self):
        nome = self.imp_nome.text()
        email = self.imp_Email.text()
        cpf = self.imp_CPF.text()
        telefone = self.imp_telefone.text()
        endereco = self.imp_endereco.text()
        data_nascimento = self.date_data.date().toString("yyyy-MM-dd")  # Formato de data para MySQL
        sexo = "Masculino" if self.opc_Masc.isChecked() else "Feminino" if self.opc_Femi.isChecked() else "Outro"

        # Insere o usuário no banco de dados
        insert_user(nome, email, cpf, telefone, endereco, data_nascimento, sexo)

        # Exibe uma mensagem de sucesso
        msg_box = QMessageBox()
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

    def mostrar_mensagem_e_fechar(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Cadastro realizado com sucesso!")
        msg.setWindowTitle("Sucesso")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        resposta = msg.exec()  # Exibe a mensagem e espera resposta
        
        if resposta == QMessageBox.StandardButton.Ok:
            self.QMainWindow.close()  # Fecha a janela principal

        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())