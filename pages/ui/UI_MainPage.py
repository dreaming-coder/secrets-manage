# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainPage.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_mainPage(object):
    def setupUi(self, mainPage):
        if not mainPage.objectName():
            mainPage.setObjectName(u"mainPage")
        mainPage.resize(800, 400)
        mainPage.setMinimumSize(QSize(800, 400))
        mainPage.setMaximumSize(QSize(800, 400))
        self.centralwidget = QWidget(mainPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 5, 15, 5)
        self.addPushButton = QPushButton(self.frame_2)
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setMinimumSize(QSize(0, 30))
        self.addPushButton.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.addPushButton)

        self.horizontalSpacer_2 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.deletePushButton = QPushButton(self.frame_2)
        self.deletePushButton.setObjectName(u"deletePushButton")
        self.deletePushButton.setMinimumSize(QSize(0, 30))
        self.deletePushButton.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.deletePushButton)

        self.horizontalSpacer_3 = QSpacerItem(16, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 7, -1)
        self.conditionLabel = QLabel(self.frame_2)
        self.conditionLabel.setObjectName(u"conditionLabel")
        self.conditionLabel.setMinimumSize(QSize(0, 30))
        self.conditionLabel.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(11)
        font.setBold(False)
        self.conditionLabel.setFont(font)

        self.horizontalLayout.addWidget(self.conditionLabel)

        self.conditionCombox = QComboBox(self.frame_2)
        self.conditionCombox.addItem("")
        self.conditionCombox.addItem("")
        self.conditionCombox.addItem("")
        self.conditionCombox.addItem("")
        self.conditionCombox.setObjectName(u"conditionCombox")
        self.conditionCombox.setMinimumSize(QSize(140, 30))
        self.conditionCombox.setMaximumSize(QSize(140, 30))

        self.horizontalLayout.addWidget(self.conditionCombox)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.contidionLineEdit = QLineEdit(self.frame_2)
        self.contidionLineEdit.setObjectName(u"contidionLineEdit")
        self.contidionLineEdit.setMinimumSize(QSize(180, 30))
        self.contidionLineEdit.setMaximumSize(QSize(180, 30))
        self.contidionLineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.contidionLineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.contidionLineEdit)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.searchPushButton = QPushButton(self.frame_2)
        self.searchPushButton.setObjectName(u"searchPushButton")
        self.searchPushButton.setMinimumSize(QSize(30, 30))
        self.searchPushButton.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.searchPushButton)

        self.resetPushButton = QPushButton(self.frame_2)
        self.resetPushButton.setObjectName(u"resetPushButton")
        self.resetPushButton.setMinimumSize(QSize(80, 30))
        self.resetPushButton.setMaximumSize(QSize(80, 30))

        self.horizontalLayout_3.addWidget(self.resetPushButton)

        self.horizontalLayout_3.setStretch(0, 7)
        self.horizontalLayout_3.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 3)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 20)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)

        self.verticalLayout.addWidget(self.frame)

        mainPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainPage)

        QMetaObject.connectSlotsByName(mainPage)
    # setupUi

    def retranslateUi(self, mainPage):
        mainPage.setWindowTitle("")
        self.addPushButton.setText(QCoreApplication.translate("mainPage", u"\u589e\u52a0", None))
        self.deletePushButton.setText(QCoreApplication.translate("mainPage", u"\u5220\u9664", None))
        self.conditionLabel.setText(QCoreApplication.translate("mainPage", u"\u68c0\u7d22\u6761\u4ef6\uff1a", None))
        self.conditionCombox.setItemText(0, QCoreApplication.translate("mainPage", u"\u5168\u90e8", None))
        self.conditionCombox.setItemText(1, QCoreApplication.translate("mainPage", u"\u540d\u79f0", None))
        self.conditionCombox.setItemText(2, QCoreApplication.translate("mainPage", u"\u8d26\u53f7", None))
        self.conditionCombox.setItemText(3, QCoreApplication.translate("mainPage", u"\u5907\u6ce8", None))

        self.contidionLineEdit.setPlaceholderText(QCoreApplication.translate("mainPage", u"\u8bf7\u8f93\u5165\u5173\u952e\u8bcd", None))
#if QT_CONFIG(tooltip)
        self.searchPushButton.setToolTip(QCoreApplication.translate("mainPage", u"\u67e5\u627e", None))
#endif // QT_CONFIG(tooltip)
        self.searchPushButton.setText("")
        self.resetPushButton.setText(QCoreApplication.translate("mainPage", u"\u91cd\u7f6e", None))
    # retranslateUi

