# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noop.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_noOp(object):
    def setupUi(self, noOp):
        if not noOp.objectName():
            noOp.setObjectName(u"noOp")
        noOp.resize(400, 508)
        self.verticalLayout = QVBoxLayout(noOp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalGroupBox = QGroupBox(noOp)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.verticalGroupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.verticalGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.verticalGroupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.verticalGroupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.verticalGroupBox)

        self.groupBox_2 = QGroupBox(noOp)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(noOp)

        QMetaObject.connectSlotsByName(noOp)
    # setupUi

    def retranslateUi(self, noOp):
        noOp.setWindowTitle(QCoreApplication.translate("noOp", u"Form", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("noOp", u"Load the automation target", None))
        self.label_2.setText(QCoreApplication.translate("noOp", u"Try loading a demo below:", None))
        self.label_4.setText(QCoreApplication.translate("noOp", u"Demo to load:", None))
        self.pushButton.setText(QCoreApplication.translate("noOp", u"Browse", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("noOp", u"GroupBox", None))
        self.label_5.setText(QCoreApplication.translate("noOp", u"Try selecting a task to perform:", None))
        self.label_6.setText(QCoreApplication.translate("noOp", u"Task to perform", None))
        self.pushButton_2.setText(QCoreApplication.translate("noOp", u"Browse", None))
    # retranslateUi

