import hashlib
import re

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QWidget, QLineEdit, QMessageBox

from dao import UserDao
from utils import Loader
from .CreateAccountPage import CreateAccountPage
from .MainPage import MainPage
from .UpdatePasswordPage import UpdatePasswordPage
from .ui import Ui_loginPage


class LoginPage(QWidget, Ui_loginPage):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.create_page = None
        self.update_password_page = None
        self.main_page = None
        self.user_dao = UserDao()

        self.setupUi(self)

        # 设置窗体按钮样式
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)

        self.setStyleSheet(Loader.loadQSS(":/styles/styles/LoginPage.qss"))

        self.action = QAction(self.passwordLineEdit)
        self.action.setIcon(QIcon(":/icons/icons/enter.png"))
        self.passwordLineEdit.addAction(self.action, QLineEdit.ActionPosition.TrailingPosition)

        self.bind()

    def bind(self):
        self.createAccount.clicked.connect(self.show_create_account_page)
        self.forgetPwd.clicked.connect(self.show_update_password_page)
        self.action.triggered.connect(self.log_in)

    def show_create_account_page(self):
        self.create_page = CreateAccountPage()
        self.create_page.show()

    def show_update_password_page(self):
        self.update_password_page = UpdatePasswordPage()
        self.update_password_page.closed.connect(lambda: self.accountLineEdit.setFocus())
        self.update_password_page.show()

    def log_in(self):
        account = self.accountLineEdit.text()
        password = self.passwordLineEdit.text()

        if account is None or account == "":
            QMessageBox.warning(self, '警告', '请输入账号！',
                                QMessageBox.StandardButton.Ok)
            self.accountLineEdit.setFocus()
            return
        elif password is None or password == "":
            QMessageBox.warning(self, '警告', '请输入密码！',
                                QMessageBox.StandardButton.Ok)
            self.passwordLineEdit.setFocus()
            return
        elif re.match(r"^\d{11}$", account):
            user = self.user_dao.get_user_by_phone(account)
        elif re.match(r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", account):
            user = self.user_dao.get_user_by_email(account)
        else:
            QMessageBox.warning(self, '警告', '该账号不存在！',
                                QMessageBox.StandardButton.Ok)
            self.accountLineEdit.clear()
            self.passwordLineEdit.clear()
            self.accountLineEdit.setFocus()
            return

        if user is None:
            QMessageBox.warning(self, '警告', '该账号不存在！',
                                QMessageBox.StandardButton.Ok)
            self.accountLineEdit.clear()
            self.passwordLineEdit.clear()
            self.accountLineEdit.setFocus()
            return

        md5 = hashlib.md5()
        md5.update(password.encode(encoding="utf-8"))

        if md5.hexdigest() == user.password:
            self.main_page = MainPage(cur_user=user)
            self.main_page.show()
            self.hide()
        else:
            QMessageBox.warning(self, '警告', '密码错误，请重新输入！',
                                QMessageBox.StandardButton.Ok)
            self.passwordLineEdit.clear()
            self.passwordLineEdit.setFocus()

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key.Key_Enter or key_event.key() == Qt.Key.Key_Return:
            self.log_in()
