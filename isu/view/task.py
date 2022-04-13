import enum
from copy import deepcopy
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from isu import utils
from isu.ui.optab import Ui_opsWidget
# from isu.models.task import Task
from isu.view.ops import AudioOp, InsertOp, CropOp, Nop, ShellOp, PaceOp, TextOp, RenderOp, SectionOp, ShellJob, SectionJob, CropJob, PaceJob, TextJob, RenderJob, AudioJob, InsertJob
from typing import List, Type

def jobFromIdx(idx: int = 0, parent = None) -> Type[QRunnable]:
    match idx:
        case 0: return ShellJob
        case 1: return InsertJob
        case 2: return CropJob
        case 3: return SectionJob
        case 4: return AudioJob
        case 5: return PaceJob
        case 6: return TextJob
        case 7: return RenderJob
        case _: return ShellJob

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
class TaskTabs(QTabWidget):
    def __init__(self, parent = None):
        super(TaskTabs, self).__init__(parent)
        self.loadConnections()

    def loadWidgets(self):
        pass


class TaskTab(QWidget, Ui_opsWidget):
    op: QWidget
    title: str = "Task"
    taskChanged = Signal(int)
    demoChanged = Signal(int)
    currentStepIndexChanged = Signal(int)


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
        self.stepIndexSpinbox: QSpinBox

        self.opParamsFrame: QGroupBox
        self.opParamsLayout: QVBoxLayout

    def loadConnections(self):
        self.taskCombo.currentIndexChanged.connect(self.taskComboChanged)
        self.demoCombo.currentIndexChanged.connect(self.demoComboChanged)
        self.stepIndexSpinbox.valueChanged.connect(self.stepIndexChanged)

    @Slot(int)
    def stepIndexChanged(self, i: int):
        self.onStepIndexChanged(i)
        self.currentTaskIndexChanged.emit(i)

    @Slot(int)
    def demoComboChanged(self, i: int):
        self.onDemoChanged(i)
        self.demoChanged.emit(i)

    @Slot(int)
    def taskComboChanged(self, i: int):
        self.onTaskChanged(i)
        self.taskChanged.emit(i)

    @Slot(int)
    def setOp(self, op_idx: int = 0):
        self.op = opFromIdx(op_idx)
        self.opParamsLayout.addWidget(self.op)
        self.opParamsLayout.setAlignment(self.op, Qt.AlignTop)

    @Slot(int)
    def onTaskChanged(self, op_idx: int = 0) -> None:
        # QMessageBox.about(self, "Task index changed", f"Task index changed to {op_idx}")
        old = self.opParamsLayout.itemAt(0).widget()
        old.setVisible(False)
        self.op = opFromIdx(op_idx)
        self.opParamsLayout.replaceWidget(old, self.op)
        self.taskCombo.setCurrentIndex(op_idx)
        self.title = self.op.title

    @Slot(int)
    def onStepIndexChanged(self, step_idx: int = 0):
        # QMessageBox.about(self, "Step index changed", f"Step index changed to {step_idx}")
        self.stepIndexSpinbox.setValue(step_idx)

    @Slot(int)
    def onDemoChanged(self, demo_idx: int = 0) -> None:
        # QMessageBox.about(self, "Demo index changed", f"Demo index changed to {demo_idx}")
        self.demoCombo.setCurrentIndex(demo_idx)



utils.show(__name__, TaskTab)