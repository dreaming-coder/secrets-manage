# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_loginPage(object):
    def setupUi(self, loginPage):
        if not loginPage.objectName():
            loginPage.setObjectName(u"loginPage")
        loginPage.resize(350, 182)
        loginPage.setMinimumSize(QSize(350, 182))
        loginPage.setMaximumSize(QSize(350, 182))
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        loginPage.setFont(font)
        loginPage.setStyleSheet(u"")
        self.backgroundFrame = QFrame(loginPage)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setGeometry(QRect(0, 0, 350, 182))
        self.backgroundFrame.setMinimumSize(QSize(350, 182))
        self.backgroundFrame.setMaximumSize(QSize(350, 182))
        self.backgroundFrame.setStyleSheet(u"")
        self.backgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.backgroundFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.backgroundFrame)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_6.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_6.setFormAlignment(Qt.AlignCenter)
        self.formLayout_6.setVerticalSpacing(8)
        self.formLayout_6.setContentsMargins(50, 0, 80, -1)
        self.account = QLabel(self.backgroundFrame)
        self.account.setObjectName(u"account")
        self.account.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.account.setFont(font2)
        self.account.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.account)

        self.password = QLabel(self.backgroundFrame)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 20))
        self.password.setFont(font2)
        self.password.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.password)

        self.passwordLineEdit = QLineEdit(self.backgroundFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setMinimumSize(QSize(0, 20))
        self.passwordLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.passwordLineEdit)

        self.accountLineEdit = QLineEdit(self.backgroundFrame)
        self.accountLineEdit.setObjectName(u"accountLineEdit")
        self.accountLineEdit.setMinimumSize(QSize(0, 20))
        self.accountLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.accountLineEdit.setClearButtonEnabled(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.accountLineEdit)


        self.verticalLayout.addLayout(self.formLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(60, -1, 50, 10)
        self.forgetPwd = QPushButton(self.backgroundFrame)
        self.forgetPwd.setObjectName(u"forgetPwd")
        self.forgetPwd.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgetPwd.setStyleSheet(u"")
        self.forgetPwd.setCheckable(False)

        self.horizontalLayout_5.addWidget(self.forgetPwd)

        self.createAccount = QPushButton(self.backgroundFrame)
        self.createAccount.setObjectName(u"createAccount")
        self.createAccount.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.createAccount)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        QWidget.setTabOrder(self.accountLineEdit, self.passwordLineEdit)
        QWidget.setTabOrder(self.passwordLineEdit, self.forgetPwd)
        QWidget.setTabOrder(self.forgetPwd, self.createAccount)

        self.retranslateUi(loginPage)

        QMetaObject.connectSlotsByName(loginPage)
    # setupUi

    def retranslateUi(self, loginPage):
        loginPage.setWindowTitle(QCoreApplication.translate("loginPage", u"\u5bc6\u7801\u7ba1\u7406\u5668", None))
        self.title.setText(QCoreApplication.translate("loginPage", u"\u5bc6\u7801\u7ba1\u7406\u5668", None))
        self.account.setText(QCoreApplication.translate("loginPage", u"\u8d26\u53f7\uff1a", None))
        self.password.setText(QCoreApplication.translate("loginPage", u"\u5bc6\u7801\uff1a", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("loginPage", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.accountLineEdit.setPlaceholderText(QCoreApplication.translate("loginPage", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7/\u90ae\u7bb1", None))
        self.forgetPwd.setText(QCoreApplication.translate("loginPage", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.createAccount.setText(QCoreApplication.translate("loginPage", u"\u521b\u5efa\u8d26\u6237", None))
    # retranslateUi

