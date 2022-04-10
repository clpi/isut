import sys
from PySide6.QtCore import *
import isu.utils as utils
from isu.view import UiLoader
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PyQt6.uic import load_ui
from isu.view.dialog import About, Preferences, Progress
from isu.ui.window import Ui_MainWindow
from isu.ui.prefs import Ui_prefsDialog
from isu.ui.prog import Ui_progDialog

# class Win(QMainWindow, Ui_MainWindow):
class Win(QMainWindow):
    def __init__(self, parent = None):
        super(Win, self).__init__()
        self.loadUi()
        self.loadWin()
        self.loadSteps()
        self.loadStatus()
        self.loadConnections()
        self.loadViews()

    def loadUi(self):
        UiLoader().loadUi(r"isu\ui\window.ui", self)

    def loadWin(self):
        self.setAcceptDrops(True)
        self.setUpdatesEnabled(True)
        self.setWindowIcon(QIcon(':/qt-project.org/logos/pysidelogo.png'))

    def loadViews(self):
        pass

    def loadStatus(self):
        self.statusBar().showMessage("Ready", 2000)

    def loadSteps(self):
        pass

    def loadConnections(self):
        pass

    @Slot()
    def browseDemo(self) -> QFile | None:
        self.statusBar().showMessage("Browsing for demo file...", 2000)
        if file := utils.browseFile(self, "Open demo", QDir.currentPath(), "Demo files (*.demo)"):
            return QFile(file)
        return None


    def showPrefs(self):
        pref

    @Slot()
    def show_about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

utils.showUi(__name__, Ui)

    # a = QApplication()
    # w=Win()
    # w.show()
    # a.exec()