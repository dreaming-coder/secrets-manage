# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateAccountPage.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_createAccountPage(object):
    def setupUi(self, createAccountPage):
        if not createAccountPage.objectName():
            createAccountPage.setObjectName(u"createAccountPage")
        createAccountPage.setWindowModality(Qt.ApplicationModal)
        createAccountPage.resize(250, 250)
        createAccountPage.setMinimumSize(QSize(250, 250))
        createAccountPage.setMaximumSize(QSize(250, 250))
        self.horizontalLayout = QHBoxLayout(createAccountPage)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.createAccountFrame = QFrame(createAccountPage)
        self.createAccountFrame.setObjectName(u"createAccountFrame")
        self.createAccountFrame.setFrameShape(QFrame.StyledPanel)
        self.createAccountFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.createAccountFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 15, 18, 12)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setVerticalSpacing(10)
        self.label = QLabel(self.createAccountFrame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.phoneLineEdit = QLineEdit(self.createAccountFrame)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        self.phoneLineEdit.setMinimumSize(QSize(0, 25))
        self.phoneLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.phoneLineEdit.setMaxLength(11)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.phoneLineEdit)

        self.label_2 = QLabel(self.createAccountFrame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.emailLineEdit = QLineEdit(self.createAccountFrame)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setMinimumSize(QSize(0, 25))
        self.emailLineEdit.setContextMenuPolicy(Qt.NoContextMenu)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.emailLineEdit)

        self.label_3 = QLabel(self.createAccountFrame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.nameLineEdit = QLineEdit(self.createAccountFrame)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setMinimumSize(QSize(0, 25))
        self.nameLineEdit.setContextMenuPolicy(Qt.NoContextMenu)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.nameLineEdit)

        self.label_4 = QLabel(self.createAccountFrame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.passwordLineEdit1 = QLineEdit(self.createAccountFrame)
        self.passwordLineEdit1.setObjectName(u"passwordLineEdit1")
        self.passwordLineEdit1.setMinimumSize(QSize(0, 25))
        self.passwordLineEdit1.setContextMenuPolicy(Qt.NoContextMenu)
        self.passwordLineEdit1.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.passwordLineEdit1)

        self.label_5 = QLabel(self.createAccountFrame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.passwordLineEdit2 = QLineEdit(self.createAccountFrame)
        self.passwordLineEdit2.setObjectName(u"passwordLineEdit2")
        self.passwordLineEdit2.setMinimumSize(QSize(0, 25))
        self.passwordLineEdit2.setContextMenuPolicy(Qt.NoContextMenu)
        self.passwordLineEdit2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.passwordLineEdit2)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.createPushButton = QPushButton(self.createAccountFrame)
        self.createPushButton.setObjectName(u"createPushButton")
        self.createPushButton.setMinimumSize(QSize(0, 30))
        self.createPushButton.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.createPushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 20)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 7)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)

        self.horizontalLayout.addWidget(self.createAccountFrame)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.phoneLineEdit)
        self.label_2.setBuddy(self.emailLineEdit)
        self.label_3.setBuddy(self.nameLineEdit)
        self.label_4.setBuddy(self.passwordLineEdit1)
        self.label_5.setBuddy(self.passwordLineEdit2)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(createAccountPage)

        QMetaObject.connectSlotsByName(createAccountPage)
    # setupUi

    def retranslateUi(self, createAccountPage):
        createAccountPage.setWindowTitle(QCoreApplication.translate("createAccountPage", u"\u521b\u5efa\u8d26\u6237", None))
        self.label.setText(QCoreApplication.translate("createAccountPage", u"\u624b\u673a\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("createAccountPage", u"\u90ae\u7bb1\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("createAccountPage", u"\u6635\u79f0\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("createAccountPage", u"\u5bc6\u7801\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("createAccountPage", u"\u91cd\u590d\u5bc6\u7801\uff1a", None))
        self.createPushButton.setText(QCoreApplication.translate("createAccountPage", u"\u521b\u5efa", None))
    # retranslateUi

