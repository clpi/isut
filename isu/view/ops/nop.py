from PySide6.QtCore import *
from isu import utils
from PySide6.QtWidgets import *
from isu.view import UiLoader
from isu.ui.noop import Ui_noOp

class Nop(QGroupBox, Ui_noOp):
    def __init__(self, parent = None):
        super(Nop, self).__init__()
        # UiLoader().loadUi("isu/ui/ops/noop.ui", self)
        self.setupUi(self)

utils.show(__name__, Nop)