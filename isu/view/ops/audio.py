import os, sys
from pathlib import WindowsPath, Path
from isu.utils import show
from typing import Optional, Any, Type
from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from isu.ui.audio import Ui_audioOp

class AudioJob(QRunnable):

    def __init__(self):
        super(AudioJob, self).__init__()

    def run(self: QRunnable) -> None:
        return super().run()

class AudioOp(QWidget, Ui_audioOp):

    def __init__(self, parent: QWidget | None) -> None:
        super(AudioOp, self).__init__(parent)
        self.setupUi(self)
        self.title: str = "Attach Audio"

    @staticmethod
    def job() -> Type[QRunnable]:
        return AudioJob

    def run(self) -> QRunnable:
        a = AudioJob()
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

show(__name__, AudioOp)