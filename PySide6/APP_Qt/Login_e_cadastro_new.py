# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_e_cadastro.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import imgn_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(19, 41, 61);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"alternate-background-color: rgb(85, 255, 255);")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMouseTracking(False)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Botao_entrar = QPushButton(self.frame_3)
        self.Botao_entrar.setObjectName(u"Botao_entrar")
        self.Botao_entrar.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Botao_entrar.sizePolicy().hasHeightForWidth())
        self.Botao_entrar.setSizePolicy(sizePolicy1)
        self.Botao_entrar.setMaximumSize(QSize(300, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Botao_entrar.setFont(font)
        self.Botao_entrar.setStyleSheet(u"#Botao_entrar{\n"
"    background-color: #0b3c58; /* Cor normal */\n"
"    color: #e8f1f2;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    border: none; /* Remove a borda padr\u00e3o, se houver */\n"
"    cursor: pointer; /* Muda o cursor para indicar que \u00e9 clic\u00e1vel */\n"
"    transition: background-color 0.3s, transform 0.1s; /* Efeito suave */\n"
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

        self.gridLayout_4.addWidget(self.Botao_entrar, 2, 0, 1, 1)

        self.gp_senha = QFrame(self.frame_3)
        self.gp_senha.setObjectName(u"gp_senha")
        self.gp_senha.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.gp_senha.sizePolicy().hasHeightForWidth())
        self.gp_senha.setSizePolicy(sizePolicy1)
        self.gp_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_senha.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.gp_senha)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_senha = QLineEdit(self.gp_senha)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_senha.sizePolicy().hasHeightForWidth())
        self.lineEdit_senha.setSizePolicy(sizePolicy1)
        self.lineEdit_senha.setMinimumSize(QSize(170, 30))
        self.lineEdit_senha.setMaximumSize(QSize(400, 50))
        font1 = QFont()
        font1.setPointSize(17)
        self.lineEdit_senha.setFont(font1)
        self.lineEdit_senha.setCursor(QCursor(Qt.CursorShape.SizeHorCursor))
        self.lineEdit_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_senha.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhNoAutoUppercase|Qt.InputMethodHint.ImhNoPredictiveText|Qt.InputMethodHint.ImhSensitiveData)
        self.lineEdit_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_senha, 1, 0, 1, 1)

        self.txt_senha = QLabel(self.gp_senha)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet(u"color: rgb(232, 241, 242);")
        self.txt_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_senha, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gp_senha, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.gp_user = QFrame(self.frame_3)
        self.gp_user.setObjectName(u"gp_user")
        self.gp_user.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.gp_user.sizePolicy().hasHeightForWidth())
        self.gp_user.setSizePolicy(sizePolicy1)
        self.gp_user.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_user.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.gp_user)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_user = QLineEdit(self.gp_user)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_user.setSizePolicy(sizePolicy1)
        self.lineEdit_user.setMinimumSize(QSize(150, 30))
        self.lineEdit_user.setMaximumSize(QSize(400, 50))
        self.lineEdit_user.setFont(font1)
        self.lineEdit_user.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.lineEdit_user, 1, 0, 1, 1)

        self.txt_user = QLabel(self.gp_user)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy1)
        self.txt_user.setFont(font2)
        self.txt_user.setStyleSheet(u"color: rgb(232, 241, 242);")
        self.txt_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_user, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gp_user, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Botao_entrar.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.lineEdit_senha.setText("")
        self.txt_senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.lineEdit_user.setText("")
        self.txt_user.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
    # retranslateUi

