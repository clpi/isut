from typing import List, Sequence, MutableSequence
from PySide6.QtCore import *
from isu.view import UiLoader
from PySide6.QtWidgets import *
from isu.actions.op import Op

class OpPool(QThreadPool):
    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.ops: MutableSequence[Op] = []