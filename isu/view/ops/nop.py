from PySide6.QtCore import *
from isu import utils
from PySide6.QtWidgets import *
from isu.view import UiLoader
from isu.ui.noop import Ui_noOp
from isu.models.demo.load import DemoLoad

class Nop(QGroupBox, Ui_noOp):

    loadedDemo = Signal(DemoLoad)

    def __init__(self, parent = None):
        super(Nop, self).__init__()
        self.setupUi(self)
        self.loadWidgets()

    def loadWidgets(self):
        self.taskCombo: QComboBox
        self.loadDemoBtn: QPushButton

utils.show(__name__, Nop)