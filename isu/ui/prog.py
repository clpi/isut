# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_progDialog(object):
    def setupUi(self, progDialog):
        if not progDialog.objectName():
            progDialog.setObjectName(u"progDialog")
        progDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(progDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(progDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.progressBar)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.progressBar_2 = QProgressBar(self.groupBox)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.progressBar_2)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalFrame_2 = QFrame(progDialog)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.horizontalFrame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalFrame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.horizontalFrame_2)


        self.retranslateUi(progDialog)

        QMetaObject.connectSlotsByName(progDialog)
    # setupUi

    def retranslateUi(self, progDialog):
        progDialog.setWindowTitle(QCoreApplication.translate("progDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("progDialog", u"Executing...", None))
        self.label.setText(QCoreApplication.translate("progDialog", u"Currently executing op ? (type ?) of ? ops", None))
        self.label_2.setText(QCoreApplication.translate("progDialog", u"Task: ?", None))
        self.label_3.setText(QCoreApplication.translate("progDialog", u"Total queue completion", None))
        self.pushButton_2.setText(QCoreApplication.translate("progDialog", u"OK", None))
        self.pushButton.setText(QCoreApplication.translate("progDialog", u"Cancel", None))
    # retranslateUi

