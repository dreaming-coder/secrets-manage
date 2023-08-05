from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtWidgets import QMainWindow, QToolButton, QHeaderView, QTableWidgetItem, QPushButton, QTableWidget, QHBoxLayout, QWidget, QMessageBox, QInputDialog, QLineEdit

from dao import ItemDao
from utils import decrypt, encrypt, Loader
from .AddItemPage import AddItemPage
from .ui import Ui_mainPage


# noinspection DuplicatedCode
class MainPage(QMainWindow, Ui_mainPage):

    def __init__(self, parent=None, cur_user=None):
        super().__init__(parent)

        self.cur_user = cur_user
        self.password_dao = ItemDao()
        self.add_item_page = None
        self.data = set()

        self.to_delete_ids = set()

        self.setupUi(self)
        self.setStyleSheet(Loader.loadQSS(":/styles/styles/MainPage.qss"))

        self.setWindowTitle(f"密码管理器 | 欢迎，{cur_user.name}！")

        # 设置窗体按钮样式
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)

        # 修改搜索文本框中的清除按钮样式需要先设定 objectName，避免全局修改
        self.contidionLineEdit.findChild(QToolButton).setObjectName("clearButton")

        self.deletePushButton.setEnabled(False)  # 初始未选择项，不允许操作

        self.refresh()

        self.bind()

    def refresh(self):
        self.data = set(self.password_dao.all(self.cur_user.id))
        self.conditionCombox.setCurrentIndex(0)
        self.contidionLineEdit.clear()
        self.refresh_table()

    def refresh_table(self):

        # 要先设置表格有几行几列，否则数据不显示
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnCount(8)

        # 设置表头
        self.tableWidget.setHorizontalHeaderLabels(["", "id", "名称", "账号", "密码", "备注", "创建时间", "操作"])

        for rowIndex, row in enumerate(self.data):

            # 第一列空出来，做复选框用
            self.tableWidget.setItem(rowIndex, 0, QTableWidgetItem())
            self.tableWidget.item(rowIndex, 0).setCheckState(Qt.CheckState.Unchecked)

            # 解决表格存放数字
            id_cell = QTableWidgetItem()
            id_cell.setData(Qt.ItemDataRole.DisplayRole, row.id)
            self.tableWidget.setItem(rowIndex, 1, QTableWidgetItem(id_cell))

            self.tableWidget.setItem(rowIndex, 2, QTableWidgetItem(row.title))
            self.tableWidget.setItem(rowIndex, 3, QTableWidgetItem(row.account))
            self.tableWidget.setItem(rowIndex, 4, QTableWidgetItem(row.password))
            self.tableWidget.setItem(rowIndex, 5, QTableWidgetItem(row.notes))
            self.tableWidget.setItem(rowIndex, 6, QTableWidgetItem(datetime.strftime(row.create_time, "%Y-%m-%d")))

            # 设置对齐方式
            for columnIndex in range(0, 7):
                self.tableWidget.item(rowIndex, columnIndex).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            # ================================= 每一行的操作按钮 =====================================

            widget = QWidget()
            layout = QHBoxLayout(widget)

            btn_1 = QPushButton()
            btn_1.setIcon(QIcon(":/icons/icons/lookup-button.png"))
            btn_1.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_1.setToolTip("查看")

            btn_2 = QPushButton()
            btn_2.setIcon(QIcon(":/icons/icons/modify-button.png"))
            btn_2.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_2.setToolTip("修改")

            btn_3 = QPushButton()
            btn_3.setIcon(QIcon(":/icons/icons/delete-button.png"))
            btn_3.setCursor(Qt.CursorShape.PointingHandCursor)
            btn_3.setToolTip("删除")

            layout.addWidget(btn_1)
            layout.addWidget(btn_2)
            layout.addWidget(btn_3)

            self.tableWidget.setCellWidget(rowIndex, 7, widget)

            def handle_bind(item):
                def display():
                    p = decrypt(item.password)
                    QMessageBox.information(self, '密码提示', f'您的密码是：{p}',
                                            QMessageBox.StandardButton.Ok,
                                            QMessageBox.StandardButton.Ok)

                def modify():
                    reply, ok = QInputDialog.getText(self, "修改密码", "请输入新的密码：", QLineEdit.EchoMode.Password)

                    if ok:
                        new_pwd_1 = reply
                        reply, ok = QInputDialog.getText(self, "修改密码", "请再次输入密码：", QLineEdit.EchoMode.Password)
                        if ok:
                            new_pwd_2 = reply
                            if new_pwd_1 == new_pwd_2:
                                new_pwd = encrypt(new_pwd_2)
                                self.password_dao.update_password(item_id=item.id, new_password=new_pwd,
                                                                  success_func=lambda: QMessageBox.about(self, "修改密码", "您的密码已修改成功"))
                                self.resetPushButton.click()
                            else:
                                QMessageBox.about(self, "修改密码", "两次密码不一致，请重新操作！")

                def delete_item():
                    self.data.discard(item)
                    self.password_dao.delete_item(item)
                    self.refresh()

                return display, modify, delete_item

            func1, func2, func3 = handle_bind(row)
            btn_1.clicked.connect(func1)
            btn_2.clicked.connect(func2)
            btn_3.clicked.connect(func3)

        # ======================================== 表格样式设置 =============================================

        self.tableWidget.hideColumn(4)  # 隐藏列
        self.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # 禁止编辑
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏行号

        # 设置选择一行
        # self.tableWidget.setSelectionMode(QTableWidget.SelectionMode.ContiguousSelection)  # 单选还是多选
        # self.tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)  # 选的是行还是项目

        self.tableWidget.horizontalHeader().setHighlightSections(False)  # 表头不会高亮变色

        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)  # 行高自适应

        # 先设置所有列自适应宽度，再单独设置列的宽度
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Custom)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Custom)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Custom)
        self.tableWidget.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeMode.Custom)

        self.tableWidget.setColumnWidth(0, 20)
        self.tableWidget.setColumnWidth(1, 40)
        self.tableWidget.setColumnWidth(6, 80)
        self.tableWidget.setColumnWidth(7, 80)

        # 指定按某列排序
        self.tableWidget.sortByColumn(1, Qt.SortOrder.AscendingOrder)

    def bind(self):
        self.addPushButton.clicked.connect(self.show_add_item_page)
        self.deletePushButton.clicked.connect(self.delete_items)
        self.tableWidget.cellChanged.connect(self.check_state)
        self.searchPushButton.clicked.connect(self.filter_items)
        self.resetPushButton.clicked.connect(self.refresh)

    def check_state(self, row, column):
        cell = self.tableWidget.item(row, column)
        item = self.tableWidget.item(row, 1)

        if item is not None:
            item_id = item.text()
            if cell.checkState() == Qt.CheckState.Checked:
                self.to_delete_ids.add(item_id)
            else:
                self.to_delete_ids.discard(item_id)

        # 控制按钮是否可用
        if len(self.to_delete_ids) > 0:
            self.deletePushButton.setEnabled(True)
        else:
            self.deletePushButton.setEnabled(False)

    def delete_items(self):
        for item in self.to_delete_ids:
            self.data.discard(item)
        self.password_dao.delete_items_by_ids(self.to_delete_ids)
        self.to_delete_ids.clear()
        self.refresh()

    def show_add_item_page(self):
        self.add_item_page = AddItemPage(cur_user=self.cur_user)

        # 创建过完刷新表格显示
        self.add_item_page.created.connect(self.refresh)

        self.add_item_page.show()

    def closeEvent(self, event: QCloseEvent):
        """自定义级联关闭窗口,重载 close() 方法没用"""
        if self.add_item_page is not None:
            self.add_item_page.close()
        super().closeEvent(event)

    def filter_items(self):
        index = self.conditionCombox.currentIndex()
        value = self.contidionLineEdit.text()
        match index:
            case 0:
                self.data = set(self.password_dao.filter_by_all(self.cur_user.id, value))
            case 1:
                self.data = set(self.password_dao.filter_by_title(self.cur_user.id, value))
            case 2:
                self.data = set(self.password_dao.filter_by_account(self.cur_user.id, value))
            case 3:
                self.data = set(self.password_dao.filter_by_notes(self.cur_user.id, value))

        self.refresh_table()

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key.Key_Enter or key_event.key() == Qt.Key.Key_Return:
            if self.contidionLineEdit.hasFocus():
                self.searchPushButton.click()
