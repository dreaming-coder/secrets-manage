from datetime import datetime
from typing import Optional, Callable

from entity import User
from .BaseDao import BaseDao

__all__ = ["UserDao"]


# noinspection PyBroadException
class UserDao(BaseDao):

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        cursor = self.connection.cursor()
        cursor.execute("select * from user where id = ?", [user_id])
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return None
        return User(*result)

    def get_user_by_phone(self, phone: str) -> Optional[User]:
        cursor = self.connection.cursor()
        cursor.execute("select * from user where phone = ?", [phone])
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return None
        return User(*result)

    def get_user_by_email(self, email: str) -> Optional[User]:
        cursor = self.connection.cursor()
        cursor.execute("select * from user where email = ?", [email])
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return None
        return User(*result)

    def add_user(self, user: User, success_func: Optional[Callable] = None, except_func: Optional[Callable] = None) -> None:
        cursor = self.connection.cursor()
        try:
            cursor.execute("insert into user(phone, email, name, password, create_time) values(?, ?, ?, ?, ?)",
                           (user.phone, user.email, user.name, user.password, datetime.now()))
            self.connection.commit()
            if success_func is not None:
                success_func()
        except Exception:
            self.connection.rollback()
            if except_func is not None:
                except_func()
        finally:
            cursor.close()

    def update_password(self, user_id: int, new_password: str, success_func: Optional[Callable] = None, except_func: Optional[Callable] = None) -> None:
        cursor = self.connection.cursor()
        try:
            cursor.execute("update user set password = ? where id = ?", (new_password, user_id))
            self.connection.commit()
            if success_func is not None:
                success_func()
        except Exception:
            self.connection.rollback()
            if except_func is not None:
                except_func()
        finally:
            cursor.close()
