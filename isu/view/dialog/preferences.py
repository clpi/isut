from PySide6.QtWidgets import *
from isu.utils import show
from isu.ui.prefs import Ui_prefsDialog

class Preferences(QDialog, Ui_prefsDialog):
    def __init__(self, parent = None) -> None:
        QDialog.__init__(self)
        self.setupUi(self)
        # super(Preferences, self).__init__(parent)

show(__name__, Preferences)