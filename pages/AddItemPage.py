from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QMouseEvent, QAction, QIcon
from PySide6.QtWidgets import QWidget, QToolButton, QLineEdit, QMessageBox

from dao import ItemDao
from entity import Item
from utils import encrypt, Loader
from .ui import Ui_addItemPage


# noinspection PyBroadException,PyAttributeOutsideInit,DuplicatedCode,PyArgumentList
class AddItemPage(QWidget, Ui_addItemPage):
    created = Signal()

    def __init__(self, parent=None, cur_user=None):
        super().__init__(parent)

        self.cur_user = cur_user
        self.origin_pos = None
        self.pwd_dao = ItemDao()

        self.setupUi(self)

        # 移除标题栏
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # 表示窗体具有透明效果，否则窗体做圆角会发现还存在黑色的角
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # 修改搜索文本框中的清除按钮样式需要先设定 objectName，避免全局修改
        self.nameLineEdit.findChild(QToolButton).setObjectName("clearButton1")
        self.accountLineEdit.findChild(QToolButton).setObjectName("clearButton2")
        self.describeLineEdit.findChild(QToolButton).setObjectName("clearButton3")

        self.setStyleSheet(Loader.loadQSS(":/styles/styles/AddItemPage.qss"))

        self.set_toggle_echo_mode()

        self.bind()

    def bind(self):
        self.addPushButton.clicked.connect(self.add_item)

    def set_toggle_echo_mode(self):
        # 设置密码框明密文切换
        self.action = QAction(self.passwordLineEdit)
        self.action.setIcon(QIcon(":/icons/icons/eye-close.png"))
        self.passwordLineEdit.addAction(self.action, QLineEdit.ActionPosition.TrailingPosition)

        self.action.triggered.connect(self.toggle_echo_mode)

    def toggle_echo_mode(self):
        if self.passwordLineEdit.echoMode() == QLineEdit.EchoMode.Password:
            self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.action.setIcon(QIcon(":/icons/icons/eye-open.png"))
        else:
            self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
            self.action.setIcon(QIcon(":/icons/icons/eye-close.png"))

    # ========================= 自定义 窗口移动 事件 start ====================================

    def mousePressEvent(self, event: QMouseEvent):
        """获取鼠标单击的位置"""
        if event.buttons() == Qt.LeftButton:
            try:
                self.origin_pos = event.pos()
            except Exception:
                pass

    def mouseMoveEvent(self, event: QMouseEvent):
        """自定义拖拽移动"""
        if self.addPushButton.underMouse() or self.clearPushButton.underMouse():
            pass
        elif self.nameLineEdit.underMouse() or self.accountLineEdit.underMouse() or self.passwordLineEdit.underMouse() or self.describeLineEdit.underMouse():
            pass
        else:
            try:
                if event.buttons() == Qt.LeftButton and self.origin_pos:
                    self.move(self.mapToGlobal(event.pos() - self.origin_pos))
                event.accept()
            except Exception:
                pass

    # ========================= 自定义 窗口移动 事件 end =====================================

    def add_item(self):
        title = self.nameLineEdit.text()
        account = self.accountLineEdit.text()
        password = self.passwordLineEdit.text()
        notes = self.describeLineEdit.text()

        if title is None or title == "":
            QMessageBox.warning(self, '警告', '请输入账号名称！',
                                QMessageBox.StandardButton.Ok)
            self.nameLineEdit.setFocus()
        elif account is None or account == "":
            QMessageBox.warning(self, '警告', '请输入账号！',
                                QMessageBox.StandardButton.Ok)
            self.accountLineEdit.setFocus()
        elif password is None or password == "":
            QMessageBox.warning(self, '警告', '请输入密码！',
                                QMessageBox.StandardButton.Ok)
            self.passwordLineEdit.setFocus()
        else:

            item = Item(id=None, user_id=self.cur_user.id, title=title, account=account, password=encrypt(password), notes=notes)
            self.pwd_dao.add_item(item, success_func=self.success_func)

        self.created.emit()

    def success_func(self):
        self.clear_line_edit_contents()
        QMessageBox.about(self, '', '创建成功！')

    def clear_line_edit_contents(self):
        self.nameLineEdit.clear()
        self.accountLineEdit.clear()
        self.passwordLineEdit.clear()
        self.describeLineEdit.clear()
        self.nameLineEdit.setFocus()

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key.Key_Enter or key_event.key() == Qt.Key.Key_Return:
            self.addPushButton.click()
        elif key_event.key() == Qt.Key.Key_Escape:
            self.close()
