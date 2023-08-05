import hashlib
import re
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit

from dao import UserDao
from entity import User
from utils import PhoneValidator, EmailValidator, PasswordValidator, Loader
from .ui import Ui_createAccountPage


# noinspection PyAttributeOutsideInit,DuplicatedCode
class CreateAccountPage(QWidget, Ui_createAccountPage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.user_dao = UserDao()

        self.setupUi(self)

        # 设置窗体按钮样式
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self.setStyleSheet(Loader.loadQSS(":/styles/styles/CreateAccountPage.qss"))

        # 创建校验器
        self.phone_validator = PhoneValidator()
        self.email_validator = EmailValidator()
        self.password_validator = PasswordValidator()

        # 对文本框进行输入校验
        self.phoneLineEdit.setValidator(self.phone_validator)
        self.emailLineEdit.setValidator(self.email_validator)
        self.passwordLineEdit1.setValidator(self.password_validator)
        self.passwordLineEdit2.setValidator(self.password_validator)

        self.set_toggle_echo_mode()

        # 绑定信号与槽
        self.bind()

    def bind(self):
        self.passwordLineEdit2.textChanged.connect(self.compare_pwd)
        self.createPushButton.clicked.connect(self.create_user)

    def set_toggle_echo_mode(self):
        # 设置密码框明密文切换
        self.action1 = QAction(self.passwordLineEdit1)
        self.action1.setIcon(QIcon(":/icons/icons/eye-close.png"))
        self.passwordLineEdit1.addAction(self.action1, QLineEdit.ActionPosition.TrailingPosition)

        self.action2 = QAction(self.passwordLineEdit2)
        self.action2.setIcon(QIcon(":/icons/icons/eye-close.png"))
        self.passwordLineEdit2.addAction(self.action2, QLineEdit.ActionPosition.TrailingPosition)

        self.action1.triggered.connect(self.toggle_echo_mode_1)
        self.action2.triggered.connect(self.toggle_echo_mode_2)

    def compare_pwd(self, text):
        """比较两次密码是否输入一致"""
        if not self.passwordLineEdit1.text().startswith(text):
            self.passwordLineEdit2.setStyleSheet("color: red")
            QMessageBox.warning(self, '警告', '两次密码不一致！',
                                QMessageBox.StandardButton.Ok)
            self.passwordLineEdit2.setText("")
        else:
            self.passwordLineEdit2.setStyleSheet("color: black")

    def create_user(self):
        phone = self.phoneLineEdit.text()
        email = self.emailLineEdit.text()
        name = self.nameLineEdit.text()
        password1 = self.passwordLineEdit1.text()
        password2 = self.passwordLineEdit2.text()

        if not re.match(r'^\d{11}$', phone):
            QMessageBox.warning(self, '警告', '请输入正确的手机号码！',
                                QMessageBox.StandardButton.Ok)
            self.phoneLineEdit.setText("")
            self.phoneLineEdit.setFocus()
        elif not re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email):
            QMessageBox.warning(self, '警告', '请输入正确的电子邮箱！',
                                QMessageBox.StandardButton.Ok)
            self.emailLineEdit.setText("")
            self.emailLineEdit.setFocus()
        elif name is None or name == "":
            QMessageBox.warning(self, '警告', '请输入昵称！',
                                QMessageBox.StandardButton.Ok)
            self.nameLineEdit.setFocus()
        elif password1 is None or password1 == "":
            QMessageBox.warning(self, '警告', '请输入密码！',
                                QMessageBox.StandardButton.Ok)
            self.passwordLineEdit1.setFocus()
        elif password1 != password2:
            QMessageBox.warning(self, '警告', '两次密码不一致！',
                                QMessageBox.StandardButton.Ok)
            self.passwordLineEdit2.setText("")
            self.passwordLineEdit2.setFocus()
        else:

            md5 = hashlib.md5()
            md5.update(password2.encode("utf-8"))

            # 创建实体对象
            user = User(phone=phone, email=email, name=name, password=md5.hexdigest())

            self.user_dao.add_user(user, success_func=self.close, except_func=self.create_user_failed)

    def create_user_failed(self):
        """创建用户失败，清空所有信息"""
        QMessageBox.critical(self, '警告', '创建用户失败，手机号码/电子邮箱已经注册！',
                             QMessageBox.StandardButton.Ok)
        self.phoneLineEdit.setText("")
        self.emailLineEdit.setText("")
        self.nameLineEdit.setText("")
        self.passwordLineEdit1.setText("")
        self.passwordLineEdit2.setText("")
        self.phoneLineEdit.setFocus()

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key.Key_Enter or key_event.key() == Qt.Key.Key_Return:
            self.createPushButton.click()
        elif key_event.key() == Qt.Key.Key_Escape:
            self.close()

    def toggle_echo_mode_1(self):
        if self.passwordLineEdit1.echoMode() == QLineEdit.EchoMode.Password:
            self.passwordLineEdit1.setEchoMode(QLineEdit.EchoMode.Normal)
            self.action1.setIcon(QIcon(":/icons/icons/eye-open.png"))
        else:
            self.passwordLineEdit1.setEchoMode(QLineEdit.EchoMode.Password)
            self.action1.setIcon(QIcon(":/icons/icons/eye-close.png"))

    def toggle_echo_mode_2(self):
        if self.passwordLineEdit2.echoMode() == QLineEdit.EchoMode.Password:
            self.passwordLineEdit2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.action2.setIcon(QIcon(":/icons/icons/eye-open.png"))
        else:
            self.passwordLineEdit2.setEchoMode(QLineEdit.EchoMode.Password)
            self.action2.setIcon(QIcon(":/icons/icons/eye-close.png"))
