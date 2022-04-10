from isu.utils import show, browseFile
from typing import List, Any
from isu.view import UiLoader
from isu.actions.op import Op
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from isu.ui.tab import Ui_opsWidget

class NoOp(QWidget, Ui_no):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)


class OpTabs(QTabWidget):

    def __init__(self, parent = None):
        QTabWidget.__init__(self, parent)
        super(OpTabs, self).__init__(parent)
        self.tabs: List[QWidget] = []

    @Slot()
    def onNoTabs(self):
        self.destroy()

    @Slot()
    def onTaskAdd(self):
        self.tabs.append(QWidget(None))


class OpTab(QWidget, Ui_opsWidget):
    def __init__(self, idx: int = -1, parent = None):
        QWidget.__init__(self)
        self.setupUi(self)
        self.allDemoCheck: QCheckBox
        self.allStepsCheck: QCheckBox
        self.op

    def op(self) -> Op:
        return Op(self.opidx)


show(__name__, OpTab)
