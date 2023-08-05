# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddItemPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_addItemPage(object):
    def setupUi(self, addItemPage):
        if not addItemPage.objectName():
            addItemPage.setObjectName(u"addItemPage")
        addItemPage.resize(300, 400)
        addItemPage.setMinimumSize(QSize(300, 400))
        addItemPage.setMaximumSize(QSize(300, 400))
        self.verticalLayout = QVBoxLayout(addItemPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.addItemFrame = QFrame(addItemPage)
        self.addItemFrame.setObjectName(u"addItemFrame")
        self.addItemFrame.setFrameShape(QFrame.StyledPanel)
        self.addItemFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.addItemFrame)
        self.verticalLayout_3.setSpacing(23)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(35, 25, 35, 40)
        self.titleLabel = QLabel(self.addItemFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.titleLabel)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.nameLineEdit = QLineEdit(self.addItemFrame)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setMinimumSize(QSize(0, 40))
        self.nameLineEdit.setMaximumSize(QSize(16777215, 40))
        self.nameLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.nameLineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.nameLineEdit)

        self.accountLineEdit = QLineEdit(self.addItemFrame)
        self.accountLineEdit.setObjectName(u"accountLineEdit")
        self.accountLineEdit.setMinimumSize(QSize(0, 40))
        self.accountLineEdit.setMaximumSize(QSize(16777215, 40))
        self.accountLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.accountLineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.accountLineEdit)

        self.passwordLineEdit = QLineEdit(self.addItemFrame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setMinimumSize(QSize(0, 40))
        self.passwordLineEdit.setMaximumSize(QSize(16777215, 40))
        self.passwordLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.passwordLineEdit)

        self.describeLineEdit = QLineEdit(self.addItemFrame)
        self.describeLineEdit.setObjectName(u"describeLineEdit")
        self.describeLineEdit.setMinimumSize(QSize(0, 40))
        self.describeLineEdit.setMaximumSize(QSize(16777215, 40))
        self.describeLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.describeLineEdit.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.describeLineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addPushButton = QPushButton(self.addItemFrame)
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setMinimumSize(QSize(0, 40))
        self.addPushButton.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.addPushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.addPushButton)

        self.clearPushButton = QPushButton(self.addItemFrame)
        self.clearPushButton.setObjectName(u"clearPushButton")
        self.clearPushButton.setMinimumSize(QSize(0, 40))
        self.clearPushButton.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.clearPushButton.setFont(font2)

        self.horizontalLayout.addWidget(self.clearPushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(1, 10)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.addItemFrame)


        self.retranslateUi(addItemPage)
        self.clearPushButton.clicked.connect(addItemPage.close)

        QMetaObject.connectSlotsByName(addItemPage)
    # setupUi

    def retranslateUi(self, addItemPage):
        addItemPage.setWindowTitle("")
        self.titleLabel.setText(QCoreApplication.translate("addItemPage", u"\u65b0\u589e\u8d26\u53f7/\u5bc6\u7801", None))
        self.nameLineEdit.setPlaceholderText(QCoreApplication.translate("addItemPage", u"\u8bf7\u8f93\u5165\u8d26\u53f7\u540d\u79f0", None))
        self.accountLineEdit.setPlaceholderText(QCoreApplication.translate("addItemPage", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("addItemPage", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.describeLineEdit.setPlaceholderText(QCoreApplication.translate("addItemPage", u"\u8bf7\u8f93\u5165\u5907\u6ce8\u4fe1\u606f", None))
        self.addPushButton.setText(QCoreApplication.translate("addItemPage", u"\u65b0  \u589e", None))
        self.clearPushButton.setText(QCoreApplication.translate("addItemPage", u"\u9000  \u51fa", None))
    # retranslateUi

