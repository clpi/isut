from PySide6.QtWidgets import *
from isu.utils import show
from PySide6.QtCore import Signal, Slot, SLOT, SIGNAL, SignalInstance, MetaSignal, QSize, QSignalMapper, Qt
from PySide6.QtGui import QAction

class About(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        # self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setAutoFillBackground(True)
        self.setWindowTitle("About Isu")
        self.header = QLabel("About", self)
        self.setWindowFlag(Qt.WindowType.Dialog)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setBaseSize(QSize(500, 350))
        self.setMinimumSize(QSize(500, 350))

        self.details = QLabel("This is the about dialog")

        self.okbtn = QPushButton("OK", self)
        self.btnbox = QHBoxLayout()
        self.btnbox.addWidget(self.okbtn)
        self.btnbox.setDirection(QBoxLayout.Direction.LeftToRight)
        self.btnbox.setContentsMargins(6, 2, 6, 2)
        # self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButtons())

        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.header)
        self.vlayout.addWidget(self.details)
        self.vlayout.addLayout(self.btnbox)

        self.setLayout(self.vlayout)

        # SignalInstance()

        self.okbtn.clicked.connect(self.close) # type: ignore


show(__name__, About)