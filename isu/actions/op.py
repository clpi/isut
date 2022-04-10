from enum import Enum, auto
from typing import Sequence, MutableMapping, MutableSequence, Type
from PySide6.QtCore import *
from isu.view import UiLoader
from PySide6.QtWidgets import *

class Op(QRunnable):

    class Ops(Enum):
        Nop = -1
        Shell = 0
        Insert = 1
        Crop = 2
        Section = 3
        Audio = 4
        Pacing = 5
        Text = 6
        Render  = 7

    @classmethod
    def ui(cls, base = None):
        uil = UiLoader()
        match cls:
            case Op.Ops.Nop: return uil.loadUi("isu/ui/ops/nop.ui", base)
            case Op.Ops.Shell: return uil.loadUi("isu/ui/ops/shell.ui", base)
            case Op.Ops.Insert: return uil.loadUi("isu/ui/ops/shell.ui", base)
            case Op.Ops.Crop: return uil.loadUi("isu/ui/ops/shell.ui", base)
            case Op.Ops.Section: return uil.loadUi("isu/ui/ops/shell.ui", base)
            case Op.Ops.Audio: return uil.loadUi("isu/ui/ops/shell.ui", base)
            case Op.Ops.Pacing: return uil.loadUi("isu/ui/ops/shell.ui", base)
            case Op.Ops.Text: return uil.loadUi("isu/ui/ops/shell.ui", base)
            case Op.Ops.Render: return uil.loadUi("isu/ui/ops/shell.ui", base)
        

    class Signals(QObject):
        started = Signal(bool)
        progress = Signal(float)
        msg = Signal(str)

        def connect(self, parent):
            self.started.connect(parent.on_op_started)
            self.progress.connect(parent.on_op_progress)
            self.msg.connect(parent.on_op_msg)
            self.msg.connect(parent.on_op_msg)

        def log(self, s: str):
            self.msg.emit(s)

        def __init__(self) -> None:
            super().__init__()
            self.op: Op.Ops = Op.Ops.Nop
            self.signals = Op.Signals()

    def __init__(self, opidx: int = -1, parent = None):
        self.op = Op.Ops(opidx)
        self.signals = Op.Signals()
        self.signals.connect(parent)

    @classmethod
    def run_op(cls, opidx: int, parent = None):
        op = Op(opidx, parent)
        op.run()
        
    @Slot()
    def run(self) -> None:
        match self.op:
            case Op.Ops.Nop:
                self.signals.msg.emit("NOP running")
            case Op.Ops.Shell:
                self.signals.msg.emit("NOP")
            case Op.Ops.Crop:
                pass
            case Op.Ops.Section:
                pass
            case Op.Ops.Audio:
                pass
            case Op.Ops.Pacing:
                pass
            case Op.Ops.Text:
                pass
            case Op.Ops.Render:
                pass
            case _:
                pass



        
