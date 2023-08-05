from PySide6.QtCore import QFile, QIODevice


# noinspection PyPep8Naming
class Loader:
    @staticmethod
    def loadQSS(file: str):
        fp = QFile(file)
        if fp.open(QIODevice.OpenModeFlag.ReadOnly):
            return str(fp.readAll(), encoding="utf-8")

    @staticmethod
    def loadSQL(file: str):
        fp = QFile(file)
        if fp.open(QIODevice.OpenModeFlag.ReadOnly):
            return str(fp.readAll(), encoding="utf-8")
