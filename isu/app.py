import sys, os
from PySide6.QtCore import *
from isu.view.window import Win
from typing import List, Type
from isu.view import UiLoader
from PySide6.QtWidgets import *
from isu.utils import app

class Isu(QObject):

    @staticmethod
    def instance() -> QCoreApplication:
        return app()

    app: QApplication
    win: QMainWindow

    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.win = Win()

    def setStyle(self, sheet: str = "isu/ui/style.qss"):
        with open(sheet, "r") as f:
            style = f.read()
            self.app.setStyle(style)

    def run(self):
        self.win.show()
        sys.exit(self.app.exec())

    def show(self):
        app = self.instance()
        self.win = Win(None)
        self.win.show()
        sys.exit(self.app.exec())

