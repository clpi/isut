# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prefs.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFontComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QSizePolicy, QSpinBox, QStackedWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_prefsDialog(object):
    def setupUi(self, prefsDialog):
        if not prefsDialog.objectName():
            prefsDialog.setObjectName(u"prefsDialog")
        prefsDialog.resize(688, 530)
        prefsDialog.setMinimumSize(QSize(600, 0))
        prefsDialog.setMaximumSize(QSize(1000000, 16777215))
        self.verticalLayout = QVBoxLayout(prefsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalGroupBox = QGroupBox(prefsDialog)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalGroupBox.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.verticalGroupBox)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setStyleSheet(u"background-color: rgba(0,0,0,0)")
        self.treeWidget.setFrameShape(QFrame.NoFrame)
        self.treeWidget.setFrameShadow(QFrame.Raised)
        self.treeWidget.setLineWidth(2)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setTextElideMode(Qt.ElideLeft)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.header().setVisible(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setProperty("showSortIndicator", False)
        self.treeWidget.header().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.treeWidget)


        self.horizontalLayout.addWidget(self.verticalGroupBox)

        self.line = QFrame(prefsDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.stackedWidget = QStackedWidget(prefsDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_4 = QFormLayout(self.groupBox)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.comboBox)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_3 = QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(11)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinBox)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.fontComboBox = QFontComboBox(self.groupBox_2)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.fontComboBox)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(prefsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Close|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(prefsDialog)
        self.buttonBox.accepted.connect(prefsDialog.accept)
        self.buttonBox.rejected.connect(prefsDialog.reject)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(prefsDialog)
    # setupUi

    def retranslateUi(self, prefsDialog):
        prefsDialog.setWindowTitle(QCoreApplication.translate("prefsDialog", u"Dialog", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("prefsDialog", u"Preferences", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("prefsDialog", u"General", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("prefsDialog", u"Appearance", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("prefsDialog", u"Behavior", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("prefsDialog", u"Advanced", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("prefsDialog", u"Theme", None))
        self.label_2.setText(QCoreApplication.translate("prefsDialog", u"Window style", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("prefsDialog", u"Native", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("prefsDialog", u"Fusion", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("prefsDialog", u"Fusion dark", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("prefsDialog", u"Accessibility", None))
        self.label_3.setText(QCoreApplication.translate("prefsDialog", u"Font size", None))
        self.label_4.setText(QCoreApplication.translate("prefsDialog", u"Font", None))
    # retranslateUi

