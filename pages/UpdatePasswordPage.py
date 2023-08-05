import hashlib
import re

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QWidget, QMessageBox, QLineEdit

from dao import UserDao, ItemDao
from utils import AccountValidator, decrypt, PasswordValidator, Loader
from .ui import Ui_updatePage


# noinspection PyAttributeOutsideInit,DuplicatedCode
class UpdatePasswordPage(QWidget, Ui_updatePage):
    closed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.cur_user = None  # 当前用户
        self.user_dao = UserDao()
        self.pwd_dao = ItemDao()

        self.setupUi(self)

        # 设置窗体按钮样式
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self.setStyleSheet(Loader.loadQSS(":/styles/styles/UpdatePasswordPage.qss"))

        # 账号限制手机号或电子邮箱
        self.account_validator = AccountValidator()
        self.accountLineEdit.setValidator(self.account_validator)

        # 密码限制
        self.password_validator = PasswordValidator()
        self.newPwd1.setValidator(self.password_validator)
        self.newPwd2.setValidator(self.password_validator)

        self.set_toggle_echo_mode()

        self.bind()

    def set_toggle_echo_mode(self):
        """设置密码框明密文切换"""
        self.validatePasswordLineEditAction = QAction(self.validatePasswordLineEdit)
        self.newPwd1Action = QAction(self.newPwd1)
        self.newPwd2Action = QAction(self.newPwd2)

        self.validatePasswordLineEditAction.setIcon(QIcon(":/icons/icons/eye-close.png"))
        self.newPwd1Action.setIcon(QIcon(":/icons/icons/eye-close.png"))
        self.newPwd2Action.setIcon(QIcon(":/icons/icons/eye-close.png"))

        self.validatePasswordLineEdit.addAction(self.validatePasswordLineEditAction, QLineEdit.ActionPosition.TrailingPosition)
        self.newPwd1.addAction(self.newPwd1Action, QLineEdit.ActionPosition.TrailingPosition)
        self.newPwd2.addAction(self.newPwd2Action, QLineEdit.ActionPosition.TrailingPosition)

        # 绑定槽
        self.validatePasswordLineEditAction.triggered.connect(self.toggle_echo_mode_1)
        self.newPwd1Action.triggered.connect(self.toggle_echo_mode_2)
        self.newPwd2Action.triggered.connect(self.toggle_echo_mode_3)

    def bind(self):
        self.nextPushButton.clicked.connect(self.check_user)
        self.accountLineEdit.textChanged.connect(self.none_limit)
        self.validatePushButton.clicked.connect(self.check_account)
        self.newPwd2.textChanged.connect(self.compare_pwd)
        self.updatePushButton.clicked.connect(self.update_password)

    def none_limit(self, text):
        """输入的账号为空则禁止下一步"""
        if text is None or text == "":
            self.nextPushButton.setEnabled(False)
        else:
            self.nextPushButton.setEnabled(True)

    def check_user(self):
        """
        校验账号是否合法，是否存在
        """
        account = self.accountLineEdit.text()

        if re.match(r"^\d{11}$", account):
            user = self.user_dao.get_user_by_phone(account)
        elif re.match(r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", account):
            user = self.user_dao.get_user_by_email(account)
        else:
            QMessageBox.warning(self, '警告', '该账号不存在！',
                                QMessageBox.StandardButton.Ok)
            self.accountLineEdit.setText("")
            self.accountLineEdit.setFocus()
            return

        if user is None:
            QMessageBox.warning(self, '警告', '该账号不存在！',
                                QMessageBox.StandardButton.Ok)
            self.accountLineEdit.setText("")
            self.accountLineEdit.setFocus()
        else:
            self.cur_user = user
            if len(self.pwd_dao.all(user_id=user.id)) == 0:
                self.stackedWidget.setCurrentIndex(2)
            else:
                self.stackedWidget.setCurrentIndex(1)

    def check_account(self):
        account = self.validateAccountLineEdit.text()
        password = self.validatePasswordLineEdit.text()

        items = self.pwd_dao.get_item_by_user_id_and_account(self.cur_user.id, account)

        for item in items:
            if decrypt(item.password) == password:
                self.stackedWidget.setCurrentIndex(2)
                return
        else:
            QMessageBox.warning(self, '警告', '您输入的账号密码有误，请重新输入！',
                                QMessageBox.StandardButton.Ok)
            self.validateAccountLineEdit.setText("")
            self.validatePasswordLineEdit.setText("")
            self.validateAccountLineEdit.setFocus()

    def compare_pwd(self, text):
        """比较两次密码是否输入一致"""
        if not self.newPwd1.text().startswith(text):
            self.newPwd2.setStyleSheet("color: red")
            QMessageBox.warning(self, '警告', '两次密码不一致！',
                                QMessageBox.StandardButton.Ok)
            self.newPwd2.setText("")
        else:
            self.newPwd2.setStyleSheet("color: black")

    def update_password(self):
        new_password_1 = self.newPwd1.text()
        new_password_2 = self.newPwd2.text()

        if new_password_1 is None or new_password_1 == "":
            QMessageBox.warning(self, '警告', '请输入密码！',
                                QMessageBox.StandardButton.Ok)
            self.newPwd1.setFocus()
        elif new_password_2 is None or new_password_2 == "":
            QMessageBox.warning(self, '警告', '请输入密码！',
                                QMessageBox.StandardButton.Ok)
            self.newPwd2.setFocus()
        elif new_password_2 != new_password_2:
            QMessageBox.warning(self, '警告', '两次密码不一致！',
                                QMessageBox.StandardButton.Ok)
            self.newPwd2.setText("")
            self.newPwd2.setFocus()
        else:
            md5 = hashlib.md5()
            md5.update(new_password_2.encode("utf-8"))
            self.user_dao.update_password(self.cur_user.id, new_password=md5.hexdigest(), success_func=self.complete, except_func=self.update_pwd_failed)

    def complete(self):
        self.close()
        self.closed.emit()

    def update_pwd_failed(self):
        """更新密码失败，清空所有信息"""
        QMessageBox.critical(self, '警告', '更新密码失败，请重新尝试修改密码！',
                             QMessageBox.StandardButton.Ok)
        self.close()

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key.Key_Enter or key_event.key() == Qt.Key.Key_Return:
            match self.stackedWidget.currentIndex():
                case 0:
                    self.nextPushButton.click()
                case 1:
                    self.validatePushButton.click()
                case 2:
                    self.updatePushButton.click()
        elif key_event.key() == Qt.Key.Key_Escape:
            self.close()

    def toggle_echo_mode_1(self):
        if self.validatePasswordLineEdit.echoMode() == QLineEdit.EchoMode.Password:
            self.validatePasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.validatePasswordLineEditAction.setIcon(QIcon(":/icons/icons/eye-open.png"))
        else:
            self.validatePasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
            self.validatePasswordLineEditAction.setIcon(QIcon(":/icons/icons/eye-close.png"))

    def toggle_echo_mode_2(self):
        if self.newPwd1.echoMode() == QLineEdit.EchoMode.Password:
            self.newPwd1.setEchoMode(QLineEdit.EchoMode.Normal)
            self.newPwd1Action.setIcon(QIcon(":/icons/icons/eye-open.png"))
        else:
            self.newPwd1.setEchoMode(QLineEdit.EchoMode.Password)
            self.newPwd1Action.setIcon(QIcon(":/icons/icons/eye-close.png"))

    def toggle_echo_mode_3(self):
        if self.newPwd2.echoMode() == QLineEdit.EchoMode.Password:
            self.newPwd2.setEchoMode(QLineEdit.EchoMode.Normal)
            self.newPwd2Action.setIcon(QIcon(":/icons/icons/eye-open.png"))
        else:
            self.validatePasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
            self.newPwd2Action.setIcon(QIcon(":/icons/icons/eye-close.png"))
