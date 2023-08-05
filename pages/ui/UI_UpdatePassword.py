# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdatePassword.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_updatePage(object):
    def setupUi(self, updatePage):
        if not updatePage.objectName():
            updatePage.setObjectName(u"updatePage")
        updatePage.setWindowModality(Qt.ApplicationModal)
        updatePage.resize(250, 280)
        updatePage.setMinimumSize(QSize(250, 280))
        updatePage.setMaximumSize(QSize(250, 280))
        self.verticalLayout = QVBoxLayout(updatePage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(updatePage)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 247))
        self.stackedWidget.setStyleSheet(u"")
        self.inputAccount = QWidget()
        self.inputAccount.setObjectName(u"inputAccount")
        self.verticalLayout_2 = QVBoxLayout(self.inputAccount)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, 20)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.label = QLabel(self.inputAccount)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setOpenExternalLinks(False)

        self.horizontalLayout_7.addWidget(self.label)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 40)
        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.accountLineEdit = QLineEdit(self.inputAccount)
        self.accountLineEdit.setObjectName(u"accountLineEdit")
        self.accountLineEdit.setMinimumSize(QSize(0, 30))
        self.accountLineEdit.setMaximumSize(QSize(50000, 30))
        self.accountLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.accountLineEdit.setEchoMode(QLineEdit.Normal)
        self.accountLineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.accountLineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.accountLineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 20)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_25)

        self.tipLabel = QLabel(self.inputAccount)
        self.tipLabel.setObjectName(u"tipLabel")
        self.tipLabel.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.tipLabel)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_26)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.nextPushButton = QPushButton(self.inputAccount)
        self.nextPushButton.setObjectName(u"nextPushButton")
        self.nextPushButton.setEnabled(False)
        self.nextPushButton.setMinimumSize(QSize(160, 30))

        self.horizontalLayout_2.addWidget(self.nextPushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 8)
        self.verticalLayout_2.setStretch(6, 1)
        self.stackedWidget.addWidget(self.inputAccount)
        self.validateAccount = QWidget()
        self.validateAccount.setObjectName(u"validateAccount")
        self.verticalLayout_3 = QVBoxLayout(self.validateAccount)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, 20)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.validateAccount)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.label_2.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_6 = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.validateAccountLineEdit = QLineEdit(self.validateAccount)
        self.validateAccountLineEdit.setObjectName(u"validateAccountLineEdit")
        self.validateAccountLineEdit.setMinimumSize(QSize(0, 30))
        self.validateAccountLineEdit.setMaximumSize(QSize(16777215, 30))
        self.validateAccountLineEdit.setContextMenuPolicy(Qt.NoContextMenu)

        self.horizontalLayout_4.addWidget(self.validateAccountLineEdit)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 20)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_7 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.validatePasswordLineEdit = QLineEdit(self.validateAccount)
        self.validatePasswordLineEdit.setObjectName(u"validatePasswordLineEdit")
        self.validatePasswordLineEdit.setMinimumSize(QSize(0, 30))
        self.validatePasswordLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.validatePasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.validatePasswordLineEdit)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 20)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_8 = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.validatePushButton = QPushButton(self.validateAccount)
        self.validatePushButton.setObjectName(u"validatePushButton")
        self.validatePushButton.setMinimumSize(QSize(160, 30))

        self.horizontalLayout_6.addWidget(self.validatePushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.validateAccount)
        self.updatePassword = QWidget()
        self.updatePassword.setObjectName(u"updatePassword")
        self.verticalLayout_4 = QVBoxLayout(self.updatePassword)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 6, -1, 20)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.label_3 = QLabel(self.updatePassword)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 40)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_19)

        self.newPwd1 = QLineEdit(self.updatePassword)
        self.newPwd1.setObjectName(u"newPwd1")
        self.newPwd1.setMinimumSize(QSize(0, 30))
        self.newPwd1.setMaximumSize(QSize(16777215, 30))
        self.newPwd1.setContextMenuPolicy(Qt.NoContextMenu)
        self.newPwd1.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_11.addWidget(self.newPwd1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_20)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 20)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)

        self.label_4 = QLabel(self.updatePassword)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 40)
        self.horizontalLayout_9.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_21)

        self.newPwd2 = QLineEdit(self.updatePassword)
        self.newPwd2.setObjectName(u"newPwd2")
        self.newPwd2.setMinimumSize(QSize(0, 30))
        self.newPwd2.setContextMenuPolicy(Qt.NoContextMenu)
        self.newPwd2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_10.addWidget(self.newPwd2)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_22)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 20)
        self.horizontalLayout_10.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_9 = QSpacerItem(20, 26, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_23)

        self.updatePushButton = QPushButton(self.updatePassword)
        self.updatePushButton.setObjectName(u"updatePushButton")
        self.updatePushButton.setMinimumSize(QSize(160, 30))

        self.horizontalLayout_12.addWidget(self.updatePushButton)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 4)
        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.verticalLayout_4.setStretch(0, 4)
        self.verticalLayout_4.setStretch(1, 4)
        self.verticalLayout_4.setStretch(2, 4)
        self.verticalLayout_4.setStretch(3, 4)
        self.verticalLayout_4.setStretch(4, 3)
        self.verticalLayout_4.setStretch(5, 4)
        self.stackedWidget.addWidget(self.updatePassword)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(updatePage)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(updatePage)
    # setupUi

    def retranslateUi(self, updatePage):
        updatePage.setWindowTitle(QCoreApplication.translate("updatePage", u"\u4fee\u6539\u5bc6\u7801", None))
        self.label.setText(QCoreApplication.translate("updatePage", u"\u8bf7\u8f93\u5165\u8d26\u53f7\uff1a", None))
        self.accountLineEdit.setPlaceholderText(QCoreApplication.translate("updatePage", u"\u624b\u673a\u53f7/\u90ae\u7bb1", None))
        self.tipLabel.setText(QCoreApplication.translate("updatePage", u"\u8d26\u53f7\u662f\u4fee\u6539\u5bc6\u7801\u7684\u5fc5\u8981\u4fe1\u606f\uff0c\u5982\u65e0\u6cd5\u63d0\u4f9b\u8bf7\u81ea\u884c\u91cd\u65b0\u6ce8\u518c\u8d26\u53f7\u3002", None))
        self.nextPushButton.setText(QCoreApplication.translate("updatePage", u"\u4e0b\u4e00\u6b65", None))
        self.label_2.setText(QCoreApplication.translate("updatePage", u"\u8bf7\u8f93\u5165\u4efb\u610f\u4e00\u7ec4\u5b58\u50a8\u7684\u8d26\u53f7\n"
"\u548c\u5bc6\u7801\uff1a", None))
        self.validateAccountLineEdit.setPlaceholderText(QCoreApplication.translate("updatePage", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.validatePasswordLineEdit.setPlaceholderText(QCoreApplication.translate("updatePage", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.validatePushButton.setText(QCoreApplication.translate("updatePage", u"\u9a8c\u8bc1", None))
        self.label_3.setText(QCoreApplication.translate("updatePage", u"\u8bf7\u8f93\u5165\u65b0\u7684\u5bc6\u7801\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("updatePage", u"\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a", None))
        self.updatePushButton.setText(QCoreApplication.translate("updatePage", u"\u5b8c\u6210", None))
    # retranslateUi

