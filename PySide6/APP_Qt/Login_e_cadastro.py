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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import imagensLogin_rc

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(798, 596)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DockWidget.sizePolicy().hasHeightForWidth())
        DockWidget.setSizePolicy(sizePolicy)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.dockWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setGeometry(QRect(290, 150, 258, 282))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMouseTracking(False)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gp_user = QFrame(self.frame_3)
        self.gp_user.setObjectName(u"gp_user")
        self.gp_user.setEnabled(True)
        sizePolicy.setHeightForWidth(self.gp_user.sizePolicy().hasHeightForWidth())
        self.gp_user.setSizePolicy(sizePolicy)
        self.gp_user.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_user.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.gp_user)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_user = QLineEdit(self.gp_user)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_user.setSizePolicy(sizePolicy)
        self.lineEdit_user.setMinimumSize(QSize(150, 30))
        self.lineEdit_user.setMaximumSize(QSize(400, 50))
        font = QFont()
        font.setPointSize(18)
        self.lineEdit_user.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_user, 1, 0, 1, 1)

        self.txt_user = QLabel(self.gp_user)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setEnabled(True)
        sizePolicy.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.txt_user.setFont(font1)
        self.txt_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_user, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gp_user, 0, 0, 1, 1)

        self.Botao_entrar = QPushButton(self.frame_3)
        self.Botao_entrar.setObjectName(u"Botao_entrar")
        self.Botao_entrar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Botao_entrar.sizePolicy().hasHeightForWidth())
        self.Botao_entrar.setSizePolicy(sizePolicy)
        self.Botao_entrar.setMaximumSize(QSize(300, 50))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.Botao_entrar.setFont(font2)
        self.Botao_entrar.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.Botao_entrar.setIconSize(QSize(16, 16))
        self.Botao_entrar.setAutoDefault(False)
        self.Botao_entrar.setFlat(False)

        self.gridLayout_4.addWidget(self.Botao_entrar, 2, 0, 1, 1)

        self.gp_senha = QFrame(self.frame_3)
        self.gp_senha.setObjectName(u"gp_senha")
        self.gp_senha.setEnabled(True)
        sizePolicy.setHeightForWidth(self.gp_senha.sizePolicy().hasHeightForWidth())
        self.gp_senha.setSizePolicy(sizePolicy)
        self.gp_senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.gp_senha.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.gp_senha)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_senha = QLineEdit(self.gp_senha)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lineEdit_senha.sizePolicy().hasHeightForWidth())
        self.lineEdit_senha.setSizePolicy(sizePolicy)
        self.lineEdit_senha.setMinimumSize(QSize(170, 30))
        self.lineEdit_senha.setMaximumSize(QSize(400, 50))
        self.lineEdit_senha.setFont(font)
        self.lineEdit_senha.setCursor(QCursor(Qt.CursorShape.SizeHorCursor))
        self.lineEdit_senha.setInputMethodHints(Qt.InputMethodHint.ImhNoAutoUppercase|Qt.InputMethodHint.ImhNoPredictiveText|Qt.InputMethodHint.ImhSensitiveData)
        self.lineEdit_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.lineEdit_senha, 1, 0, 1, 1)

        self.txt_senha = QLabel(self.gp_senha)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEnabled(True)
        sizePolicy.setHeightForWidth(self.txt_senha.sizePolicy().hasHeightForWidth())
        self.txt_senha.setSizePolicy(sizePolicy)
        self.txt_senha.setFont(font1)
        self.txt_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_senha, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gp_senha, 1, 0, 1, 1)

        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/Login/fundo.jpg"))
        self.label.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.label.raise_()
        self.frame_3.raise_()

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        self.Botao_entrar.setDefault(False)


        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.lineEdit_user.setText("")
        self.txt_user.setText(QCoreApplication.translate("DockWidget", u"Usuario", None))
        self.Botao_entrar.setText(QCoreApplication.translate("DockWidget", u"Entrar", None))
        self.lineEdit_senha.setText("")
        self.txt_senha.setText(QCoreApplication.translate("DockWidget", u"Senha", None))
        self.label.setText("")
    # retranslateUi

