import os, sys
from pathlib import WindowsPath, Path
from isu.utils import show
from typing import Optional, Any, Type
from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from isu.ui.pace import Ui_paceOp

class PaceJob(QRunnable):

    def __init__(self):
        super(PaceJob, self).__init__()

    def run(self: QRunnable) -> None:
        return super().run()

class PaceOp(QWidget, Ui_paceOp):

    def __init__(self, parent: QWidget | None) -> None:
        super(PaceOp, self).__init__(parent)
        self.setupUi(self)
        self.title: str = "Attach Pace"

    @staticmethod
    def job() -> Type[QRunnable]:
        return PaceJob

    def run(self) -> QRunnable:
        a = PaceJob()
        return a

    def load_ui(self):
        pass

    def load_widgets(self):
        # self.opsParamsStack.addWidget(self)

        # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
        pass

    @staticmethod
    def cbidx() -> int:
        return 3

show(__name__, PaceOp)