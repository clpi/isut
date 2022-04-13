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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QSpinBox, QToolButton,
    QVBoxLayout, QWidget)

class Ui_opsWidget(object):
    def setupUi(self, opsWidget):
        if not opsWidget.objectName():
            opsWidget.setObjectName(u"opsWidget")
        opsWidget.resize(489, 642)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(opsWidget.sizePolicy().hasHeightForWidth())
        opsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(opsWidget)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.verticalGroupBox_3 = QGroupBox(opsWidget)
        self.verticalGroupBox_3.setObjectName(u"verticalGroupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalGroupBox_3.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_3.setSizePolicy(sizePolicy1)
        self.verticalGroupBox_3.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.verticalGroupBox_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout = QFormLayout(self.verticalGroupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.verticalGroupBox_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.stepIndexSpinbox = QSpinBox(self.verticalGroupBox_3)
        self.stepIndexSpinbox.setObjectName(u"stepIndexSpinbox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.stepIndexSpinbox)

        self.label_4 = QLabel(self.verticalGroupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

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

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.taskCombo)

        self.label = QLabel(self.verticalGroupBox_3)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.demoCombo = QComboBox(self.verticalGroupBox_3)
        self.demoCombo.setObjectName(u"demoCombo")

        self.horizontalLayout.addWidget(self.demoCombo)

        self.loadDemoBtn = QToolButton(self.verticalGroupBox_3)
        self.loadDemoBtn.setObjectName(u"loadDemoBtn")

        self.horizontalLayout.addWidget(self.loadDemoBtn)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.formLayout.setLayout(3, QFormLayout.LabelRole, self.horizontalLayout_2)


        self.horizontalLayout_5.addWidget(self.verticalGroupBox_3)

        self.verticalGroupBox_2 = QGroupBox(opsWidget)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.verticalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_2.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setBold(False)
        font.setKerning(False)
        self.verticalGroupBox_2.setFont(font)
        self.verticalGroupBox_2.setAutoFillBackground(False)
        self.verticalGroupBox_2.setStyleSheet(u"")
        self.verticalGroupBox_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalGroupBox_2.setFlat(False)
        self.stepTargetsLayout = QVBoxLayout(self.verticalGroupBox_2)
        self.stepTargetsLayout.setSpacing(2)
        self.stepTargetsLayout.setObjectName(u"stepTargetsLayout")
        self.stepTargetsLayout.setContentsMargins(4, 4, 4, 4)
        self.allDemoCheck = QCheckBox(self.verticalGroupBox_2)
        self.allDemoCheck.setObjectName(u"allDemoCheck")
        self.allDemoCheck.setMaximumSize(QSize(10000, 16777215))

        self.stepTargetsLayout.addWidget(self.allDemoCheck)

        self.allStepsCheck = QCheckBox(self.verticalGroupBox_2)
        self.allStepsCheck.setObjectName(u"allStepsCheck")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.allStepsCheck.sizePolicy().hasHeightForWidth())
        self.allStepsCheck.setSizePolicy(sizePolicy4)
        self.allStepsCheck.setMinimumSize(QSize(180, 0))
        self.allStepsCheck.setLayoutDirection(Qt.LeftToRight)

        self.stepTargetsLayout.addWidget(self.allStepsCheck)

        self.allStepsMarkedCheck = QCheckBox(self.verticalGroupBox_2)
        self.allStepsMarkedCheck.setObjectName(u"allStepsMarkedCheck")

        self.stepTargetsLayout.addWidget(self.allStepsMarkedCheck)

        self.allMarkedCheck = QCheckBox(self.verticalGroupBox_2)
        self.allMarkedCheck.setObjectName(u"allMarkedCheck")

        self.stepTargetsLayout.addWidget(self.allMarkedCheck)

        self.matchSubstringCheck = QCheckBox(self.verticalGroupBox_2)
        self.matchSubstringCheck.setObjectName(u"matchSubstringCheck")

        self.stepTargetsLayout.addWidget(self.matchSubstringCheck)

        self.titleSubstr = QLineEdit(self.verticalGroupBox_2)
        self.titleSubstr.setObjectName(u"titleSubstr")

        self.stepTargetsLayout.addWidget(self.titleSubstr)


        self.horizontalLayout_5.addWidget(self.verticalGroupBox_2)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.opParamsFrame = QGroupBox(opsWidget)
        self.opParamsFrame.setObjectName(u"opParamsFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(3)
        sizePolicy5.setHeightForWidth(self.opParamsFrame.sizePolicy().hasHeightForWidth())
        self.opParamsFrame.setSizePolicy(sizePolicy5)
        self.opParamsFrame.setAlignment(Qt.AlignCenter)
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
        self.label_3.setText(QCoreApplication.translate("opsWidget", u"Index in task queue", None))
        self.label_4.setText(QCoreApplication.translate("opsWidget", u"Selected task type", None))
        self.taskCombo.setItemText(0, QCoreApplication.translate("opsWidget", u"Shell", None))
        self.taskCombo.setItemText(1, QCoreApplication.translate("opsWidget", u"Insert", None))
        self.taskCombo.setItemText(2, QCoreApplication.translate("opsWidget", u"Crop", None))
        self.taskCombo.setItemText(3, QCoreApplication.translate("opsWidget", u"Section", None))
        self.taskCombo.setItemText(4, QCoreApplication.translate("opsWidget", u"Add Audio", None))
        self.taskCombo.setItemText(5, QCoreApplication.translate("opsWidget", u"Pacing", None))
        self.taskCombo.setItemText(6, QCoreApplication.translate("opsWidget", u"Add Text", None))
        self.taskCombo.setItemText(7, QCoreApplication.translate("opsWidget", u"Render", None))

        self.label.setText(QCoreApplication.translate("opsWidget", u"Demo target", None))
        self.loadDemoBtn.setText(QCoreApplication.translate("opsWidget", u"...", None))
#if QT_CONFIG(statustip)
        self.verticalGroupBox_2.setStatusTip(QCoreApplication.translate("opsWidget", u"Specify demo and section/step targets for the task", None))
#endif // QT_CONFIG(statustip)
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("opsWidget", u"Step Targets", None))
        self.allDemoCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all demos", None))
        self.allStepsCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all steps of selected demo", None))
        self.allStepsMarkedCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to all steps of selected sections", None))
        self.allMarkedCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to selected steps", None))
        self.matchSubstringCheck.setText(QCoreApplication.translate("opsWidget", u"Apply to sections with title containing", None))
        self.opParamsFrame.setTitle(QCoreApplication.translate("opsWidget", u"Parameters", None))
        pass
    # retranslateUi

