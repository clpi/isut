import enum
from copy import deepcopy
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from isu import utils
from isu.ui.optab import Ui_opsWidget
from isu.view.ops import AudioOp, InsertOp, CropOp, Nop, ShellOp, PaceOp, TextOp, RenderOp, SectionOp
from typing import List, Type

class TaskTab(QWidget, Ui_opsWidget):
    op: QWidget
    title: str = "Task"
    taskChanged = Signal(int)
    demoChanged = Signal(int)

    @staticmethod
    def opFromIdx(idx: int = 0, parent = None) -> QWidget:
        match idx:
            case -1: return Nop(parent)
            case 0: return ShellOp(parent)
            case 1: return InsertOp(parent)
            case 2: return CropOp(parent)
            case 3: return SectionOp(parent)
            case 4: return AudioOp(parent)
            case 5: return PaceOp(parent)
            case 6: return TextOp(parent)
            case 7: return RenderOp(parent)
            case _: return ShellOp(parent)

    def __init__(self, idx: int = 0, parent = None):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setOp(idx)
        self.loadWidgets()
        self.loadConnections()

    def loadWidgets(self):
        self.allDemoCheck: QCheckBox
        self.allMarkedCheck: QCheckBox
        self.allStepsMarkedCheck: QCheckBox
        self.allStepsCheck: QCheckBox

        self.loadDemoBtn: QPushButton
        self.demoCombo: QComboBox
        self.taskCombo: QComboBox

        self.opParamsLayout: QVBoxLayout

    @Slot(int)
    def setCurrentDemo(self, index: int = 0):
        self.demoCombo.setCurrentIndex(index)

    def loadConnections(self):
        self.taskCombo.currentIndexChanged.connect(self.taskComboChanged)
        self.demoCombo.currentIndexChanged.connect(self.demoComboChanged)

    @Slot(int)
    def onTaskChanged(self, index: int = 0):
        """ Called when external fn changes current task index """
        self.taskCombo.setCurrentIndex(index)
        self.setOp(index)

    @Slot(int)
    def demoComboChanged(self, index: int = 0):
        self.demoChanged.emit(index)


    @Slot(int)
    def setOp(self, op_idx: int = 0):
        self.op = self.opFromIdx(op_idx)
        self.opParamsLayout.addWidget(self.op)
        self.opParamsLayout.setAlignment(self.op, Qt.AlignTop)

    @Slot(int)
    def taskComboChanged(self, op_idx: int = 0) -> None:
        old = self.opParamsLayout.itemAt(0).widget()
        old.setVisible(False)
        self.op = self.opFromIdx(op_idx)
        self.opParamsLayout.replaceWidget(old, self.op)
        self.taskChanged.emit(op_idx)
        # self.taskCombo.setCurrentIndex(op_idx)


utils.show(__name__, TaskTab)