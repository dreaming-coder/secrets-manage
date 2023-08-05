from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication

# noinspection PyUnresolvedReferences
import resources.resources_rc
from pages import LoginPage


def init():
    """
    初始化程序
    """
    ...


if __name__ == '__main__':
    init()
    app = QApplication()
    app.setWindowIcon(QPixmap(":/icons/icons/favicon.ico"))

    win = LoginPage()
    win.show()
    app.exec()
