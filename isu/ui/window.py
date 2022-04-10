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
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QToolButton, QTreeWidget, QTreeWidgetItem, QUndoView,
    QVBoxLayout, QWidget)

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
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.dataLayout = QVBoxLayout()
        self.dataLayout.setSpacing(4)
        self.dataLayout.setObjectName(u"dataLayout")
        self.dataLayout.setContentsMargins(0, 0, 0, 0)
        self.tasksTabs = QTabWidget(self.jobsPage)
        self.tasksTabs.setObjectName(u"tasksTabs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tasksTabs.sizePolicy().hasHeightForWidth())
        self.tasksTabs.setSizePolicy(sizePolicy1)
        self.tasksTabs.setMinimumSize(QSize(350, 0))
        self.tasksTabs.setMaximumSize(QSize(324234, 16777215))
        self.tasksTabs.setTabPosition(QTabWidget.North)
        self.dataLoadedTab = QWidget()
        self.dataLoadedTab.setObjectName(u"dataLoadedTab")
        self.dataLoadedTab.setMaximumSize(QSize(16777214, 16777215))
        self.verticalLayout_34 = QVBoxLayout(self.dataLoadedTab)
        self.verticalLayout_34.setSpacing(4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label = QLabel(self.dataLoadedTab)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setIndent(0)

        self.horizontalLayout_23.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_2)

        self.browseButton = QPushButton(self.dataLoadedTab)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setKerning(True)
        self.browseButton.setFont(font2)
        self.browseButton.setAutoDefault(True)

        self.horizontalLayout_23.addWidget(self.browseButton)


        self.verticalLayout_34.addLayout(self.horizontalLayout_23)

        self.loadedDataTree = QTableWidget(self.dataLoadedTab)
        if (self.loadedDataTree.columnCount() < 3):
            self.loadedDataTree.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.loadedDataTree.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.loadedDataTree.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.loadedDataTree.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.loadedDataTree.setObjectName(u"loadedDataTree")
        self.loadedDataTree.setMinimumSize(QSize(350, 0))

        self.verticalLayout_34.addWidget(self.loadedDataTree)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.browseDemoBtn = QPushButton(self.dataLoadedTab)
        self.browseDemoBtn.setObjectName(u"browseDemoBtn")
        self.browseDemoBtn.setAutoDefault(False)
        self.browseDemoBtn.setFlat(False)

        self.horizontalLayout_19.addWidget(self.browseDemoBtn)

        self.browseAudioBtn = QPushButton(self.dataLoadedTab)
        self.browseAudioBtn.setObjectName(u"browseAudioBtn")

        self.horizontalLayout_19.addWidget(self.browseAudioBtn)

        self.browseScriptBtn = QPushButton(self.dataLoadedTab)
        self.browseScriptBtn.setObjectName(u"browseScriptBtn")

        self.horizontalLayout_19.addWidget(self.browseScriptBtn)

        self.toolButton_12 = QToolButton(self.dataLoadedTab)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_12.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.toolButton_12.setAutoRaise(False)
        self.toolButton_12.setArrowType(Qt.DownArrow)

        self.horizontalLayout_19.addWidget(self.toolButton_12)


        self.verticalLayout_34.addLayout(self.horizontalLayout_19)

        self.tasksTabs.addTab(self.dataLoadedTab, "")
        self.dataPrestTab = QWidget()
        self.dataPrestTab.setObjectName(u"dataPrestTab")
        self.verticalLayout_36 = QVBoxLayout(self.dataPrestTab)
        self.verticalLayout_36.setSpacing(4)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_7 = QLabel(self.dataPrestTab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_30.addWidget(self.label_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_7)

        self.comboBox = QComboBox(self.dataPrestTab)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_30.addWidget(self.comboBox)

        self.pushButton_54 = QPushButton(self.dataPrestTab)
        self.pushButton_54.setObjectName(u"pushButton_54")

        self.horizontalLayout_30.addWidget(self.pushButton_54)


        self.verticalLayout_36.addLayout(self.horizontalLayout_30)

        self.dataTree = QTreeWidget(self.dataPrestTab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Name");
        self.dataTree.setHeaderItem(__qtreewidgetitem)
        self.dataTree.setObjectName(u"dataTree")

        self.verticalLayout_36.addWidget(self.dataTree)

        self.widget_7 = QWidget(self.dataPrestTab)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_29 = QVBoxLayout(self.widget_7)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.demoLoadBtn = QPushButton(self.widget_7)
        self.demoLoadBtn.setObjectName(u"demoLoadBtn")

        self.horizontalLayout_21.addWidget(self.demoLoadBtn)

        self.pushButton_50 = QPushButton(self.widget_7)
        self.pushButton_50.setObjectName(u"pushButton_50")

        self.horizontalLayout_21.addWidget(self.pushButton_50)

        self.pushButton_51 = QPushButton(self.widget_7)
        self.pushButton_51.setObjectName(u"pushButton_51")

        self.horizontalLayout_21.addWidget(self.pushButton_51)

        self.pushButton_52 = QPushButton(self.widget_7)
        self.pushButton_52.setObjectName(u"pushButton_52")

        self.horizontalLayout_21.addWidget(self.pushButton_52)

        self.toolButton_13 = QToolButton(self.widget_7)
        self.toolButton_13.setObjectName(u"toolButton_13")

        self.horizontalLayout_21.addWidget(self.toolButton_13)


        self.verticalLayout_29.addLayout(self.horizontalLayout_21)


        self.verticalLayout_36.addWidget(self.widget_7)

        self.tasksTabs.addTab(self.dataPrestTab, "")
        self.dataSavedTab = QWidget()
        self.dataSavedTab.setObjectName(u"dataSavedTab")
        self.verticalLayout_21 = QVBoxLayout(self.dataSavedTab)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_6 = QWidget(self.dataSavedTab)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_24 = QVBoxLayout(self.widget_6)
        self.verticalLayout_24.setSpacing(4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_25.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_3)

        self.toolButton_15 = QToolButton(self.widget_6)
        self.toolButton_15.setObjectName(u"toolButton_15")

        self.horizontalLayout_25.addWidget(self.toolButton_15)


        self.verticalLayout_24.addLayout(self.horizontalLayout_25)

        self.tableView = QTableView(self.widget_6)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_24.addWidget(self.tableView)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.verticalLayout_24.addLayout(self.horizontalLayout_26)


        self.verticalLayout_21.addWidget(self.widget_6)

        self.tasksTabs.addTab(self.dataSavedTab, "")

        self.dataLayout.addWidget(self.tasksTabs)

        self.tasksTabs_2 = QTabWidget(self.jobsPage)
        self.tasksTabs_2.setObjectName(u"tasksTabs_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tasksTabs_2.sizePolicy().hasHeightForWidth())
        self.tasksTabs_2.setSizePolicy(sizePolicy2)
        self.tasksTabs_2.setMinimumSize(QSize(350, 0))
        self.tasksTabs_2.setMaximumSize(QSize(23434, 16777215))
        self.tasksTabs_2.setCursor(QCursor(Qt.ArrowCursor))
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.verticalLayout_30 = QVBoxLayout(self.tab_11)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_11 = QLabel(self.tab_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setIndent(8)

        self.horizontalLayout_35.addWidget(self.label_11)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_11)

        self.addStepButton = QPushButton(self.tab_11)
        self.addStepButton.setObjectName(u"addStepButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.addStepButton.sizePolicy().hasHeightForWidth())
        self.addStepButton.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setKerning(False)
        self.addStepButton.setFont(font3)
        self.addStepButton.setCursor(QCursor(Qt.ArrowCursor))
        self.addStepButton.setContextMenuPolicy(Qt.PreventContextMenu)
        self.addStepButton.setAcceptDrops(False)
        self.addStepButton.setAutoFillBackground(False)
        self.addStepButton.setIconSize(QSize(16, 16))
        self.addStepButton.setAutoDefault(True)
        self.addStepButton.setFlat(False)

        self.horizontalLayout_35.addWidget(self.addStepButton)


        self.verticalLayout_30.addLayout(self.horizontalLayout_35)

        self.stepsTable = QTableWidget(self.tab_11)
        if (self.stepsTable.columnCount() < 3):
            self.stepsTable.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.stepsTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.stepsTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.stepsTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.stepsTable.setObjectName(u"stepsTable")
        self.stepsTable.setFrameShape(QFrame.StyledPanel)
        self.stepsTable.setFrameShadow(QFrame.Sunken)
        self.stepsTable.setLineWidth(0)
        self.stepsTable.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.stepsTable.setTabKeyNavigation(True)
        self.stepsTable.setDragEnabled(True)
        self.stepsTable.setDragDropOverwriteMode(False)
        self.stepsTable.setDragDropMode(QAbstractItemView.DragDrop)
        self.stepsTable.setDefaultDropAction(Qt.MoveAction)
        self.stepsTable.setAlternatingRowColors(True)
        self.stepsTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_30.addWidget(self.stepsTable)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_5 = QPushButton(self.tab_11)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_7 = QPushButton(self.tab_11)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.tab_11)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.runButton = QPushButton(self.tab_11)
        self.runButton.setObjectName(u"runButton")
        self.runButton.setAutoFillBackground(False)
        self.runButton.setAutoDefault(True)

        self.horizontalLayout_5.addWidget(self.runButton)

        self.toolButton_2 = QToolButton(self.tab_11)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setPopupMode(QToolButton.MenuButtonPopup)
        self.toolButton_2.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.toolButton_2.setArrowType(Qt.NoArrow)

        self.horizontalLayout_5.addWidget(self.toolButton_2)


        self.verticalLayout_30.addLayout(self.horizontalLayout_5)

        self.tasksTabs_2.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_37 = QVBoxLayout(self.tab_12)
        self.verticalLayout_37.setSpacing(5)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_8 = QLabel(self.tab_12)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_31.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_8)

        self.comboBox_4 = QComboBox(self.tab_12)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_31.addWidget(self.comboBox_4)

        self.pushButton_55 = QPushButton(self.tab_12)
        self.pushButton_55.setObjectName(u"pushButton_55")

        self.horizontalLayout_31.addWidget(self.pushButton_55)


        self.verticalLayout_37.addLayout(self.horizontalLayout_31)

        self.tableView_2 = QTableView(self.tab_12)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_37.addWidget(self.tableView_2)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_45 = QPushButton(self.tab_12)
        self.pushButton_45.setObjectName(u"pushButton_45")

        self.horizontalLayout_20.addWidget(self.pushButton_45)

        self.pushButton_46 = QPushButton(self.tab_12)
        self.pushButton_46.setObjectName(u"pushButton_46")

        self.horizontalLayout_20.addWidget(self.pushButton_46)

        self.pushButton_48 = QPushButton(self.tab_12)
        self.pushButton_48.setObjectName(u"pushButton_48")

        self.horizontalLayout_20.addWidget(self.pushButton_48)

        self.pushButton_47 = QPushButton(self.tab_12)
        self.pushButton_47.setObjectName(u"pushButton_47")

        self.horizontalLayout_20.addWidget(self.pushButton_47)

        self.toolButton_14 = QToolButton(self.tab_12)
        self.toolButton_14.setObjectName(u"toolButton_14")

        self.horizontalLayout_20.addWidget(self.toolButton_14)


        self.verticalLayout_37.addLayout(self.horizontalLayout_20)

        self.tasksTabs_2.addTab(self.tab_12, "")
        self.tasksUndoTab = QWidget()
        self.tasksUndoTab.setObjectName(u"tasksUndoTab")
        self.tasksUndoTab.setMaximumSize(QSize(16777213, 16777215))
        self.tasksUndoTab.setFont(font2)
        self.verticalLayout_22 = QVBoxLayout(self.tasksUndoTab)
        self.verticalLayout_22.setSpacing(4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_4 = QLabel(self.tasksUndoTab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_24.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_4)

        self.toolButton_16 = QToolButton(self.tasksUndoTab)
        self.toolButton_16.setObjectName(u"toolButton_16")

        self.horizontalLayout_24.addWidget(self.toolButton_16)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)

        self.undoView = QUndoView(self.tasksUndoTab)
        self.undoView.setObjectName(u"undoView")
        self.undoView.setEnabled(True)

        self.verticalLayout_22.addWidget(self.undoView)

        self.tasksTabs_2.addTab(self.tasksUndoTab, "")

        self.dataLayout.addWidget(self.tasksTabs_2)


        self.horizontalLayout_6.addLayout(self.dataLayout)

        self.opsLayout = QWidget(self.jobsPage)
        self.opsLayout.setObjectName(u"opsLayout")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.opsLayout.sizePolicy().hasHeightForWidth())
        self.opsLayout.setSizePolicy(sizePolicy4)
        self.opsLayout.setMaximumSize(QSize(16777215, 16777212))
        self.opsLayout.setFocusPolicy(Qt.NoFocus)
        self.opsLayout.setLayoutDirection(Qt.LeftToRight)
        self.opsLayout.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.opsLayout)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.opsTabs = QTabWidget(self.opsLayout)
        self.opsTabs.setObjectName(u"opsTabs")
        self.opsTabs.setEnabled(False)
        self.opsTabs.setTabsClosable(True)
        self.opsTabs.setMovable(True)

        self.verticalLayout_2.addWidget(self.opsTabs)


        self.horizontalLayout_6.addWidget(self.opsLayout)

        self.infoView = QFrame(self.jobsPage)
        self.infoView.setObjectName(u"infoView")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.infoView.sizePolicy().hasHeightForWidth())
        self.infoView.setSizePolicy(sizePolicy5)
        self.infoView.setMaximumSize(QSize(23525, 16777215))
        self.infoView.setFrameShape(QFrame.StyledPanel)
        self.infoView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.infoView)
        self.verticalLayout_23.setSpacing(4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.propertyTabs = QTabWidget(self.infoView)
        self.propertyTabs.setObjectName(u"propertyTabs")
        self.propertyTabs.setMinimumSize(QSize(350, 0))
        self.propertyTabs.setMaximumSize(QSize(234243, 16777215))
        self.propertyTabs.setFont(font2)
        self.stepPropsPage = QWidget()
        self.stepPropsPage.setObjectName(u"stepPropsPage")
        self.verticalLayout_5 = QVBoxLayout(self.stepPropsPage)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.propStack = QStackedWidget(self.stepPropsPage)
        self.propStack.setObjectName(u"propStack")
        self.propStack.setAutoFillBackground(False)
        self.propStack.setLineWidth(0)
        self.stepStackPage = QWidget()
        self.stepStackPage.setObjectName(u"stepStackPage")
        self.verticalLayout_8 = QVBoxLayout(self.stepStackPage)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_9 = QLabel(self.stepStackPage)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_32.addWidget(self.label_9)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_10)

        self.toolButton = QToolButton(self.stepStackPage)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_32.addWidget(self.toolButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_32)

        self.tableWidget = QTableWidget(self.stepStackPage)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_8.addWidget(self.tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.stepStackPage)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.stepStackPage)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.propStack.addWidget(self.stepStackPage)
        self.sectStackPage = QWidget()
        self.sectStackPage.setObjectName(u"sectStackPage")
        self.verticalLayout_3 = QVBoxLayout(self.sectStackPage)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_5 = QLabel(self.sectStackPage)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_29.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_6)

        self.toolButton_3 = QToolButton(self.sectStackPage)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_29.addWidget(self.toolButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_29)

        self.tableWidget_2 = QTableWidget(self.sectStackPage)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem14)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_3.addWidget(self.tableWidget_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_13 = QPushButton(self.sectStackPage)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_9.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.sectStackPage)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_9.addWidget(self.pushButton_14)

        self.toolButton_4 = QToolButton(self.sectStackPage)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.horizontalLayout_9.addWidget(self.toolButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.propStack.addWidget(self.sectStackPage)

        self.verticalLayout_5.addWidget(self.propStack)

        self.propertyTabs.addTab(self.stepPropsPage, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_25 = QVBoxLayout(self.tab_5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.graphicsView = QGraphicsView(self.tab_5)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_25.addWidget(self.graphicsView)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_38 = QPushButton(self.tab_5)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.horizontalLayout_17.addWidget(self.pushButton_38)

        self.pushButton_39 = QPushButton(self.tab_5)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.horizontalLayout_17.addWidget(self.pushButton_39)

        self.toolButton_10 = QToolButton(self.tab_5)
        self.toolButton_10.setObjectName(u"toolButton_10")

        self.horizontalLayout_17.addWidget(self.toolButton_10)


        self.verticalLayout_25.addLayout(self.horizontalLayout_17)

        self.propertyTabs.addTab(self.tab_5, "")

        self.verticalLayout_23.addWidget(self.propertyTabs)

        self.demoViewTabs = QTabWidget(self.infoView)
        self.demoViewTabs.setObjectName(u"demoViewTabs")
        self.demoViewTabs.setEnabled(True)
        self.demoViewTabs.setMinimumSize(QSize(350, 0))
        self.demoViewTabs.setMaximumSize(QSize(16777215, 16777215))
        self.demoViewTabs.setFont(font2)
        self.demoViewTabs.setTabPosition(QTabWidget.North)
        self.demoViewTabs.setTabShape(QTabWidget.Rounded)
        self.demoViewTabs.setElideMode(Qt.ElideLeft)
        self.demoOverviewGroupPage1 = QWidget()
        self.demoOverviewGroupPage1.setObjectName(u"demoOverviewGroupPage1")
        self.demoOverviewGroupPage1.setEnabled(True)
        self.verticalLayout_26 = QVBoxLayout(self.demoOverviewGroupPage1)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_5)

        self.label_6 = QLabel(self.demoOverviewGroupPage1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)

        self.horizontalLayout_28.addWidget(self.label_6)

        self.toolButton_5 = QToolButton(self.demoOverviewGroupPage1)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.horizontalLayout_28.addWidget(self.toolButton_5)


        self.verticalLayout_26.addLayout(self.horizontalLayout_28)

        self.infoDemoTree = QTreeWidget(self.demoOverviewGroupPage1)
        self.infoDemoTree.setObjectName(u"infoDemoTree")
        self.infoDemoTree.setEnabled(True)

        self.verticalLayout_26.addWidget(self.infoDemoTree)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.addDemoStepBtn = QPushButton(self.demoOverviewGroupPage1)
        self.addDemoStepBtn.setObjectName(u"addDemoStepBtn")
        self.addDemoStepBtn.setEnabled(True)

        self.horizontalLayout_18.addWidget(self.addDemoStepBtn)

        self.delDemoStepBtn = QPushButton(self.demoOverviewGroupPage1)
        self.delDemoStepBtn.setObjectName(u"delDemoStepBtn")

        self.horizontalLayout_18.addWidget(self.delDemoStepBtn)

        self.dupeDemoStepBtn = QPushButton(self.demoOverviewGroupPage1)
        self.dupeDemoStepBtn.setObjectName(u"dupeDemoStepBtn")

        self.horizontalLayout_18.addWidget(self.dupeDemoStepBtn)

        self.toolButton_11 = QToolButton(self.demoOverviewGroupPage1)
        self.toolButton_11.setObjectName(u"toolButton_11")

        self.horizontalLayout_18.addWidget(self.toolButton_11)


        self.verticalLayout_26.addLayout(self.horizontalLayout_18)

        self.demoViewTabs.addTab(self.demoOverviewGroupPage1, "")
        self.demoMetadataTab = QWidget()
        self.demoMetadataTab.setObjectName(u"demoMetadataTab")
        self.demoViewTabs.addTab(self.demoMetadataTab, "")

        self.verticalLayout_23.addWidget(self.demoViewTabs)


        self.horizontalLayout_6.addWidget(self.infoView)

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
        self.browseButton.clicked.connect(self.browseButton.showMenu)
        self.menubar.objectNameChanged.connect(self.statusbar.showMessage)
        self.actionQuit.triggered.connect(MainWindow.close)

        self.centralTabs.setCurrentIndex(1)
        self.tasksTabs.setCurrentIndex(0)
        self.browseButton.setDefault(True)
        self.browseDemoBtn.setDefault(False)
        self.tasksTabs_2.setCurrentIndex(0)
        self.addStepButton.setDefault(True)
        self.runButton.setDefault(True)
        self.propertyTabs.setCurrentIndex(0)
        self.propStack.setCurrentIndex(0)
        self.demoViewTabs.setCurrentIndex(0)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        ___qtablewidgetitem = self.loadedDataTree.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtablewidgetitem1 = self.loadedDataTree.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.loadedDataTree.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Links", None));
        self.browseDemoBtn.setText(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.browseAudioBtn.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.browseScriptBtn.setText(QCoreApplication.translate("MainWindow", u"Script", None))
        self.toolButton_12.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tasksTabs.setTabText(self.tasksTabs.indexOf(self.dataLoadedTab), QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Task Presets", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        ___qtreewidgetitem = self.dataTree.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Step Count", None));
        self.demoLoadBtn.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.toolButton_13.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tasksTabs.setTabText(self.tasksTabs.indexOf(self.dataPrestTab), QCoreApplication.translate("MainWindow", u"Presets", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Job history", None))
        self.toolButton_15.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tasksTabs.setTabText(self.tasksTabs.indexOf(self.dataSavedTab), QCoreApplication.translate("MainWindow", u"Saved", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.addStepButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(shortcut)
        self.addStepButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem3 = self.stepsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Task", None));
        ___qtablewidgetitem4 = self.stepsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Demo", None));
        ___qtablewidgetitem5 = self.stepsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Steps", None));
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(shortcut)
        self.runButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tasksTabs_2.setTabText(self.tasksTabs_2.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Steps", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Loaded Data", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Demo", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Audio", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Script", None))

        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.toolButton_14.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tasksTabs_2.setTabText(self.tasksTabs_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"History", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Undo History", None))
        self.toolButton_16.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tasksTabs_2.setTabText(self.tasksTabs_2.indexOf(self.tasksUndoTab), QCoreApplication.translate("MainWindow", u"Undo", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Step Info", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Step index", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Section index", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"TP", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"CI", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Hover", None));
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"More Info", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Section Info", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtablewidgetitem12 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem13 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem14 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Audio", None));
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"More Info", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.propertyTabs.setTabText(self.propertyTabs.indexOf(self.stepPropsPage), QCoreApplication.translate("MainWindow", u"Properties", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"More Info", None))
        self.toolButton_10.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.propertyTabs.setTabText(self.propertyTabs.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Preview", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtreewidgetitem1 = self.infoDemoTree.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Image", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Audio", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"TItle", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Index", None));
        self.addDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.delDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.dupeDemoStepBtn.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.toolButton_11.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.demoViewTabs.setTabText(self.demoViewTabs.indexOf(self.demoOverviewGroupPage1), QCoreApplication.translate("MainWindow", u"Demo Steps", None))
        self.demoViewTabs.setTabText(self.demoViewTabs.indexOf(self.demoMetadataTab), QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuDemo.setTitle(QCoreApplication.translate("MainWindow", u"Demo", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuTasks.setTitle(QCoreApplication.translate("MainWindow", u"Tasks", None))
    # retranslateUi

