from PySide6.QtWidgets import *
from isu import utils
from isu.ui.tab import Ui_opsWidget

class TaskTab(QWidget, Ui_opsWidget):
    def __init__(self, idx: int = -1, parent = None):
        QWidget.__init__(self)
        self.setupUi(self)
        self.allDemoCheck: QCheckBox
        self.allStepsCheck: QCheckBox

utils.show(__name__, TaskTab)