from operator import getitem
import os, sys, pathlib
import os, sys
from isu.utils import show
from pathlib import WindowsPath, Path
from typing import Optional, Any, Type
from PIL import Image
from typing import Optional, Sequence, Dict, Any
from PIL import Image
from av import VideoFormat, VideoFrame, AudioFormat
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from isu.ui.render import Ui_renderOp
from PySide6.QtMultimedia import *
from PySide6.QtMultimediaWidgets import *

AudioFmt = ["mp3", "wav", "flac", "ogg"]

class RenderJob(QRunnable):

    started = Signal()

    def __init__(self, format, title, res, fps, dir) -> None:
        super(RenderJob, self).__init__()

    def run(self: QRunnable) -> None:
        return super().run()

class RenderOp(QWidget, Ui_renderOp):

    def __init__(self, parent = None) -> None:
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.title: str = "Render"
        self.loadWidgets()
        self.loadConnections()

    @staticmethod
    def job() -> Type[QRunnable]:
        return RenderJob

    def outputPath(self) -> QFile:
        dir = self.renderOutputDir.text()
        title = self.renderOutputTitle.text()
        return QFile(os.path.join(dir, title + "." + self.fmt().name.lower()))


    def run(self) -> QRunnable:
        return RenderJob(
            res=(self.renderResH.value(), self.renderResW.value()),
            fps=self.renderFpsSb.value(),
            dir=pathlib.Path(self.renderOutputDir.text()),
            format=self.fmt(),
            title=self.renderOutputTitle.text(),
            # with_audio=self.withAudioCb.isChecked(),
            # with_cursor=self.withCursorCb.isChecked(),
            # with_text=self.withTextCb.isChecked(),
        )

    def loadWidgets(self):
        self.renderOutputTitle: QLineEdit
        self.renderOutputFormat: QComboBox
        self.renderResH: QSpinBox
        self.renderResW: QSpinBox
        self.renderFpsSb: QDoubleSpinBox

        self.withCursorCheck: QCheckBox
        self.withAudioCheck: QCheckBox
        self.withTextCheck: QCheckBox

        self.renderBrowseDirBtn: QPushButton
        self.renderOutputDir: QLineEdit

    def loadConnections(self):
        self.renderBrowseDirBtn.clicked.connect(self.browse_dir)

    @Slot(str, name="renderSetDir")
    def set_dir(self, dir: str):
        self.renderOutputDir.setText(dir)

    def set_rtitle(self, t: str):
        self.renderOutputTitleStr = t

    def browse_dir(self) -> pathlib.Path | None:
        try:
            odir = QFileDialog.getExistingDirectory(self,"Select output directory")
            self.set_dir(odir)
            return pathlib.Path(odir)
        except:
            return None

    # def fmt(self) -> Format:
    #     sel = self.renderOutputFormat.currentIndex()
    #     return Format(sel)

show(__name__, RenderOp)