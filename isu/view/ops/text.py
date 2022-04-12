import os, sys
from isu import utils
from pathlib import WindowsPath, Path
from typing import Optional, Any, Type
from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from isu.ui.text import Ui_textOp

class TextJob(QRunnable):

    def __init__(self) -> None:
        super(TextJob, self).__init__()

    def run(self: QRunnable) -> None:
        return super().run()

class TextOp(QTabWidget, Ui_textOp):

    def __init__(self, parent = None) -> None:
        super(TextOp, self).__init__(parent)
        self.setupUi(self)
        self.title: str = "Text"
        self.loadWidgets()
        self.loadConnections()

    @staticmethod
    def job() -> Type[QRunnable]:
        return TextJob

    def run(self) -> QRunnable:
        return TextJob(
        )

    def loadWidgets(self):
        pass

    def loadConnections(self):
        pass

utils.show(__name__, TextOp)