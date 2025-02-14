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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import imagemTeste1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 596)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(150, 25))
        self.frame_5.setMaximumSize(QSize(300, 50))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Botao_entrar = QPushButton(self.frame_5)
        self.Botao_entrar.setObjectName(u"Botao_entrar")
        self.Botao_entrar.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Botao_entrar.sizePolicy().hasHeightForWidth())
        self.Botao_entrar.setSizePolicy(sizePolicy)
        self.Botao_entrar.setMinimumSize(QSize(150, 25))
        self.Botao_entrar.setMaximumSize(QSize(300, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.Botao_entrar.setFont(font)
        self.Botao_entrar.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.Botao_entrar.setIconSize(QSize(16, 16))
        self.Botao_entrar.setAutoDefault(False)
        self.Botao_entrar.setFlat(False)

        self.verticalLayout_2.addWidget(self.Botao_entrar)


        self.gridLayout.addWidget(self.frame_5, 7, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(52, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(400, 0))
        self.lineEdit.setMaximumSize(QSize(600, 20))

        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 3)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(100, 500))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(30, 15))
        self.label_6.setMaximumSize(QSize(35, 15))
        self.label_6.setFont(font1)

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(50, 0))
        self.lineEdit_4.setMaximumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.lineEdit_4, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_7, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 7, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(52, 20))
        self.label_2.setMaximumSize(QSize(52, 20))
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(100, 0))
        self.lineEdit_2.setMaximumSize(QSize(200, 20))

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 7, 5, 1, 1)

        self.txt_Cadastro = QLabel(self.centralwidget)
        self.txt_Cadastro.setObjectName(u"txt_Cadastro")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.txt_Cadastro.setFont(font2)

        self.gridLayout.addWidget(self.txt_Cadastro, 0, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(52, 20))
        self.label_7.setFont(font1)

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(400, 0))
        self.lineEdit_5.setMaximumSize(QSize(600, 20))

        self.gridLayout_8.addWidget(self.lineEdit_5, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_8, 2, 3, 1, 3)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.frame_6)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_6.addWidget(self.radioButton_3, 0, 1, 1, 1)

        self.radioButton = QRadioButton(self.frame_6)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_6.addWidget(self.radioButton, 0, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self.frame_6)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_6.addWidget(self.radioButton_2, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.frame_6, 6, 1, 1, 3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 20))
        self.label_4.setMaximumSize(QSize(125, 20))
        self.label_4.setFont(font1)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.dateEdit, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 4, 1, 1, 3)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(52, 20))
        self.label_3.setMaximumSize(QSize(52, 20))
        self.label_3.setFont(font1)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(100, 0))
        self.lineEdit_3.setMaximumSize(QSize(200, 20))

        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 3, 2, 1, 2)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(69, 20))
        self.label_8.setFont(font1)

        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(325, 0))
        self.lineEdit_6.setMaximumSize(QSize(300, 20))

        self.gridLayout_9.addWidget(self.lineEdit_6, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_9, 5, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Botao_entrar.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DDD:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.txt_Cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
    # retranslateUi

