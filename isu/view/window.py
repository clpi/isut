import sys
from typing import List, MutableSequence
from isu.models.task import TaskTableItem
from PySide6.QtCore import *
from isu.utils import show, browseFile, browseDir
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from isu.view.task import TaskTab, TaskTabs, opFromIdx
from isu.view.ops import Nop
from isu.ui.window import Ui_MainWindow
from isu.view.dialog import About, Preferences, Progress

# class Win(QMainWindow, Ui_MainWindow):
class Win(QMainWindow, Ui_MainWindow):

    stepAdded = Signal(int)
    demoAdded = Signal()
    scriptAdded = Signal()

    steps = []
    demoList = []

    def __init__(self, parent = None):
        super(Win, self).__init__()
        self.steps: MutableSequence[TaskTab] = []
        self.demoLoaded: list = []
        self.scriptLoaded: list = []
        self.audioLoaded: list = []
        self.setupUi(self)
        self.loadWin()
        self.loadSteps()
        self.loadTables()
        self.loadStatus()
        self.loadConnections()
        self.loadViews()

    def loadWin(self):
        self.setAcceptDrops(True)
        self.setUpdatesEnabled(True)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DialogApplyButton))
        self.setAnimated(True)

    def loadTables(self):
        # self.taskStepsTable.setModel(TaskTableItem)
        self.taskStepsTable.setCornerButtonEnabled(True)
        self.taskStepsTable.setUpdatesEnabled(True)

    def loadViews(self):
        # --------- DATA LOADED (top left) ------
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

        # --------- TASK DATA (bot left) ---------
        self.taskTabs: QTabWidget
        self.runStepsBtn: QPushButton

        self.stepUpBtn: QPushButton
        self.stepDownBtn: QPushButton

        self.taskStepsTable: QTableWidget

        # --------- OPS TABS (middle) ----------
        self.opsTabs: QTabWidget
        self.opsLayout: QVBoxLayout


        # ------- DEMO INFO (top right) -------
        self.demoViewTabs: QTabWidget
        self.demoStepsLabel: QLabel
        self.addDemoStepBtn: QPushButton
        self.delDemoStepBtn: QPushButton
        self.demoStepsOptBtn: QToolButton

        self.demoUpBtn: QPushButton
        self.demoDownBtn: QPushButton
        self.demoDeleteBtn: QPushButton
        self.demoEtcBtn: QToolButton
        self.demoCopyBtn: QPushButton
        self.demoStepsTree: QTreeWidget

        self.demoMetadataTab: QWidget

        # ------- SELECTION INFO (bot right) ------
        self.propTabs: QTabWidget
        self.propTabs.setMinimumWidth(375)
        self.propsTab: QWidget
        self.propsStack: QStackedWidget

        self.stepPropsPage: QWidget
        self.stepPropsLabel: QLabel
        self.stepPropsOptsBtn: QToolButton
        self.stepPropsInfoBtn: QPushButton
        self.stepPropsResetBtn: QPushButton
        self.stepPropsTable: QTableWidget


        self.sectPropsPage: QWidget
        self.sectPropsLabel: QLabel
        self.sectPropsOptsBtn: QToolButton
        self.sectPropsInfoBtn: QPushButton
        self.sectPropsResetBtn: QPushButton
        self.sectPropsTable: QTableWidget

        self.previewTab: QWidget
        self.previewGfx: QGraphicsView

    def loadStatus(self):
        self.statusBar: QStatusBar
        self.statusBar().showMessage("Ready", 2000)

    def loadSteps(self):
        self.opsLayout: QVBoxLayout
        self.opsTabs: QTabWidget
        self.setNoop()

    def loadConnections(self):
        # self.actionNewStep.triggered.connect(self.addStep)
        # self.actionRun.triggered.connect(self.runSteps)
        self.actionPreferences.triggered.connect(self.showPrefs)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionOpenDemo.triggered.connect(self.browseDemo)
        self.actionOpenAudio.triggered.connect(self.browseAudioDir)
        self.actionOpenScript.triggered.connect(self.browseScript)

        self.runStepsBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.runStepsBtn.clicked.connect(self.showProgress)
        self.browseDemoBtn.setIcon(self.style().standardIcon(QStyle.SP_FileIcon))
        self.browseDemoBtn.clicked.connect(self.browseDemo)
        self.browseAudioBtn.clicked.connect(self.browseAudioDir)
        self.browseScriptBtn.clicked.connect(self.browseScript)

        self.audioLoadBtn.clicked.connect(self.browseAudioDir)
        self.demoLoadBtn.clicked.connect(self.browseDemo)
        self.scriptLoadBtn.clicked.connect(self.browseScript)

        self.addStepBtn.setIcon(self.style().standardIcon(QStyle.SP_CustomBase))
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
        # self.disconnect()
        self.opsTabs.setCurrentIndex(index)
        self.connect()

    def setNoop(self):
        self.opsTabs.clear()
        self.opsTabs.setEnabled(True)
        self.opsTabs.setTabsClosable(False)
        self.opsTabs.addTab(Nop(parent=self.opsTabs), "No Op")

    @Slot(int)
    def onStepTaskChanged(self, task_idx: int):
        self.opsTabs.currentWidget().onTaskChanged(task_idx)
        row = self.taskStepsTable.currentRow()
        title = self.opsTabs.currentWidget().title
        self.taskStepsTable.setItem(row, 2, QTableWidgetItem(title))
        self.setWindowTitle("Isu: " + str(title))

    @Slot(int)
    def onStepChanged(self, index: int):
        self.opsTabs.setCurrentIndex(index)

    def connect(self):
        self.opsTabs.currentWidget().taskChanged.connect(self.onStepTaskChanged)
        self.opsTabs.currentWidget().demoChanged.connect(self.onDemoChanged)
        self.opsTabs.currentWidget().currentStepIndexChanged.connect(self.onStepChanged)

    def disconnect(self):
        self.opsTabs.currentWidget().taskChanged.disconnect(self.onStepTaskChanged)
        self.opsTabs.currentWidget().demoChanged.disconnect(self.onDemoChanged)
        self.opsTabs.currentWidget().currentStepIndexChanged.disconnect(self.onStepChanged)

    @Slot(int)
    def onDemoChanged(self, index: int):
        self.demoLoadedTree.setCurrentIndex(index)

    @Slot(int)
    def onTabDeleted(self, index: int):
        self.taskStepsTable.removeRow(index)
        if self.opsTabs.count() == 0:
            self.setNoop()

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
    def onTableRowDeleted(self, index: int):
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
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

    @Slot()
    def showProgress(self):
        p = Progress(parent=self)
        p.show()

    def selectedTaskStep(self) -> int:
        tab_i = self.opsTabs.currentIndex()
        table_i = self.taskStepsTable.currentRow()
        return table_i

    def selectedDemo(self) -> int:
        return self.demoLoadedTree.currentIndex().row()

    def selectedTaskOp(self) -> int:
        return self.opsTabs.currentIn

show(__name__, Win)