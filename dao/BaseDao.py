import sqlite3

from utils import datasource, Loader


class BaseDao:
    _connection = None

    def __init__(self):
        # 创建Sqlite连接引擎
        if self._connection is None:
            self.__connection = self._connection = sqlite3.connect(database=datasource)
            cursor = self.__connection.cursor()
            try:
                cursor.execute(Loader.loadSQL(":/sql/sql/user.sql"))
                cursor.execute(Loader.loadSQL(":/sql/sql/item.sql"))
                self.__connection.commit()
            except Exception as e:
                print(e)
        else:
            self.__connection = self._connection

    @property
    def connection(self):
        return self.__connection
