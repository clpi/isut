import os, sys
from isu.utils import show
from pathlib import WindowsPath, Path
from typing import Optional, Any, Type
from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from isu.ui.crop import Ui_cropOp

class CropJob(QRunnable):

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        super(CropJob, self).__init__()

    def run(self: QRunnable) -> None:
        return super().run()

class CropOp(QWidget, Ui_cropOp):

    def __init__(self, parent: QWidget | None) -> None:
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.title: str = "Crop Demo"
        self.loadWidgets()

    @staticmethod
    def job() -> Type[QRunnable]:
        return CropJob

    def run(self) -> QRunnable:
        return CropJob(
            x=self.cropSpinX.value(),
            y=self.cropSpinY.value(),
            w=self.cropSpinW.value(),
            h=self.cropSpinH.value()
        )

    def loadWidgets(self):
        self.cropSpinX: QSpinBox
        self.cropSpinY: QSpinBox
        self.cropSpinW: QSpinBox
        self.cropSpinH: QSpinBox


show(__name__, CropOp)