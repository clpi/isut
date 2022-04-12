import os, sys
from isu.utils import show
from pathlib import WindowsPath, Path
from typing import Optional, Any, Type
from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from isu.ui.shell import Ui_shellOp

class ShellJob(QRunnable):

    def __init__(self, img_path: str, x: int, y: int, w: int, h: int) -> None:
        super(ShellJob, self).__init__()

    def run(self: QRunnable) -> None:
        return super().run()

class ShellOp(QWidget, Ui_shellOp):

    def __init__(self, parent: QWidget | None) -> None:
        super(ShellOp, self).__init__(parent)
        self.setupUi(self)
        self.title: str = "Shell Img"
        self.loadWidgets()
        self.loadConnections()

    @staticmethod
    def job() -> Type[QRunnable]:
        return ShellJob

    def run(self) -> QRunnable:
        return ShellJob(
            # apply_to=apply_to,
            # all_steps=all_steps,
            img_path=self.ShellImgPath.text(),
            x=self.shellFgX.value(),
            y=self.shellFgY.value(),
            w=self.shellFgW.value(),
            h=self.shellFgH.value()
        )

    def loadWidgets(self):
        self.shellImgPath : QLineEdit
        self.shellBrowseImgBtn : QPushButton

        self.shellFgX: QSpinBox
        self.shellFgY: QSpinBox
        self.shellFgW: QSpinBox
        self.shellFgH: QSpinBox

    def loadConnections(self):
        self.shellBrowseImgBtn.clicked.connect(self.browse_shell)

    @Slot()
    def browse_shell(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
            self.shellImgPath.setText(fileName)
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
        except: pass

show(__name__, ShellOp)