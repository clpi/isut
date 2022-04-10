import sys, os
from PySide6.QtCore import *
from isu.view.window import Win
from typing import List, Type
from isu.view import UiLoader
from PySide6.QtWidgets import *

def app() -> QCoreApplication:
    match QApplication.instance():
        case None: return QApplication(sys.argv)
        case ins: return ins

class Isu(QObject):

    @staticmethod
    def instance() -> QCoreApplication:
        return app()

    app: QCoreApplication
    win: QMainWindow

    def __init__(self) -> None:
        self.app = app()
        self.win = Win()

    def run(self):
        self.win.show()
        sys.exit(self.app.exec())

    def show(self):
        self.app = self.instance()
        self.win = Win(None)
        self.win.show()
        sys.exit(self.app.exec())

