from entity import Item
from .BaseDao import BaseDao
from typing import Optional, Callable
from datetime import datetime

__all__ = ["ItemDao"]


# noinspection PyBroadException,PyUnresolvedReferences
class ItemDao(BaseDao):

    def all(self, user_id: int) -> list[Item]:
        cursor = self.connection.cursor()
        cursor.execute("select * from item where user_id = ?", [user_id])
        results = cursor.fetchall()
        cursor.close()
        return [Item(*r) for r in results]

    def get_item_by_user_id_and_account(self, user_id: int, account: str) -> list[Item]:
        cursor = self.connection.cursor()
        cursor.execute("select * from item where user_id = ? and account = ?", [user_id, account])
        results = cursor.fetchall()
        cursor.close()
        return [Item(*r) for r in results]

    def add_item(self, item: Item, success_func: Optional[Callable] = None, except_func: Optional[Callable] = None) -> None:
        cursor = self.connection.cursor()
        try:
            now = datetime.now()
            cursor.execute("insert into item(user_id, title, account, password, notes, create_time, update_time) values(?, ?, ?, ?, ?,?, ?)",
                           (item.user_id, item.title, item.account, item.password, item.notes, now, now))
            self.connection.commit()
            if success_func is not None:
                success_func()
        except Exception:
            self.connection.rollback()
            if except_func is not None:
                except_func()
        finally:
            cursor.close()

    def update_password(self, item_id: int, new_password: str, success_func: Optional[Callable] = None, except_func: Optional[Callable] = None) -> None:
        cursor = self.connection.cursor()
        try:
            cursor.execute("update item set password = ? where id = ?", (new_password, item_id))
            self.connection.commit()
            if success_func is not None:
                success_func()
        except Exception:
            self.connection.rollback()
            if except_func is not None:
                except_func()
        finally:
            cursor.close()

    def delete_items_by_ids(self, ids: set[int]):

        cursor = self.connection.cursor()
        cursor.executemany("delete from item where id = ?", [(int(n),) for n in ids])
        self.connection.commit()
        cursor.close()

    def delete_item(self, item: Item):
        cursor = self.connection.cursor()
        cursor.execute("delete from item where id = ?", [item.id])
        self.connection.commit()
        cursor.close()

    def filter_by_all(self, user_id: int, text: str):
        text = f"%{text}%"
        cursor = self.connection.cursor()
        cursor.execute("select * from item where user_id = ? and (title like ? or account like ? or notes like ?)",
                       (user_id, text, text, text))
        results = cursor.fetchall()
        cursor.close()
        return [Item(*r) for r in results]

    def filter_by_title(self, user_id: int, text: str):
        text = f"%{text}%"
        cursor = self.connection.cursor()
        cursor.execute("select * from item where user_id = ? and title like ?",
                       (user_id, text))
        results = cursor.fetchall()
        cursor.close()
        return [Item(*r) for r in results]

    def filter_by_account(self, user_id, text):
        text = f"%{text}%"
        cursor = self.connection.cursor()
        cursor.execute("select * from item where user_id = ? and item.account like ?",
                       (user_id, text))
        results = cursor.fetchall()
        cursor.close()
        return [Item(*r) for r in results]

    def filter_by_notes(self, user_id, text):
        text = f"%{text}%"
        cursor = self.connection.cursor()
        cursor.execute("select * from item where user_id = ? and notes like ?",
                       (user_id, text))
        results = cursor.fetchall()
        cursor.close()
        return [Item(*r) for r in results]
