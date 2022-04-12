# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optab.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QSizePolicy, QSpacerItem, QSpinBox, QToolButton,
    QVBoxLayout, QWidget)

class Ui_opsWidget(object):
    def setupUi(self, opsWidget):
        if not opsWidget.objectName():
            opsWidget.setObjectName(u"opsWidget")
        opsWidget.resize(489, 576)
        self.verticalLayout_4 = QVBoxLayout(opsWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalGroupBox_3 = QGroupBox(opsWidget)
        self.verticalGroupBox_3.setObjectName(u"verticalGroupBox_3")
        self.verticalGroupBox_3.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.verticalLayout_2 = QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalGroupBox_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(463, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.stepIndexSpin = QSpinBox(self.verticalGroupBox_3)
        self.stepIndexSpin.setObjectName(u"stepIndexSpin")

        self.horizontalLayout_2.addWidget(self.stepIndexSpin)

        self.label_6 = QLabel(self.verticalGroupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.toolButton_3 = QToolButton(self.verticalGroupBox_3)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_2.addWidget(self.toolButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalGroupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(463, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.verticalGroupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.taskCombo = QComboBox(self.verticalGroupBox_3)
        self.taskCombo.addItem("")
        self.taskCombo.addItem("")
        self.taskCombo.addItem("")
        self.taskCombo.addItem("")
        self.taskCombo.addItem("")
        self.taskCombo.addItem("")
        self.taskCombo.addItem("")
        self.taskCombo.addItem("")
        self.taskCombo.setObjectName(u"taskCombo")

        self.horizontalLayout.addWidget(self.taskCombo)

        self.toolButton = QToolButton(self.verticalGroupBox_3)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.targetLayout = QHBoxLayout()
        self.targetLayout.setObjectName(u"targetLayout")
        self.label = QLabel(self.verticalGroupBox_3)
        self.label.setObjectName(u"label")

        self.targetLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.targetLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.verticalGroupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.targetLayout.addWidget(self.label_5)

        self.demoCombo = QComboBox(self.verticalGroupBox_3)
        self.demoCombo.setObjectName(u"demoCombo")

        self.targetLayout.addWidget(self.demoCombo)

        self.loadDemoBtn = QToolButton(self.verticalGroupBox_3)
        self.loadDemoBtn.setObjectName(u"loadDemoBtn")

        self.targetLayout.addWidget(self.loadDemoBtn)


        self.verticalLayout_2.addLayout(self.targetLayout)


        self.horizontalLayout_5.addWidget(self.verticalGroupBox_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalGroupBox_2 = QGroupBox(opsWidget)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.allDemoCheck = QCheckBox(self.verticalGroupBox_2)
        self.allDemoCheck.setObjectName(u"allDemoCheck")
        self.allDemoCheck.setMaximumSize(QSize(10000, 16777215))

        self.verticalLayout_5.addWidget(self.allDemoCheck)

        self.allStepsCheck = QCheckBox(self.verticalGroupBox_2)
        self.allStepsCheck.setObjectName(u"allStepsCheck")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.allStepsCheck.sizePolicy().hasHeightForWidth())
        self.allStepsCheck.setSizePolicy(sizePolicy1)
        self.allStepsCheck.setMinimumSize(QSize(180, 0))
        self.allStepsCheck.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_5.addWidget(self.allStepsCheck)

        self.allStepsMarkedCheck = QCheckBox(self.verticalGroupBox_2)
        self.allStepsMarkedCheck.setObjectName(u"allStepsMarkedCheck")

        self.verticalLayout_5.addWidget(self.allStepsMarkedCheck)

        self.allMarkedCheck = QCheckBox(self.verticalGroupBox_2)
        self.allMarkedCheck.setObjectName(u"allMarkedCheck")

        self.verticalLayout_5.addWidget(self.allMarkedCheck)

        self.matchSubstringCheck = QCheckBox(self.verticalGroupBox_2)
        self.matchSubstringCheck.setObjectName(u"matchSubstringCheck")

        self.verticalLayout_5.addWidget(self.matchSubstringCheck)

        self.titleSubstr = QLineEdit(self.verticalGroupBox_2)
        self.titleSubstr.setObjectName(u"titleSubstr")

        self.verticalLayout_5.addWidget(self.titleSubstr)


        self.horizontalLayout_5.addWidget(self.verticalGroupBox_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.opParamsFrame = QGroupBox(opsWidget)
        self.opParamsFrame.setObjectName(u"opParamsFrame")
        self.verticalLayout = QVBoxLayout(self.opParamsFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.opParamsLayout = QVBoxLayout()
        self.opParamsLayout.setObjectName(u"opParamsLayout")

        self.verticalLayout.addLayout(self.opParamsLayout)


        self.verticalLayout_4.addWidget(self.opParamsFrame)


        self.retranslateUi(opsWidget)

        QMetaObject.connectSlotsByName(opsWidget)
    # setupUi

    def retranslateUi(self, opsWidget):
        self.verticalGroupBox_3.setTitle(QCoreApplication.translate("opsWidget", u"Task Info", None))
        self.label_3.setText(QCoreApplication.translate("opsWidget", u"Index", None))
        self.label_6.setText(QCoreApplication.translate("opsWidget", u"Index:", None))
        self.toolButton_3.setText(QCoreApplication.translate("opsWidget", u"...", None))
        self.label_2.setText(QCoreApplication.translate("opsWidget", u"Task", None))
        self.label_4.setText(QCoreApplication.translate("opsWidget", u"Current:", None))
        self.taskCombo.setItemText(0, QCoreApplication.translate("opsWidget", u"Shell", None))
        self.taskCombo.setItemText(1, QCoreApplication.translate("opsWidget", u"Insert", None))
        self.taskCombo.setItemText(2, QCoreApplication.translate("opsWidget", u"Crop", None))
        self.taskCombo.setItemText(3, QCoreApplication.translate("opsWidget", u"Section", None))
        self.taskCombo.setItemText(4, QCoreApplication.translate("opsWidget", u"Add Audio", None))
        self.taskCombo.setItemText(5, QCoreApplication.translate("opsWidget", u"Pacing", None))
        self.taskCombo.setItemText(6, QCoreApplication.translate("opsWidget", u"Add Text", None))
        self.taskCombo.setItemText(7, QCoreApplication.translate("opsWidget", u"Render", None))

        self.toolButton.setText(QCoreApplication.translate("opsWidget", u"...", None))
        self.label.setText(QCoreApplication.translate("opsWidget", u"Target", None))
        self.label_5.setText(QCoreApplication.translate("opsWidget", u"Demo:", None))
        self.loadDemoBtn.setText(QCoreApplication.translate("opsWidget", u"...", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("opsWidget", u"Step Targets", None))
        self.allDemoCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all demos", None))
        self.allStepsCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all steps", None))
        self.allStepsMarkedCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all steps of marked sections", None))
        self.allMarkedCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to marked steps", None))
        self.matchSubstringCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to steps with title containing:", None))
        self.opParamsFrame.setTitle(QCoreApplication.translate("opsWidget", u"Parameters", None))
        pass
    # retranslateUi

