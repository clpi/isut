from PySide6.QtWidgets import *
from isu.view.task import TaskTab
from PySide6.QtCore import *

class TaskTable(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.setColumnCount(4)

class TaskTableItem(QAbstractItemModel):
    def __init__(self, task_idx: int = 0, parent=None):
        QAbstractItemModel.__init__(self, parent)
        # self.setData(value=task_idx)
