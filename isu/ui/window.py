# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGraphicsView, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QToolButton, QTreeView,
    QTreeWidget, QTreeWidgetItem, QUndoView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1240, 760)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1240, 760))
        MainWindow.setMaximumSize(QSize(16777203, 16777210))
        font = QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionStep = QAction(MainWindow)
        self.actionStep.setObjectName(u"actionStep")
        self.actionOpen_Demo = QAction(MainWindow)
        self.actionOpen_Demo.setObjectName(u"actionOpen_Demo")
        self.actionOpen_Audio = QAction(MainWindow)
        self.actionOpen_Audio.setObjectName(u"actionOpen_Audio")
        self.actionOpen_Script = QAction(MainWindow)
        self.actionOpen_Script.setObjectName(u"actionOpen_Script")
        self.actionSave_Jobs = QAction(MainWindow)
        self.actionSave_Jobs.setObjectName(u"actionSave_Jobs")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionQueue = QAction(MainWindow)
        self.actionQueue.setObjectName(u"actionQueue")
        self.actionJobs_Editor = QAction(MainWindow)
        self.actionJobs_Editor.setObjectName(u"actionJobs_Editor")
        self.actionJobs_Editor.setCheckable(True)
        self.actionJobs_Editor.setChecked(True)
        self.actionXML_Editor = QAction(MainWindow)
        self.actionXML_Editor.setObjectName(u"actionXML_Editor")
        self.actionXML_Editor.setCheckable(True)
        self.actionScript_Editor = QAction(MainWindow)
        self.actionScript_Editor.setObjectName(u"actionScript_Editor")
        self.actionScript_Editor.setCheckable(True)
        self.actionFull_Screen = QAction(MainWindow)
        self.actionFull_Screen.setObjectName(u"actionFull_Screen")
        self.actionFull_Screen.setCheckable(True)
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionClear_jobs = QAction(MainWindow)
        self.actionClear_jobs.setObjectName(u"actionClear_jobs")
        self.actionDelete_current_task = QAction(MainWindow)
        self.actionDelete_current_task.setObjectName(u"actionDelete_current_task")
        self.actionDuplicate_current_task = QAction(MainWindow)
        self.actionDuplicate_current_task.setObjectName(u"actionDuplicate_current_task")
        self.actionReset_current_task = QAction(MainWindow)
        self.actionReset_current_task.setObjectName(u"actionReset_current_task")
        self.actionMenubar = QAction(MainWindow)
        self.actionMenubar.setObjectName(u"actionMenubar")
        self.actionMenubar.setCheckable(True)
        self.actionMenubar.setChecked(True)
        self.actionStatusbar = QAction(MainWindow)
        self.actionStatusbar.setObjectName(u"actionStatusbar")
        self.actionStatusbar.setCheckable(True)
        self.actionRun_current_task = QAction(MainWindow)
        self.actionRun_current_task.setObjectName(u"actionRun_current_task")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave_current_state = QAction(MainWindow)
        self.actionSave_current_state.setObjectName(u"actionSave_current_state")
        self.actionReset_changes = QAction(MainWindow)
        self.actionReset_changes.setObjectName(u"actionReset_changes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.centralTabs = QStackedWidget(self.centralwidget)
        self.centralTabs.setObjectName(u"centralTabs")
        self.centralTabs.setMouseTracking(True)
        self.centralTabs.setAcceptDrops(True)
        self.centralTabs.setLineWidth(0)
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.centralTabs.addWidget(self.startPage)
        self.jobsPage = QWidget()
        self.jobsPage.setObjectName(u"jobsPage")
        self.jobsPage.setMouseTracking(True)
        self.jobsPage.setAcceptDrops(True)
        self.jobsPage.setAutoFillBackground(True)
        self.horizontalLayout_6 = QHBoxLayout(self.jobsPage)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.splitter_3 = QSplitter(self.jobsPage)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setMinimumSize(QSize(325, 0))
        self.splitter.setMaximumSize(QSize(375, 16777215))
        self.splitter.setBaseSize(QSize(375, 0))
        self.splitter.setOrientation(Qt.Vertical)
        self.dataLoadTabs = QTabWidget(self.splitter)
        self.dataLoadTabs.setObjectName(u"dataLoadTabs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(8)
        sizePolicy2.setHeightForWidth(self.dataLoadTabs.sizePolicy().hasHeightForWidth())
        self.dataLoadTabs.setSizePolicy(sizePolicy2)
        self.dataLoadTabs.setMinimumSize(QSize(325, 0))
        self.dataLoadTabs.setMaximumSize(QSize(239824, 16777215))
        self.dataLoadTabs.setBaseSize(QSize(375, 0))
        self.dataLoadTabs.setStyleSheet(u"")
        self.dataLoadTabs.setTabPosition(QTabWidget.North)
        self.demoLoadedTab = QWidget()
        self.demoLoadedTab.setObjectName(u"demoLoadedTab")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.demoLoadedTab.sizePolicy().hasHeightForWidth())
        self.demoLoadedTab.setSizePolicy(sizePolicy3)
        self.demoLoadedTab.setMaximumSize(QSize(375, 16777215))
        self.verticalLayout_34 = QVBoxLayout(self.demoLoadedTab)
        self.verticalLayout_34.setSpacing(2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(4, 2, 4, 2)
        self.dataLoadedTopBtns = QHBoxLayout()
        self.dataLoadedTopBtns.setSpacing(4)
        self.dataLoadedTopBtns.setObjectName(u"dataLoadedTopBtns")
        self.dataLoadedTopBtns.setContentsMargins(0, -1, 0, -1)
        self.demoLoadedLabel = QLabel(self.demoLoadedTab)
        self.demoLoadedLabel.setObjectName(u"demoLoadedLabel")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setKerning(True)
        self.demoLoadedLabel.setFont(font1)
        self.demoLoadedLabel.setIndent(0)

        self.dataLoadedTopBtns.addWidget(self.demoLoadedLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dataLoadedTopBtns.addItem(self.horizontalSpacer_2)

        self.browseDemoBtn = QPushButton(self.demoLoadedTab)
        self.browseDemoBtn.setObjectName(u"browseDemoBtn")
        self.browseDemoBtn.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setKerning(True)
        self.browseDemoBtn.setFont(font2)
        self.browseDemoBtn.setAutoDefault(True)

        self.dataLoadedTopBtns.addWidget(self.browseDemoBtn)


        self.verticalLayout_34.addLayout(self.dataLoadedTopBtns)

        self.demoLoadedTree = QTableWidget(self.demoLoadedTab)
        if (self.demoLoadedTree.columnCount() < 3):
            self.demoLoadedTree.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.demoLoadedTree.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.demoLoadedTree.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.demoLoadedTree.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.demoLoadedTree.setObjectName(u"demoLoadedTree")
        self.demoLoadedTree.setMinimumSize(QSize(350, 0))

        self.verticalLayout_34.addWidget(self.demoLoadedTree)

        self.dataLoadedBtns = QHBoxLayout()
        self.dataLoadedBtns.setSpacing(0)
        self.dataLoadedBtns.setObjectName(u"dataLoadedBtns")
        self.demoRecentBtn = QPushButton(self.demoLoadedTab)
        self.demoRecentBtn.setObjectName(u"demoRecentBtn")
        self.demoRecentBtn.setAutoDefault(False)
        self.demoRecentBtn.setFlat(False)

        self.dataLoadedBtns.addWidget(self.demoRecentBtn)

        self.demoSavedBtn = QPushButton(self.demoLoadedTab)
        self.demoSavedBtn.setObjectName(u"demoSavedBtn")

        self.dataLoadedBtns.addWidget(self.demoSavedBtn)

        self.demoRemoveBtn = QPushButton(self.demoLoadedTab)
        self.demoRemoveBtn.setObjectName(u"demoRemoveBtn")

        self.dataLoadedBtns.addWidget(self.demoRemoveBtn)

        self.demoLoadBtn = QPushButton(self.demoLoadedTab)
        self.demoLoadBtn.setObjectName(u"demoLoadBtn")

        self.dataLoadedBtns.addWidget(self.demoLoadBtn)

        self.demoEtcBtn = QToolButton(self.demoLoadedTab)
        self.demoEtcBtn.setObjectName(u"demoEtcBtn")
        self.demoEtcBtn.setPopupMode(QToolButton.MenuButtonPopup)
        self.demoEtcBtn.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.demoEtcBtn.setAutoRaise(False)
        self.demoEtcBtn.setArrowType(Qt.DownArrow)

        self.dataLoadedBtns.addWidget(self.demoEtcBtn)


        self.verticalLayout_34.addLayout(self.dataLoadedBtns)

        self.dataLoadTabs.addTab(self.demoLoadedTab, "")
        self.audioLoadedTab = QWidget()
        self.audioLoadedTab.setObjectName(u"audioLoadedTab")
        sizePolicy3.setHeightForWidth(self.audioLoadedTab.sizePolicy().hasHeightForWidth())
        self.audioLoadedTab.setSizePolicy(sizePolicy3)
        self.audioLoadedTab.setMaximumSize(QSize(375, 16777215))
        self.verticalLayout_36 = QVBoxLayout(self.audioLoadedTab)
        self.verticalLayout_36.setSpacing(2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(4, 2, 4, 2)
        self.audioLoadedTopBtns = QHBoxLayout()
        self.audioLoadedTopBtns.setSpacing(4)
        self.audioLoadedTopBtns.setObjectName(u"audioLoadedTopBtns")
        self.audioLoadedLabel = QLabel(self.audioLoadedTab)
        self.audioLoadedLabel.setObjectName(u"audioLoadedLabel")

        self.audioLoadedTopBtns.addWidget(self.audioLoadedLabel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.audioLoadedTopBtns.addItem(self.horizontalSpacer_7)

        self.browseAudioBtn = QPushButton(self.audioLoadedTab)
        self.browseAudioBtn.setObjectName(u"browseAudioBtn")

        self.audioLoadedTopBtns.addWidget(self.browseAudioBtn)


        self.verticalLayout_36.addLayout(self.audioLoadedTopBtns)

        self.audioLoadedTree = QTreeWidget(self.audioLoadedTab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Name");
        self.audioLoadedTree.setHeaderItem(__qtreewidgetitem)
        self.audioLoadedTree.setObjectName(u"audioLoadedTree")

        self.verticalLayout_36.addWidget(self.audioLoadedTree)

        self.audioLoadedBtns = QWidget(self.audioLoadedTab)
        self.audioLoadedBtns.setObjectName(u"audioLoadedBtns")
        self.horizontalLayout_7 = QHBoxLayout(self.audioLoadedBtns)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.audioRecentBtn = QPushButton(self.audioLoadedBtns)
        self.audioRecentBtn.setObjectName(u"audioRecentBtn")

        self.horizontalLayout_7.addWidget(self.audioRecentBtn)

        self.audioSavedBtn = QPushButton(self.audioLoadedBtns)
        self.audioSavedBtn.setObjectName(u"audioSavedBtn")

        self.horizontalLayout_7.addWidget(self.audioSavedBtn)

        self.audioLoadBtn = QPushButton(self.audioLoadedBtns)
        self.audioLoadBtn.setObjectName(u"audioLoadBtn")

        self.horizontalLayout_7.addWidget(self.audioLoadBtn)

        self.audioRemoveBtn = QPushButton(self.audioLoadedBtns)
        self.audioRemoveBtn.setObjectName(u"audioRemoveBtn")

        self.horizontalLayout_7.addWidget(self.audioRemoveBtn)

        self.audioEtcBtn = QToolButton(self.audioLoadedBtns)
        self.audioEtcBtn.setObjectName(u"audioEtcBtn")

        self.horizontalLayout_7.addWidget(self.audioEtcBtn)


        self.verticalLayout_36.addWidget(self.audioLoadedBtns)

        self.dataLoadTabs.addTab(self.audioLoadedTab, "")
        self.scriptsLoadedTab = QWidget()
        self.scriptsLoadedTab.setObjectName(u"scriptsLoadedTab")
        self.verticalLayout_21 = QVBoxLayout(self.scriptsLoadedTab)
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(4, 2, 4, 2)
        self.scriptsLoadedTopBtns = QHBoxLayout()
        self.scriptsLoadedTopBtns.setObjectName(u"scriptsLoadedTopBtns")
        self.scriptsLoadedLabel = QLabel(self.scriptsLoadedTab)
        self.scriptsLoadedLabel.setObjectName(u"scriptsLoadedLabel")

        self.scriptsLoadedTopBtns.addWidget(self.scriptsLoadedLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.scriptsLoadedTopBtns.addItem(self.horizontalSpacer_3)

        self.browseScriptBtn = QPushButton(self.scriptsLoadedTab)
        self.browseScriptBtn.setObjectName(u"browseScriptBtn")
        self.browseScriptBtn.setAutoDefault(True)
        self.browseScriptBtn.setFlat(False)

        self.scriptsLoadedTopBtns.addWidget(self.browseScriptBtn)


        self.verticalLayout_21.addLayout(self.scriptsLoadedTopBtns)

        self.scriptsLoadedTree = QTableWidget(self.scriptsLoadedTab)
        self.scriptsLoadedTree.setObjectName(u"scriptsLoadedTree")

        self.verticalLayout_21.addWidget(self.scriptsLoadedTree)

        self.scriptsLoadedBtns = QHBoxLayout()
        self.scriptsLoadedBtns.setSpacing(0)
        self.scriptsLoadedBtns.setObjectName(u"scriptsLoadedBtns")
        self.scriptRecentsBtn = QPushButton(self.scriptsLoadedTab)
        self.scriptRecentsBtn.setObjectName(u"scriptRecentsBtn")

        self.scriptsLoadedBtns.addWidget(self.scriptRecentsBtn)

        self.scriptsSavedBtn = QPushButton(self.scriptsLoadedTab)
        self.scriptsSavedBtn.setObjectName(u"scriptsSavedBtn")

        self.scriptsLoadedBtns.addWidget(self.scriptsSavedBtn)

        self.scriptRemoveBtn = QPushButton(self.scriptsLoadedTab)
        self.scriptRemoveBtn.setObjectName(u"scriptRemoveBtn")

        self.scriptsLoadedBtns.addWidget(self.scriptRemoveBtn)

        self.scriptLoadBtn = QPushButton(self.scriptsLoadedTab)
        self.scriptLoadBtn.setObjectName(u"scriptLoadBtn")

        self.scriptsLoadedBtns.addWidget(self.scriptLoadBtn)

        self.scriptsEtcBtn = QToolButton(self.scriptsLoadedTab)
        self.scriptsEtcBtn.setObjectName(u"scriptsEtcBtn")

        self.scriptsLoadedBtns.addWidget(self.scriptsEtcBtn)


        self.verticalLayout_21.addLayout(self.scriptsLoadedBtns)

        self.dataLoadTabs.addTab(self.scriptsLoadedTab, "")
        self.splitter.addWidget(self.dataLoadTabs)
        self.taskTabs = QTabWidget(self.splitter)
        self.taskTabs.setObjectName(u"taskTabs")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.taskTabs.sizePolicy().hasHeightForWidth())
        self.taskTabs.setSizePolicy(sizePolicy4)
        self.taskTabs.setMinimumSize(QSize(325, 0))
        self.taskTabs.setMaximumSize(QSize(375, 16777215))
        self.taskTabs.setCursor(QCursor(Qt.ArrowCursor))
        self.taskStepsTab = QWidget()
        self.taskStepsTab.setObjectName(u"taskStepsTab")
        self.taskStepsTab.setMaximumSize(QSize(375, 16777215))
        self.verticalLayout_30 = QVBoxLayout(self.taskStepsTab)
        self.verticalLayout_30.setSpacing(2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(4, 2, 4, 2)
        self.taskStepsTopBtns = QHBoxLayout()
        self.taskStepsTopBtns.setSpacing(4)
        self.taskStepsTopBtns.setObjectName(u"taskStepsTopBtns")
        self.taskStepsTopBtns.setContentsMargins(0, -1, 0, -1)
        self.taskStepsTitle = QLabel(self.taskStepsTab)
        self.taskStepsTitle.setObjectName(u"taskStepsTitle")
        self.taskStepsTitle.setFont(font1)
        self.taskStepsTitle.setIndent(8)

        self.taskStepsTopBtns.addWidget(self.taskStepsTitle)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.taskStepsTopBtns.addItem(self.horizontalSpacer_11)

        self.stepTargetCombo = QComboBox(self.taskStepsTab)
        self.stepTargetCombo.setObjectName(u"stepTargetCombo")
        self.stepTargetCombo.setFrame(True)

        self.taskStepsTopBtns.addWidget(self.stepTargetCombo)

        self.addStepBtn = QPushButton(self.taskStepsTab)
        self.addStepBtn.setObjectName(u"addStepBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.addStepBtn.sizePolicy().hasHeightForWidth())
        self.addStepBtn.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setKerning(False)
        self.addStepBtn.setFont(font3)
        self.addStepBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.addStepBtn.setContextMenuPolicy(Qt.PreventContextMenu)
        self.addStepBtn.setAcceptDrops(False)
        self.addStepBtn.setAutoFillBackground(False)
        self.addStepBtn.setIconSize(QSize(16, 16))
        self.addStepBtn.setAutoDefault(True)
        self.addStepBtn.setFlat(False)

        self.taskStepsTopBtns.addWidget(self.addStepBtn)


        self.verticalLayout_30.addLayout(self.taskStepsTopBtns)

        self.taskStepsTable = QTableWidget(self.taskStepsTab)
        if (self.taskStepsTable.columnCount() < 3):
            self.taskStepsTable.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.taskStepsTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.taskStepsTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.taskStepsTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.taskStepsTable.setObjectName(u"taskStepsTable")
        self.taskStepsTable.setFrameShape(QFrame.StyledPanel)
        self.taskStepsTable.setFrameShadow(QFrame.Sunken)
        self.taskStepsTable.setLineWidth(0)
        self.taskStepsTable.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.taskStepsTable.setTabKeyNavigation(True)
        self.taskStepsTable.setDragEnabled(True)
        self.taskStepsTable.setDragDropOverwriteMode(False)
        self.taskStepsTable.setDragDropMode(QAbstractItemView.DragDrop)
        self.taskStepsTable.setDefaultDropAction(Qt.MoveAction)
        self.taskStepsTable.setAlternatingRowColors(True)
        self.taskStepsTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_30.addWidget(self.taskStepsTable)

        self.taskStepsBtns = QHBoxLayout()
        self.taskStepsBtns.setSpacing(0)
        self.taskStepsBtns.setObjectName(u"taskStepsBtns")
        self.stepUpBtn = QPushButton(self.taskStepsTab)
        self.stepUpBtn.setObjectName(u"stepUpBtn")

        self.taskStepsBtns.addWidget(self.stepUpBtn)

        self.stepDownBtn = QPushButton(self.taskStepsTab)
        self.stepDownBtn.setObjectName(u"stepDownBtn")

        self.taskStepsBtns.addWidget(self.stepDownBtn)

        self.deleteStepBtn = QPushButton(self.taskStepsTab)
        self.deleteStepBtn.setObjectName(u"deleteStepBtn")

        self.taskStepsBtns.addWidget(self.deleteStepBtn)

        self.copyStepBtn = QPushButton(self.taskStepsTab)
        self.copyStepBtn.setObjectName(u"copyStepBtn")

        self.taskStepsBtns.addWidget(self.copyStepBtn)

        self.runStepsBtn = QPushButton(self.taskStepsTab)
        self.runStepsBtn.setObjectName(u"runStepsBtn")
        self.runStepsBtn.setAutoFillBackground(False)
        self.runStepsBtn.setAutoDefault(True)

        self.taskStepsBtns.addWidget(self.runStepsBtn)

        self.etcStepsBtn = QToolButton(self.taskStepsTab)
        self.etcStepsBtn.setObjectName(u"etcStepsBtn")
        self.etcStepsBtn.setPopupMode(QToolButton.MenuButtonPopup)
        self.etcStepsBtn.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.etcStepsBtn.setArrowType(Qt.NoArrow)

        self.taskStepsBtns.addWidget(self.etcStepsBtn)


        self.verticalLayout_30.addLayout(self.taskStepsBtns)

        self.taskTabs.addTab(self.taskStepsTab, "")
        self.taskHistoryTab = QWidget()
        self.taskHistoryTab.setObjectName(u"taskHistoryTab")
        self.verticalLayout_37 = QVBoxLayout(self.taskHistoryTab)
        self.verticalLayout_37.setSpacing(2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(4, 2, 4, 2)
        self.taskHistoryTopBtns = QHBoxLayout()
        self.taskHistoryTopBtns.setObjectName(u"taskHistoryTopBtns")
        self.taskHistoryLabel = QLabel(self.taskHistoryTab)
        self.taskHistoryLabel.setObjectName(u"taskHistoryLabel")

        self.taskHistoryTopBtns.addWidget(self.taskHistoryLabel)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.taskHistoryTopBtns.addItem(self.horizontalSpacer_8)

        self.taskHistoryCombo = QComboBox(self.taskHistoryTab)
        self.taskHistoryCombo.addItem("")
        self.taskHistoryCombo.addItem("")
        self.taskHistoryCombo.addItem("")
        self.taskHistoryCombo.setObjectName(u"taskHistoryCombo")

        self.taskHistoryTopBtns.addWidget(self.taskHistoryCombo)

        self.browseTaskHistoryBtn = QPushButton(self.taskHistoryTab)
        self.browseTaskHistoryBtn.setObjectName(u"browseTaskHistoryBtn")

        self.taskHistoryTopBtns.addWidget(self.browseTaskHistoryBtn)


        self.verticalLayout_37.addLayout(self.taskHistoryTopBtns)

        self.tableView_2 = QTableView(self.taskHistoryTab)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_37.addWidget(self.tableView_2)

        self.taskHistoryBtns = QHBoxLayout()
        self.taskHistoryBtns.setSpacing(0)
        self.taskHistoryBtns.setObjectName(u"taskHistoryBtns")
        self.taskHistoryLoadBtn = QPushButton(self.taskHistoryTab)
        self.taskHistoryLoadBtn.setObjectName(u"taskHistoryLoadBtn")

        self.taskHistoryBtns.addWidget(self.taskHistoryLoadBtn)

        self.taskHistorySaveBtn = QPushButton(self.taskHistoryTab)
        self.taskHistorySaveBtn.setObjectName(u"taskHistorySaveBtn")

        self.taskHistoryBtns.addWidget(self.taskHistorySaveBtn)

        self.taskHistoryEditBtn = QPushButton(self.taskHistoryTab)
        self.taskHistoryEditBtn.setObjectName(u"taskHistoryEditBtn")

        self.taskHistoryBtns.addWidget(self.taskHistoryEditBtn)

        self.taskHistoryRemoveBtn = QPushButton(self.taskHistoryTab)
        self.taskHistoryRemoveBtn.setObjectName(u"taskHistoryRemoveBtn")

        self.taskHistoryBtns.addWidget(self.taskHistoryRemoveBtn)

        self.taskHistoryEtcBtn = QToolButton(self.taskHistoryTab)
        self.taskHistoryEtcBtn.setObjectName(u"taskHistoryEtcBtn")

        self.taskHistoryBtns.addWidget(self.taskHistoryEtcBtn)


        self.verticalLayout_37.addLayout(self.taskHistoryBtns)

        self.taskTabs.addTab(self.taskHistoryTab, "")
        self.taskUndoTab = QWidget()
        self.taskUndoTab.setObjectName(u"taskUndoTab")
        self.taskUndoTab.setMaximumSize(QSize(16777213, 16777215))
        self.taskUndoTab.setFont(font2)
        self.verticalLayout_22 = QVBoxLayout(self.taskUndoTab)
        self.verticalLayout_22.setSpacing(4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.taskUndoTopBtns = QHBoxLayout()
        self.taskUndoTopBtns.setObjectName(u"taskUndoTopBtns")
        self.label_4 = QLabel(self.taskUndoTab)
        self.label_4.setObjectName(u"label_4")

        self.taskUndoTopBtns.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.taskUndoTopBtns.addItem(self.horizontalSpacer_4)

        self.toolButton_16 = QToolButton(self.taskUndoTab)
        self.toolButton_16.setObjectName(u"toolButton_16")

        self.taskUndoTopBtns.addWidget(self.toolButton_16)


        self.verticalLayout_22.addLayout(self.taskUndoTopBtns)

        self.undoView = QUndoView(self.taskUndoTab)
        self.undoView.setObjectName(u"undoView")
        self.undoView.setEnabled(True)

        self.verticalLayout_22.addWidget(self.undoView)

        self.taskTabs.addTab(self.taskUndoTab, "")
        self.splitter.addWidget(self.taskTabs)
        self.splitter_3.addWidget(self.splitter)
        self.opsView = QWidget(self.splitter_3)
        self.opsView.setObjectName(u"opsView")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.opsView.sizePolicy().hasHeightForWidth())
        self.opsView.setSizePolicy(sizePolicy6)
        self.opsView.setMinimumSize(QSize(425, 0))
        self.opsView.setMaximumSize(QSize(16777215, 16777212))
        self.opsView.setBaseSize(QSize(460, 0))
        self.opsView.setFocusPolicy(Qt.NoFocus)
        self.opsView.setLayoutDirection(Qt.LeftToRight)
        self.opsView.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.opsView)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.opsTabs = QTabWidget(self.opsView)
        self.opsTabs.setObjectName(u"opsTabs")
        self.opsTabs.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(8)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.opsTabs.sizePolicy().hasHeightForWidth())
        self.opsTabs.setSizePolicy(sizePolicy7)
        self.opsTabs.setBaseSize(QSize(500, 0))
        self.opsTabs.setTabsClosable(True)
        self.opsTabs.setMovable(True)

        self.verticalLayout_2.addWidget(self.opsTabs)

        self.splitter_3.addWidget(self.opsView)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy1.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy1)
        self.splitter_2.setMinimumSize(QSize(300, 0))
        self.splitter_2.setBaseSize(QSize(350, 0))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.demoViewTabs = QTabWidget(self.splitter_2)
        self.demoViewTabs.setObjectName(u"demoViewTabs")
        self.demoViewTabs.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.demoViewTabs.sizePolicy().hasHeightForWidth())
        self.demoViewTabs.setSizePolicy(sizePolicy2)
        self.demoViewTabs.setMinimumSize(QSize(325, 0))
        self.demoViewTabs.setMaximumSize(QSize(16777215, 16777215))
        self.demoViewTabs.setBaseSize(QSize(350, 0))
        self.demoViewTabs.setFont(font2)
        self.demoViewTabs.setTabPosition(QTabWidget.North)
        self.demoViewTabs.setTabShape(QTabWidget.Rounded)
        self.demoViewTabs.setElideMode(Qt.ElideLeft)
        self.demoStepsTab = QWidget()
        self.demoStepsTab.setObjectName(u"demoStepsTab")
        self.demoStepsTab.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.demoStepsTab.sizePolicy().hasHeightForWidth())
        self.demoStepsTab.setSizePolicy(sizePolicy8)
        self.verticalLayout_26 = QVBoxLayout(self.demoStepsTab)
        self.verticalLayout_26.setSpacing(2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(4, 2, 4, 2)
        self.demoStepsTopBtns = QHBoxLayout()
        self.demoStepsTopBtns.setSpacing(4)
        self.demoStepsTopBtns.setObjectName(u"demoStepsTopBtns")
        self.demoStepsTopBtns.setContentsMargins(0, -1, 0, -1)
        self.demoStepsLabel = QLabel(self.demoStepsTab)
        self.demoStepsLabel.setObjectName(u"demoStepsLabel")
        self.demoStepsLabel.setEnabled(True)

        self.demoStepsTopBtns.addWidget(self.demoStepsLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.demoStepsTopBtns.addItem(self.horizontalSpacer_5)

        self.addDemoStepBtn = QPushButton(self.demoStepsTab)
        self.addDemoStepBtn.setObjectName(u"addDemoStepBtn")
        self.addDemoStepBtn.setEnabled(True)

        self.demoStepsTopBtns.addWidget(self.addDemoStepBtn)

        self.delDemoStepBtn = QPushButton(self.demoStepsTab)
        self.delDemoStepBtn.setObjectName(u"delDemoStepBtn")

        self.demoStepsTopBtns.addWidget(self.delDemoStepBtn)

        self.demoStepsOptionsBtn = QToolButton(self.demoStepsTab)
        self.demoStepsOptionsBtn.setObjectName(u"demoStepsOptionsBtn")

        self.demoStepsTopBtns.addWidget(self.demoStepsOptionsBtn)


        self.verticalLayout_26.addLayout(self.demoStepsTopBtns)

        self.demoStepsTree = QTreeWidget(self.demoStepsTab)
        self.demoStepsTree.setObjectName(u"demoStepsTree")
        self.demoStepsTree.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.demoStepsTree.sizePolicy().hasHeightForWidth())
        self.demoStepsTree.setSizePolicy(sizePolicy1)

        self.verticalLayout_26.addWidget(self.demoStepsTree)

        self.demoStepsBtns = QHBoxLayout()
        self.demoStepsBtns.setSpacing(0)
        self.demoStepsBtns.setObjectName(u"demoStepsBtns")
        self.pushButton_3 = QPushButton(self.demoStepsTab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.demoStepsBtns.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.demoStepsTab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.demoStepsBtns.addWidget(self.pushButton_4)

        self.pushButton_8 = QPushButton(self.demoStepsTab)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.demoStepsBtns.addWidget(self.pushButton_8)

        self.dupeDemoStepBtn = QPushButton(self.demoStepsTab)
        self.dupeDemoStepBtn.setObjectName(u"dupeDemoStepBtn")

        self.demoStepsBtns.addWidget(self.dupeDemoStepBtn)

        self.demoStepsMiscBtn = QToolButton(self.demoStepsTab)
        self.demoStepsMiscBtn.setObjectName(u"demoStepsMiscBtn")

        self.demoStepsBtns.addWidget(self.demoStepsMiscBtn)


        self.verticalLayout_26.addLayout(self.demoStepsBtns)

        self.demoViewTabs.addTab(self.demoStepsTab, "")
        self.demoMetadataTab = QWidget()
        self.demoMetadataTab.setObjectName(u"demoMetadataTab")
        self.verticalLayout_4 = QVBoxLayout(self.demoMetadataTab)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 2, 4, 2)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.demoMetadataTab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.demoMetadataTab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.treeView = QTreeView(self.demoMetadataTab)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_4.addWidget(self.treeView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_6 = QPushButton(self.demoMetadataTab)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.demoMetadataTab)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.toolButton_2 = QToolButton(self.demoMetadataTab)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_2.setAutoRaise(False)

        self.horizontalLayout_5.addWidget(self.toolButton_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.demoViewTabs.addTab(self.demoMetadataTab, "")
        self.splitter_2.addWidget(self.demoViewTabs)
        self.propTabs = QTabWidget(self.splitter_2)
        self.propTabs.setObjectName(u"propTabs")
        sizePolicy4.setHeightForWidth(self.propTabs.sizePolicy().hasHeightForWidth())
        self.propTabs.setSizePolicy(sizePolicy4)
        self.propTabs.setMinimumSize(QSize(325, 0))
        self.propTabs.setMaximumSize(QSize(234243, 16777215))
        self.propTabs.setFont(font2)
        self.propsTab = QWidget()
        self.propsTab.setObjectName(u"propsTab")
        self.verticalLayout_5 = QVBoxLayout(self.propsTab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.propStack = QStackedWidget(self.propsTab)
        self.propStack.setObjectName(u"propStack")
        self.propStack.setAutoFillBackground(False)
        self.propStack.setLineWidth(0)
        self.stepStackPage = QWidget()
        self.stepStackPage.setObjectName(u"stepStackPage")
        self.verticalLayout_8 = QVBoxLayout(self.stepStackPage)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 2, 4, 2)
        self.stepPageTopBtns = QHBoxLayout()
        self.stepPageTopBtns.setSpacing(4)
        self.stepPageTopBtns.setObjectName(u"stepPageTopBtns")
        self.stepPageTopBtns.setContentsMargins(0, -1, 0, -1)
        self.stepPageLabel = QLabel(self.stepStackPage)
        self.stepPageLabel.setObjectName(u"stepPageLabel")

        self.stepPageTopBtns.addWidget(self.stepPageLabel)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.stepPageTopBtns.addItem(self.horizontalSpacer_10)

        self.stepPageOptionsBtn = QToolButton(self.stepStackPage)
        self.stepPageOptionsBtn.setObjectName(u"stepPageOptionsBtn")

        self.stepPageTopBtns.addWidget(self.stepPageOptionsBtn)


        self.verticalLayout_8.addLayout(self.stepPageTopBtns)

        self.stepPageTable = QTableWidget(self.stepStackPage)
        if (self.stepPageTable.columnCount() < 6):
            self.stepPageTable.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.stepPageTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.stepPageTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.stepPageTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.stepPageTable.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.stepPageTable.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.stepPageTable.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.stepPageTable.setObjectName(u"stepPageTable")

        self.verticalLayout_8.addWidget(self.stepPageTable)

        self.stepPageBtns = QHBoxLayout()
        self.stepPageBtns.setObjectName(u"stepPageBtns")
        self.stepPageResetBtn = QPushButton(self.stepStackPage)
        self.stepPageResetBtn.setObjectName(u"stepPageResetBtn")

        self.stepPageBtns.addWidget(self.stepPageResetBtn)

        self.stepPageInfoBtn = QPushButton(self.stepStackPage)
        self.stepPageInfoBtn.setObjectName(u"stepPageInfoBtn")

        self.stepPageBtns.addWidget(self.stepPageInfoBtn)


        self.verticalLayout_8.addLayout(self.stepPageBtns)

        self.propStack.addWidget(self.stepStackPage)
        self.sectStackPage = QWidget()
        self.sectStackPage.setObjectName(u"sectStackPage")
        self.verticalLayout_3 = QVBoxLayout(self.sectStackPage)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 2, 4, 2)
        self.sectPageTopBtns = QHBoxLayout()
        self.sectPageTopBtns.setSpacing(4)
        self.sectPageTopBtns.setObjectName(u"sectPageTopBtns")
        self.label_5 = QLabel(self.sectStackPage)
        self.label_5.setObjectName(u"label_5")

        self.sectPageTopBtns.addWidget(self.label_5)

        self.sectPageLabel = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.sectPageTopBtns.addItem(self.sectPageLabel)

        self.sectPageOptionsBtn = QToolButton(self.sectStackPage)
        self.sectPageOptionsBtn.setObjectName(u"sectPageOptionsBtn")

        self.sectPageTopBtns.addWidget(self.sectPageOptionsBtn)


        self.verticalLayout_3.addLayout(self.sectPageTopBtns)

        self.sectInfoTable = QTableWidget(self.sectStackPage)
        if (self.sectInfoTable.rowCount() < 3):
            self.sectInfoTable.setRowCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.sectInfoTable.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.sectInfoTable.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.sectInfoTable.setVerticalHeaderItem(2, __qtablewidgetitem14)
        self.sectInfoTable.setObjectName(u"sectInfoTable")

        self.verticalLayout_3.addWidget(self.sectInfoTable)

        self.sectPageBtns = QHBoxLayout()
        self.sectPageBtns.setSpacing(0)
        self.sectPageBtns.setObjectName(u"sectPageBtns")
        self.sectPageResetBtn = QPushButton(self.sectStackPage)
        self.sectPageResetBtn.setObjectName(u"sectPageResetBtn")

        self.sectPageBtns.addWidget(self.sectPageResetBtn)

        self.sectPageInfoBtn = QPushButton(self.sectStackPage)
        self.sectPageInfoBtn.setObjectName(u"sectPageInfoBtn")

        self.sectPageBtns.addWidget(self.sectPageInfoBtn)

        self.toolButton_4 = QToolButton(self.sectStackPage)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.sectPageBtns.addWidget(self.toolButton_4)


        self.verticalLayout_3.addLayout(self.sectPageBtns)

        self.propStack.addWidget(self.sectStackPage)

        self.verticalLayout_5.addWidget(self.propStack)

        self.propTabs.addTab(self.propsTab, "")
        self.previewTab = QWidget()
        self.previewTab.setObjectName(u"previewTab")
        self.verticalLayout_25 = QVBoxLayout(self.previewTab)
        self.verticalLayout_25.setSpacing(2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(4, 2, 4, 2)
        self.graphicsView = QGraphicsView(self.previewTab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_25.addWidget(self.graphicsView)

        self.propTabs.addTab(self.previewTab, "")
        self.splitter_2.addWidget(self.propTabs)
        self.splitter_3.addWidget(self.splitter_2)

        self.horizontalLayout_6.addWidget(self.splitter_3)

        self.centralTabs.addWidget(self.jobsPage)
        self.rawEditor = QWidget()
        self.rawEditor.setObjectName(u"rawEditor")
        self.horizontalLayout_2 = QHBoxLayout(self.rawEditor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.centralTabs.addWidget(self.rawEditor)

        self.verticalLayout.addWidget(self.centralTabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(0, 20))
        self.statusbar.setMaximumSize(QSize(16777215, 25))
        self.statusbar.setLayoutDirection(Qt.RightToLeft)
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1240, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuNew = QMenu(self.menuFile)
        self.menuNew.setObjectName(u"menuNew")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuDemo = QMenu(self.menubar)
        self.menuDemo.setObjectName(u"menuDemo")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setToolTipsVisible(True)
        self.menuTasks = QMenu(self.menubar)
        self.menuTasks.setObjectName(u"menuTasks")
        self.menuTasks.setTearOffEnabled(False)
        self.menuTasks.setSeparatorsCollapsible(True)
        self.menuTasks.setToolTipsVisible(True)
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuDemo.menuAction())
        self.menubar.addAction(self.menuTasks.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Jobs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Demo)
        self.menuFile.addAction(self.actionOpen_Audio)
        self.menuFile.addAction(self.actionOpen_Script)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menuNew.addAction(self.actionStep)
        self.menuNew.addAction(self.actionQueue)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuView.addAction(self.actionJobs_Editor)
        self.menuView.addAction(self.actionXML_Editor)
        self.menuView.addAction(self.actionScript_Editor)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFull_Screen)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionMenubar)
        self.menuView.addAction(self.actionStatusbar)
        self.menuDemo.addAction(self.actionNew)
        self.menuDemo.addAction(self.actionOpen)
        self.menuDemo.addAction(self.actionSave_current_state)
        self.menuDemo.addAction(self.actionReset_changes)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTasks.addAction(self.actionRun)
        self.menuTasks.addAction(self.actionClear_jobs)
        self.menuTasks.addSeparator()
        self.menuTasks.addAction(self.actionDelete_current_task)
        self.menuTasks.addAction(self.actionDuplicate_current_task)
        self.menuTasks.addAction(self.actionReset_current_task)
        self.menuTasks.addAction(self.actionRun_current_task)

        self.retranslateUi(MainWindow)
        self.menubar.objectNameChanged.connect(self.statusbar.showMessage)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.browseDemoBtn.clicked.connect(self.browseDemoBtn.showMenu)
        self.taskStepsTable.cellClicked.connect(self.opsTabs.setCurrentIndex)
        self.opsTabs.tabCloseRequested.connect(self.taskStepsTable.removeRow)
        self.opsTabs.currentChanged.connect(self.taskStepsTable.selectRow)

        self.centralTabs.setCurrentIndex(1)
        self.dataLoadTabs.setCurrentIndex(0)
        self.browseDemoBtn.setDefault(True)
        self.demoRecentBtn.setDefault(False)
        self.browseScriptBtn.setDefault(True)
        self.taskTabs.setCurrentIndex(1)
        self.addStepBtn.setDefault(True)
        self.runStepsBtn.setDefault(True)
        self.demoViewTabs.setCurrentIndex(0)
        self.propTabs.setCurrentIndex(0)
        self.propStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Impresys Demo Utilities", None))
        self.actionStep.setText(QCoreApplication.translate("MainWindow", u"Step", None))
#if QT_CONFIG(shortcut)
        self.actionStep.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S, Return", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Demo.setText(QCoreApplication.translate("MainWindow", u"Open Demo", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Demo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Audio.setText(QCoreApplication.translate("MainWindow", u"Open Audio", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Audio.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Script.setText(QCoreApplication.translate("MainWindow", u"Open Script", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Script.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Jobs.setText(QCoreApplication.translate("MainWindow", u"Save Job List", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Jobs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
#if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionQueue.setText(QCoreApplication.translate("MainWindow", u"Queue", None))
        self.actionJobs_Editor.setText(QCoreApplication.translate("MainWindow", u"Jobs Editor", None))
        self.actionXML_Editor.setText(QCoreApplication.translate("MainWindow", u"XML Editor", None))
        self.actionScript_Editor.setText(QCoreApplication.translate("MainWindow", u"Script Editor", None))
        self.actionFull_Screen.setText(QCoreApplication.translate("MainWindow", u"Full Screen", None))
#if QT_CONFIG(shortcut)
        self.actionFull_Screen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run all tasks", None))
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear_jobs.setText(QCoreApplication.translate("MainWindow", u"Clear all tasks", None))
#if QT_CONFIG(shortcut)
        self.actionClear_jobs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete_current_task.setText(QCoreApplication.translate("MainWindow", u"Delete current task", None))
        self.actionDuplicate_current_task.setText(QCoreApplication.translate("MainWindow", u"Duplicate current task", None))
        self.actionReset_current_task.setText(QCoreApplication.translate("MainWindow", u"Reset current task", None))
        self.actionMenubar.setText(QCoreApplication.translate("MainWindow", u"Menubar", None))
#if QT_CONFIG(shortcut)
        self.actionMenubar.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionStatusbar.setText(QCoreApplication.translate("MainWindow", u"Statusbar", None))
#if QT_CONFIG(shortcut)
        self.actionStatusbar.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun_current_task.setText(QCoreApplication.translate("MainWindow", u"Run current task", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave_current_state.setText(QCoreApplication.translate("MainWindow", u"Save current state", None))
        self.actionReset_changes.setText(QCoreApplication.translate("MainWindow", u"Reset changes", None))
#if QT_CONFIG(statustip)
        self.dataLoadTabs.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.demoLoadedTab.setStatusTip(QCoreApplication.translate("MainWindow", u"Currently loaded demos available to edit", None))
#endif // QT_CONFIG(statustip)
        self.demoLoadedLabel.setText(QCoreApplication.translate("MainWindow", u"Demo Files", None))
#if QT_CONFIG(statustip)
        self.browseDemoBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Browse for .demo file", None))
#endif // QT_CONFIG(statustip)
        self.browseDemoBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        ___qtablewidgetitem = self.demoLoadedTree.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtablewidgetitem1 = self.demoLoadedTree.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.demoLoadedTree.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Links", None));
        self.demoRecentBtn.setText(QCoreApplication.translate("MainWindow", u"Recent", None))
        self.demoSavedBtn.setText(QCoreApplication.translate("MainWindow", u"Saved", None))
        self.demoRemoveBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.demoLoadBtn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.demoEtcBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.dataLoadTabs.setTabText(self.dataLoadTabs.indexOf(self.demoLoadedTab), QCoreApplication.translate("MainWindow", u"Demo", None))
#if QT_CONFIG(statustip)
        self.audioLoadedTab.setStatusTip(QCoreApplication.translate("MainWindow", u"Currently loaded audio folders available to attach to demo files", None))
#endif // QT_CONFIG(statustip)
        self.audioLoadedLabel.setText(QCoreApplication.translate("MainWindow", u"Audio Folders", None))
        self.browseAudioBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        ___qtreewidgetitem = self.audioLoadedTree.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Step Count", None));
        self.audioRecentBtn.setText(QCoreApplication.translate("MainWindow", u"Recent", None))
        self.audioSavedBtn.setText(QCoreApplication.translate("MainWindow", u"Saved", None))
        self.audioLoadBtn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.audioRemoveBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.audioEtcBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.dataLoadTabs.setTabText(self.dataLoadTabs.indexOf(self.audioLoadedTab), QCoreApplication.translate("MainWindow", u"Audio", None))
        self.scriptsLoadedLabel.setText(QCoreApplication.translate("MainWindow", u"Script Files", None))
        self.browseScriptBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
#if QT_CONFIG(statustip)
        self.scriptRecentsBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Browse recent demo files", None))
#endif // QT_CONFIG(statustip)
        self.scriptRecentsBtn.setText(QCoreApplication.translate("MainWindow", u"Recents", None))
#if QT_CONFIG(statustip)
        self.scriptsSavedBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Browse bookmarked demo files", None))
#endif // QT_CONFIG(statustip)
        self.scriptsSavedBtn.setText(QCoreApplication.translate("MainWindow", u"Saved", None))
#if QT_CONFIG(statustip)
        self.scriptRemoveBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Remove selected demo file", None))
#endif // QT_CONFIG(statustip)
        self.scriptRemoveBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
#if QT_CONFIG(statustip)
        self.scriptLoadBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Load a new .demo file", None))
#endif // QT_CONFIG(statustip)
        self.scriptLoadBtn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.scriptsEtcBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.dataLoadTabs.setTabText(self.dataLoadTabs.indexOf(self.scriptsLoadedTab), QCoreApplication.translate("MainWindow", u"Script", None))
#if QT_CONFIG(statustip)
        self.taskTabs.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.taskStepsTitle.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.stepTargetCombo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Demo", None))
#if QT_CONFIG(statustip)
        self.addStepBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Add a new step to the task queue", None))
#endif // QT_CONFIG(statustip)
        self.addStepBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(shortcut)
        self.addStepBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem3 = self.taskStepsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Task", None));
        ___qtablewidgetitem4 = self.taskStepsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Demo", None));
        ___qtablewidgetitem5 = self.taskStepsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Steps", None));
#if QT_CONFIG(statustip)
        self.taskStepsTable.setStatusTip(QCoreApplication.translate("MainWindow", u"Currently queued tasks to run", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.stepUpBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Move currently selected step up in queue", None))
#endif // QT_CONFIG(statustip)
        self.stepUpBtn.setText(QCoreApplication.translate("MainWindow", u"Up", None))
#if QT_CONFIG(statustip)
        self.stepDownBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Move selected step down in queue", None))
#endif // QT_CONFIG(statustip)
        self.stepDownBtn.setText(QCoreApplication.translate("MainWindow", u"Down", None))
#if QT_CONFIG(statustip)
        self.deleteStepBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete selected step", None))
#endif // QT_CONFIG(statustip)
        self.deleteStepBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(statustip)
        self.copyStepBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Duplicate selected step", None))
#endif // QT_CONFIG(statustip)
        self.copyStepBtn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(statustip)
        self.runStepsBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Execute all steps in task queue", None))
#endif // QT_CONFIG(statustip)
        self.runStepsBtn.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(shortcut)
        self.runStepsBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.etcStepsBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"More queue options", None))
#endif // QT_CONFIG(statustip)
        self.etcStepsBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.taskTabs.setTabText(self.taskTabs.indexOf(self.taskStepsTab), QCoreApplication.translate("MainWindow", u"Steps", None))
        self.taskHistoryLabel.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.taskHistoryCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Demo", None))
        self.taskHistoryCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Audio", None))
        self.taskHistoryCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Script", None))

        self.browseTaskHistoryBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.taskHistoryLoadBtn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.taskHistorySaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.taskHistoryEditBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.taskHistoryRemoveBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.taskHistoryEtcBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.taskTabs.setTabText(self.taskTabs.indexOf(self.taskHistoryTab), QCoreApplication.translate("MainWindow", u"History", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Undo History", None))
        self.toolButton_16.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.taskTabs.setTabText(self.taskTabs.indexOf(self.taskUndoTab), QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(statustip)
        self.demoViewTabs.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.demoStepsLabel.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
#if QT_CONFIG(statustip)
        self.addDemoStepBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Add a new step/section to the demo file", None))
#endif // QT_CONFIG(statustip)
        self.addDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(statustip)
        self.delDemoStepBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Remove selected step(s) to the demo file", None))
#endif // QT_CONFIG(statustip)
        self.delDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.demoStepsOptionsBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtreewidgetitem1 = self.demoStepsTree.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Image", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Audio", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"TItle", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Index", None));
#if QT_CONFIG(statustip)
        self.demoStepsTree.setStatusTip(QCoreApplication.translate("MainWindow", u"Selectable and modifiable step listing for selected demo", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(statustip)
        self.dupeDemoStepBtn.setStatusTip(QCoreApplication.translate("MainWindow", u"Duplicate selected step or section", None))
#endif // QT_CONFIG(statustip)
        self.dupeDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.demoStepsMiscBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.demoViewTabs.setTabText(self.demoViewTabs.indexOf(self.demoStepsTab), QCoreApplication.translate("MainWindow", u"Demo Steps", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.demoViewTabs.setTabText(self.demoViewTabs.indexOf(self.demoMetadataTab), QCoreApplication.translate("MainWindow", u"Metadata", None))
#if QT_CONFIG(tooltip)
        self.propTabs.setToolTip(QCoreApplication.translate("MainWindow", u"Properties of selected step(s) or section(s)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.propTabs.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.propTabs.setWhatsThis(QCoreApplication.translate("MainWindow", u"Currently selected section/step properties", None))
#endif // QT_CONFIG(whatsthis)
        self.stepPageLabel.setText(QCoreApplication.translate("MainWindow", u"Step Info", None))
        self.stepPageOptionsBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtablewidgetitem6 = self.stepPageTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Step index", None));
        ___qtablewidgetitem7 = self.stepPageTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Section index", None));
        ___qtablewidgetitem8 = self.stepPageTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"TP", None));
        ___qtablewidgetitem9 = self.stepPageTable.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"CI", None));
        ___qtablewidgetitem10 = self.stepPageTable.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        ___qtablewidgetitem11 = self.stepPageTable.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Hover", None));
#if QT_CONFIG(statustip)
        self.stepPageTable.setStatusTip(QCoreApplication.translate("MainWindow", u"Properties of selected step(s) or section(s)", None))
#endif // QT_CONFIG(statustip)
        self.stepPageResetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.stepPageInfoBtn.setText(QCoreApplication.translate("MainWindow", u"More Info", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Section Info", None))
        self.sectPageOptionsBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtablewidgetitem12 = self.sectInfoTable.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem13 = self.sectInfoTable.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem14 = self.sectInfoTable.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Audio", None));
        self.sectPageResetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.sectPageInfoBtn.setText(QCoreApplication.translate("MainWindow", u"More Info", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.propTabs.setTabText(self.propTabs.indexOf(self.propsTab), QCoreApplication.translate("MainWindow", u"Properties", None))
        self.propTabs.setTabText(self.propTabs.indexOf(self.previewTab), QCoreApplication.translate("MainWindow", u"Preview", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuDemo.setTitle(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTasks.setTitle(QCoreApplication.translate("MainWindow", u"Tasks", None))
    # retranslateUi

