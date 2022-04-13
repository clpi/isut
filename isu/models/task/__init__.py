from .table import TaskTable, TaskTableItem
from PySide6.QtCore import QObject, QRunnable

class Task(QRunnable):

    def __init__(self, idx: int = 0, parent = None) -> None:
        super(Task, self).__init__()
        # self = self.jobFromIdx(idx, parent)

    # @staticmethod
    # def jobFromIdx(idx: int = 0, parent = None) -> QRunnable:
    #     match idx:
    #         case -1: return Nop(parent)
    #         case 0: return ShellOp(parent)
    #         case 1: return InsertOp(parent)
    #         case 2: return CropOp(parent)
    #         case 3: return SectionOp(parent)
    #         case 4: return AudioOp(parent)
    #         case 5: return PaceOp(parent)
    #         case 6: return TextOp(parent)
    #         case 7: return RenderOp(parent)
    #         case _: return ShellOp(parent)
