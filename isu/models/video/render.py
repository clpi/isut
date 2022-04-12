from enum import Enum
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
from PySide6.QtMultimediaWidgets import *
import av, cv2, ffmpeg

class RenderThread(QThread):

    class State(Enum):
        Queued = 0
        InStep = 1
        InSection = 2
        Finished = 3

    newFrame = Signal(QImage)
    state: State = State.Queued

    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.state = RenderThread.State.Queued
