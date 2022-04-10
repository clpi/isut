from isu.ui.prog import Ui_progDialog
from isu.utils import show, showUi
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Progress(QDialog, Ui_progDialog):
    def __init__(self, parent=None):
        super().__init__(parent)


show(__name__, Progress)