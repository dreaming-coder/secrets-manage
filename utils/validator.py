from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

__all__ = [
    "PhoneValidator",
    "EmailValidator",
    "AccountValidator",
    "PasswordValidator"
]


class PhoneValidator(QRegularExpressionValidator):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.reg = QRegularExpression(r'^\d{11}$')
        self.setRegularExpression(self.reg)


class EmailValidator(QRegularExpressionValidator):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.reg = QRegularExpression(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
        self.setRegularExpression(self.reg)


class AccountValidator(QRegularExpressionValidator):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.reg = QRegularExpression(r'^\d{11}|\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
        self.setRegularExpression(self.reg)


class PasswordValidator(QRegularExpressionValidator):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.reg = QRegularExpression(r'^[a-zA-Z][\w!@#$%^&*_]{5,17}$')
        self.setRegularExpression(self.reg)
