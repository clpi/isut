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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QFormLayout, QGraphicsView, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_textOp(object):
    def setupUi(self, textOp):
        if not textOp.objectName():
            textOp.setObjectName(u"textOp")
        textOp.resize(402, 456)
        self.paramsTab = QWidget()
        self.paramsTab.setObjectName(u"paramsTab")
        self.verticalLayout = QVBoxLayout(self.paramsTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formGroupBox = QGroupBox(self.paramsTab)
        self.formGroupBox.setObjectName(u"formGroupBox")
        self.formLayout = QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.formGroupBox)
        self.label.setObjectName(u"label")
        self.label.setMargin(4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.formGroupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(131383, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.formGroupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMargin(4)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fontComboBox = QFontComboBox(self.formGroupBox)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.horizontalLayout.addWidget(self.fontComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.formGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.spinBox = QSpinBox(self.formGroupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_5 = QLabel(self.formGroupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(4)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.formGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox = QComboBox(self.formGroupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.label_8 = QLabel(self.formGroupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.comboBox_2 = QComboBox(self.formGroupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.formGroupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(self.formGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_6 = QLabel(self.formGroupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(4)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)


        self.verticalLayout.addWidget(self.formGroupBox)

        self.groupBox = QGroupBox(self.paramsTab)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(6, -1, 6, 6)
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(4)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLineWidth(0)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout_4.addWidget(self.spinBox_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setLineWidth(0)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout_4.addWidget(self.spinBox_3)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox)

        textOp.addTab(self.paramsTab, "")
        self.previewTab = QWidget()
        self.previewTab.setObjectName(u"previewTab")
        self.verticalLayout_2 = QVBoxLayout(self.previewTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.checkBox = QCheckBox(self.previewTab)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.checkBox)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_4)

        self.checkBox_2 = QCheckBox(self.previewTab)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.checkBox_2)

        self.comboBox_3 = QComboBox(self.previewTab)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setEnabled(False)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.comboBox_3)

        self.checkBox_3 = QCheckBox(self.previewTab)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.checkBox_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_3 = QPushButton(self.previewTab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.label_14 = QLabel(self.previewTab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.label_14)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.formLayout_3)

        self.groupBox_2 = QGroupBox(self.previewTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.graphicsView = QGraphicsView(self.groupBox_2)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_3.addWidget(self.graphicsView)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        textOp.addTab(self.previewTab, "")
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.fontComboBox)
        self.label_3.setBuddy(self.spinBox)
        self.label_4.setBuddy(self.comboBox)
        self.label_8.setBuddy(self.comboBox_2)
        self.label_6.setBuddy(self.pushButton)
        self.label_10.setBuddy(self.spinBox_2)
        self.label_11.setBuddy(self.spinBox_3)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(textOp)
        self.checkBox.clicked["bool"].connect(self.checkBox_2.setEnabled)
        self.checkBox.clicked["bool"].connect(self.checkBox_3.setEnabled)
        self.checkBox.clicked["bool"].connect(self.comboBox_3.setEnabled)
        self.checkBox.clicked["bool"].connect(self.pushButton_3.setEnabled)
        self.checkBox.clicked["bool"].connect(self.label_14.setEnabled)

        textOp.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(textOp)
    # setupUi

    def retranslateUi(self, textOp):
        textOp.setWindowTitle(QCoreApplication.translate("textOp", u"TabWidget", None))
        self.formGroupBox.setTitle(QCoreApplication.translate("textOp", u"Text Content Parameters", None))
        self.label.setText(QCoreApplication.translate("textOp", u"Content", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("textOp", u"Text to display", None))
        self.label_2.setText(QCoreApplication.translate("textOp", u"Font", None))
        self.label_3.setText(QCoreApplication.translate("textOp", u"Size", None))
        self.label_5.setText(QCoreApplication.translate("textOp", u"Style", None))
        self.label_4.setText(QCoreApplication.translate("textOp", u"Weight", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("textOp", u"Strong", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("textOp", u"Bold", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("textOp", u"Semibold", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("textOp", u"Regular", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("textOp", u"Semilight", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("textOp", u"Light", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("textOp", u"Thin", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("textOp", u"Regular", None))
        self.label_8.setText(QCoreApplication.translate("textOp", u"Style", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("textOp", u"Italic", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("textOp", u"Underlined", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("textOp", u"Strikethrough", None))

        self.pushButton.setText(QCoreApplication.translate("textOp", u"Select...", None))
        self.label_7.setText(QCoreApplication.translate("textOp", u"No color selected", None))
        self.label_6.setText(QCoreApplication.translate("textOp", u"Color", None))
        self.groupBox.setTitle(QCoreApplication.translate("textOp", u"Text Placement Parameters", None))
        self.label_9.setText(QCoreApplication.translate("textOp", u"Placement", None))
        self.label_10.setText(QCoreApplication.translate("textOp", u"X:", None))
        self.label_11.setText(QCoreApplication.translate("textOp", u"Y:", None))
        textOp.setTabText(textOp.indexOf(self.paramsTab), QCoreApplication.translate("textOp", u"Params", None))
        self.checkBox.setText(QCoreApplication.translate("textOp", u"Show with background", None))
        self.checkBox_2.setText(QCoreApplication.translate("textOp", u"Use currently selected demo", None))
        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("textOp", u"Step 1, Section 1", None))
        self.checkBox_3.setText(QCoreApplication.translate("textOp", u"Use custom image", None))
        self.pushButton_3.setText(QCoreApplication.translate("textOp", u"Browse...", None))
        self.label_14.setText(QCoreApplication.translate("textOp", u"No image selected", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("textOp", u"Text preview", None))
        textOp.setTabText(textOp.indexOf(self.previewTab), QCoreApplication.translate("textOp", u"Preview", None))
    # retranslateUi

