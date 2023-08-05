from datetime import datetime
from typing import Optional, Union


# noinspection PyShadowingBuiltins
class User:

    def __init__(self, id: Optional[int] = None, phone: Optional[str] = None, email: Optional[str] = None,
                 name: Optional[str] = None, password: Optional[str] = None,
                 create_time: Union[datetime, str, None] = None, last_login_time: Union[datetime, str, None] = None):
        self.id: Optional[int] = id  # id
        self.phone: Optional[str] = phone  # 手机号
        self.email: Optional[str] = email  # 电子邮箱
        self.name: Optional[str] = name  # 昵称
        self.password: Optional[str] = password  # 密码

        # 创建时间
        if isinstance(create_time, str):
            self.create_time = datetime.strptime(create_time, "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.create_time = create_time

        # 最后登录时间
        if isinstance(last_login_time, str):
            self.last_login_time = datetime.strptime(last_login_time, "%Y-%m-%d %H:%M:%S.%f")
        else:
            self.last_login_time = last_login_time

    def __repr__(self):
        return f"""
User(
    id = {self.id},
    name = {self.name}
    phone = {self.phone},
    email = {self.email},
    password = {self.password},
    create_time = {self.create_time},
    last_login_time = {self.last_login_time}
)"""
