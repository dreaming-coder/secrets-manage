from PySide6.QtCore import QSettings
from cryptography.fernet import Fernet

__all__ = [
    "datasource",
    "key"
]

settings = QSettings("conf/config.ini", QSettings.Format.IniFormat)

datasource = settings.value("database/datasource")

key = settings.value("crypto/key")

if key is None or key == "":
    key = Fernet.generate_key().decode(encoding="utf-8")
    settings.setValue("crypto/key", key)




