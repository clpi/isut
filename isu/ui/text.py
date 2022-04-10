# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_textOp(object):
    def setupUi(self, textOp):
        if not textOp.objectName():
            textOp.setObjectName(u"textOp")
        textOp.resize(350, 276)
        self.verticalLayout = QVBoxLayout(textOp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(textOp)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 330, 206))
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 120, 80))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.label_8 = QLabel(textOp)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.comboBox = QComboBox(textOp)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)


        self.retranslateUi(textOp)

        QMetaObject.connectSlotsByName(textOp)
    # setupUi

    def retranslateUi(self, textOp):
        self.groupBox.setTitle(QCoreApplication.translate("textOp", u"GroupBox", None))
        self.label_8.setText(QCoreApplication.translate("textOp", u"Audio attachment behavior", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("textOp", u"Mixed section and step audio", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("textOp", u"Section audio only", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("textOp", u"Step audio only", None))

        pass
    # retranslateUi

