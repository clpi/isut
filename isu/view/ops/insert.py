import os, sys
from isu import utils
from pathlib import WindowsPath, Path
from typing import Optional, Any, Type
from PIL import Image
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from isu.ui.insert import Ui_insertOp

class InsertJob(QRunnable):

    def __init__(self, img_path: str, x: int, y: int, w: int, h: int) -> None:
        super(InsertJob, self).__init__()

    def run(self: QRunnable) -> None:
        return super().run()

class InsertOp(QWidget, Ui_insertOp):

    def __init__(self, parent = None) -> None:
        super(InsertOp, self).__init__(parent)
        self.setupUi(self)
        self.title: str = "Insert Img"
        self.loadWidgets()
        self.loadConnections()

    @staticmethod
    def job() -> Type[QRunnable]:
        return InsertJob

    def run(self) -> QRunnable:
        return InsertJob(
            # apply_to=apply_to,
            # all_steps=all_steps,
            img_path=self.insertImgPath.text(),
            x=self.insertFgX.value(),
            y=self.insertFgY.value(),
            w=self.insertFgW.value(),
            h=self.insertFgH.value()
        )

    def loadWidgets(self):
        self.insertImgPath : QLineEdit
        self.insertBrowseImgBtn : QPushButton

        self.insertFgX: QSpinBox
        self.insertFgY: QSpinBox
        self.insertFgW: QSpinBox
        self.insertFgH: QSpinBox

    def loadConnections(self):
        self.insertBrowseImgBtn.clicked.connect(self.browse_insert)

    @Slot()
    def browse_insert(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self,"Browse for image files", "","All Files (*);;PNG files (*.png)")
            self.insertImgPath.setText(fileName)
            img_tmp = Image.open(fileName)
            iwidth, iheight = img_tmp.size
        except: pass

utils.show(__name__, InsertOp)