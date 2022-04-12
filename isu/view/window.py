import sys
from typing import List, MutableSequence
from PySide6.QtCore import *
from isu.utils import show, browseFile, browseDir
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from isu.view.task import TaskTab
from isu.view.ops import Nop
from isu.ui.window import Ui_MainWindow
from isu.view.dialog import About, Preferences, Progress

# class Win(QMainWindow, Ui_MainWindow):
class Win(QMainWindow, Ui_MainWindow):

    stepAdded = Signal(int)
    demoAdded = Signal()
    scriptAdded = Signal()

    def __init__(self, parent = None):
        super(Win, self).__init__()
        self.steps: MutableSequence[TaskTab] = []
        self.demoLoaded: list = []
        self.scriptLoaded: list = []
        self.audioLoaded: list = []
        self.setupUi(self)
        self.loadWin()
        self.loadSteps()
        self.loadStatus()
        self.loadConnections()
        self.loadViews()

    def loadWin(self):
        self.setAcceptDrops(True)
        self.setUpdatesEnabled(True)
        self.setWindowIcon(QIcon(':/qt-project.org/logos/pysidelogo.png'))
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_CommandLink))

    def loadViews(self):
        self.dataLoadTabs: QTabWidget

        self.demoLoadedTab: QWidget
        self.demoLoadedTree: QTreeWidget
        self.demoLoadedLabel: QLabel
        self.demoLoadBtn: QPushButton
        self.browseDemoBtn: QPushButton

        self.audioLoadedTab: QWidget
        self.audioLoadedTree: QTreeWidget
        self.audioLoadedLabel: QLabel
        self.audioLoadBtn: QPushButton
        self.browseAudioBtn: QPushButton

        self.scriptsLoadedTab: QWidget
        self.scriptsLoadedTree: QTreeWidget
        self.scriptsLoadedLabel: QLabel
        self.scriptLoadBtn: QPushButton
        self.browseScriptBtn: QPushButton
        self.runStepsBtn: QPushButton

        self.opsTabs: QTabWidget
        self.opsView: QVBoxLayout

        self.taskStepsTable: QTableWidget

        self.demoViewTabs: QTabWidget
        self.demoMetadataTab: QWidget


    def loadStatus(self):
        self.statusBar: QStatusBar
        self.statusBar().showMessage("Ready", 2000)

    def loadSteps(self):
        self.opsView: QVBoxLayout
        self.opsTabs: QTabWidget
        self.setNoop()

    def loadConnections(self):
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionPreferences.triggered.connect(self.showPrefs)
        self.actionNew.triggered.connect(self.show_about)

        self.runStepsBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.runStepsBtn.clicked.connect(self.showProgress)
        self.browseDemoBtn.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        self.browseDemoBtn.clicked.connect(self.browseDemo)
        self.browseAudioBtn.clicked.connect(self.browseAudioDir)
        self.browseScriptBtn.clicked.connect(self.browseScript)

        self.audioLoadBtn.clicked.connect(self.browseAudioDir)
        self.demoLoadBtn.clicked.connect(self.browseDemo)
        self.scriptLoadBtn.clicked.connect(self.browseScript)

        self.addStepBtn.clicked.connect(self.addStepBtnClicked)

    @Slot()
    def browseScript(self) -> QFile | None:
        self.statusBar().showMessage("Browsing for script file...", 2000)
        if file := browseFile(self, "Open script file", QDir.currentPath(), "Docx files (*.docx)"):
            return QFile(file)
        return None

    @Slot()
    def addDefaultStep(self):
        self.steps.append(TaskTab(idx=0, parent=self.opsTabs))
        index = self.taskStepsTable.rowCount() - 1
        self.taskStepsTable.insertRow(index)
        self.taskStepsTable.setCellWidget(index, 0, QLabel(str(index)))
        self.taskStepsTable.setCellWidget(index, 1, QLabel(str(self.steps[index].title)))
        self.taskStepsTable.setCellWidget(index, 2, QLabel("[DEMO]"))
        self.taskStepsTable.selectRow(index)
        self.opsTabs.addTab(self.steps[index], self.steps[index].title)
        self.opsTabs.setCurrentIndex(index)
        self.opsTabs.widget(index).taskChanged.connect(self.onTaskChanged)

    def setNoop(self):
        self.opsTabs.clear()
        self.opsTabs.setEnabled(True)
        self.opsTabs.setTabsClosable(False)
        self.opsTabs.addTab(Nop(parent=self.opsTabs), "No Op")

    @Slot(int)
    def onTaskChanged(self, index: int):
        self.opsTabs.setCurrentIndex(index)
        self.opsTabs.widget(index).taskChanged.connect(self.onTaskChanged)
        self.opsTabs.widget(index).demoChanged.connect(self.onDemoChanged)

    @Slot(int)
    def onDemoChanged(self, index: int):
        self.demoLoadedTree.setCurrentIndex(index)

    @Slot(int)
    def onTabDeleted(self, index: int):
        self.taskStepsTable.removeRow(index)
        if self.opsTabs.count() == 0:
            self.setNoop()

    @Slot(int)
    def onTableRowDeleted(self, index: int):
        self.opsTabs.removeTab(index)

    @Slot(int, int)
    def onTabMoved(self, index: int, final: int):
        pass

    @Slot(int, int)
    def onRowMoved(self, index: int, final: int):
        pass

    @Slot(int)
    def onTabSelectionChanged(self, index: int):
        self.taskStepsTable.selectRow(index)

    @Slot(int)
    def onTableRowSelected(self, index: int):
        self.opsTabs.setCurrentIndex(index)

    @Slot(int)
    def onTaskRowDeleted(self, index: int):
        self.opsTabs.removeTab(index)

    @Slot()
    def addStepBtnClicked(self):
        if self.steps.__len__() == 0:
            if self.opsTabs.count() == 1:
                self.opsTabs.clear()
                self.opsTabs.setTabsClosable(True)
                self.opsTabs.setEnabled(True)
        self.addDefaultStep()

    @Slot()
    def browseDemo(self) -> QFile | None:
        self.statusBar().showMessage("Browsing for demo file...", 2000)
        if file := browseFile(self, "Open demo", QDir.currentPath(), "Demo files (*.demo)"):
            return QFile(file)
        return None

    @Slot()
    def browseAudioDir(self) -> QDir | None:
        self.statusBar().showMessage("Browsing for audio dir...", 2000)
        if directory := browseDir(self, "Open audio dir", QDir.currentPath(), ""):
            return QDir(directory)
        return None

    @Slot()
    def showPrefs(self):
        p = Preferences(parent=self)
        p.show()

    @Slot()
    def showAbout(self):
        a = About(parent=self)
        a.show()

    @Slot()
    def showProgress(self):
        p = Progress(parent=self)
        p.show()

    @Slot()
    def show_about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

show(__name__, Win)

    # a = QApplication()
    # w=Win()
    # w.show()
    # a.exec()