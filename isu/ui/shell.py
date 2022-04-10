# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shell.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)
class Ui_shellOp(object):
    def setupUi(self, shellOp):
        if not shellOp.objectName():
            shellOp.setObjectName(u"shellOp")
        shellOp.setAutoFillBackground(False)
        self.formLayout_2 = QFormLayout(shellOp)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setVerticalSpacing(40)
        self.formLayout_2.setContentsMargins(-1, 11, -1, -1)
        self.label = QLabel(shellOp)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.shellImgPath = QLineEdit(shellOp)
        self.shellImgPath.setObjectName(u"shellImgPath")

        self.horizontalLayout_4.addWidget(self.shellImgPath)

        self.shellBrowseImgBtn = QPushButton(shellOp)
        self.shellBrowseImgBtn.setObjectName(u"shellBrowseImgBtn")

        self.horizontalLayout_4.addWidget(self.shellBrowseImgBtn)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_2 = QLabel(shellOp)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(shellOp)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.shellFgX = QSpinBox(shellOp)
        self.shellFgX.setObjectName(u"shellFgX")
        self.shellFgX.setMaximum(100000000)

        self.horizontalLayout_7.addWidget(self.shellFgX)

        self.label_4 = QLabel(shellOp)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.shellFgY = QSpinBox(shellOp)
        self.shellFgY.setObjectName(u"shellFgY")
        self.shellFgY.setMaximum(100000000)

        self.horizontalLayout_7.addWidget(self.shellFgY)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_5 = QLabel(shellOp)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(shellOp)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.shellFgW = QSpinBox(shellOp)
        self.shellFgW.setObjectName(u"shellFgW")
        self.shellFgW.setMaximum(100000000)

        self.horizontalLayout_8.addWidget(self.shellFgW)

        self.label_6 = QLabel(shellOp)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.shellFgH = QSpinBox(shellOp)
        self.shellFgH.setObjectName(u"shellFgH")
        self.shellFgH.setMaximum(10000000)

        self.horizontalLayout_8.addWidget(self.shellFgH)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_8)


        self.retranslateUi(shellOp)

        QMetaObject.connectSlotsByName(shellOp)
    # setupUi

    def retranslateUi(self, shellOp):
        self.label.setText(QCoreApplication.translate("shellOp", u"Background", None))
#if QT_CONFIG(statustip)
        self.shellImgPath.setStatusTip(QCoreApplication.translate("shellOp", u"Filepath of image to be used as shell for demo assets", None))
#endif // QT_CONFIG(statustip)
        self.shellBrowseImgBtn.setText(QCoreApplication.translate("shellOp", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("shellOp", u"Coordinates of assets on shell", None))
        self.label_3.setText(QCoreApplication.translate("shellOp", u"X", None))
        self.label_4.setText(QCoreApplication.translate("shellOp", u"Y", None))
        self.label_5.setText(QCoreApplication.translate("shellOp", u"Dimensions of assets on shell", None))
        self.label_7.setText(QCoreApplication.translate("shellOp", u"Width", None))
        self.label_6.setText(QCoreApplication.translate("shellOp", u"Height", None))
        pass
    # retranslateUi

