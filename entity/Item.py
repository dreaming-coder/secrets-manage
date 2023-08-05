from datetime import datetime
from typing import Optional, Union


# noinspection PyShadowingBuiltins
class Item:
    def __init__(self, id: Optional[int], user_id: Optional[int], title: Optional[str],
                 account: Optional[str] = None, password: Optional[str] = None, notes: Optional[str] = None,
                 create_time: Union[datetime, str, None] = None, update_time: Union[datetime, str, None] = None):
        self.id: Optional[int] = id  # id
        self.user_id: Optional[int] = user_id  # 用户id
        self.title: Optional[str] = title  # 账号名
        self.account: Optional[str] = account  # 账号
        self.password: Optional[str] = password  # 密码
        self.notes: Optional[str] = notes  # 备注

        # 创建时间
        if isinstance(create_time, str):
            self.create_time: Union[datetime, str, None] = datetime.strptime(create_time, "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.create_time: Union[datetime, str, None] = create_time

            # 更新时间
        if isinstance(update_time, str):
            self.update_time: Union[datetime, str, None] = datetime.strptime(update_time, "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.update_time: Union[datetime, str, None] = update_time

    def __repr__(self):
        return f"""
Item(
    id = {self.id}
    user_id = {self.user_id},
    title = {self.title}
    account = {self.account},
    password = {self.password},
    notes = {self.notes},
    create_time = {self.create_time}，
    update_time = {self.update_time}
)"""
