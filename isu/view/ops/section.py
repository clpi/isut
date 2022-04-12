import os, sys
from isu import utils
from pathlib import WindowsPath, Path
from typing import Optional, Any, Type
from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from isu.ui.section import Ui_sectionOp

class SectionJob(QRunnable):

    def __init__(self) -> None:
        super(SectionJob, self).__init__()

    def run(self: QRunnable) -> None:
        return super().run()

class SectionOp(QWidget, Ui_sectionOp):

    def __init__(self, parent = None) -> None:
        super(SectionOp, self).__init__(parent)
        self.setupUi(self)
        self.title: str = "Section"
        self.loadWidgets()
        self.loadConnections()

    @staticmethod
    def job() -> Type[QRunnable]:
        return SectionJob

    def run(self) -> QRunnable:
        return SectionJob(
        )

    def loadWidgets(self):
        pass

    def loadConnections(self):
        pass

utils.show(__name__, SectionOp)