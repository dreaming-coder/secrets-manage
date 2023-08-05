from cryptography.fernet import Fernet

from .settings import key

__all__ = ["encrypt", "decrypt"]

f = Fernet(key.encode())


def encrypt(data: str) -> str:
    """加密"""
    return f.encrypt(data.encode(encoding="utf-8")).decode(encoding="utf-8")


def decrypt(data: str) -> str:
    """解密"""
    return f.decrypt(data.encode(encoding="utf-8")).decode(encoding="utf-8")
