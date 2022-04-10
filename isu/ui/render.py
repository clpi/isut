# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'render.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_renderOp(object):
    def setupUi(self, renderOp):
        if not renderOp.objectName():
            renderOp.setObjectName(u"renderOp")
        renderOp.resize(462, 483)
        self.verticalLayout_4 = QVBoxLayout(renderOp)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.renderTabTabs = QTabWidget(renderOp)
        self.renderTabTabs.setObjectName(u"renderTabTabs")
        self.renderTabTabs.setAcceptDrops(False)
        self.renderTabTabs.setAutoFillBackground(False)
        self.renderTabTabs.setElideMode(Qt.ElideRight)
        self.renderTabTabs.setDocumentMode(False)
        self.renderTabTabs.setMovable(True)
        self.renderTabVideoTab = QWidget()
        self.renderTabVideoTab.setObjectName(u"renderTabVideoTab")
        self.verticalLayout_2 = QVBoxLayout(self.renderTabVideoTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.renderTabVideoTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 446, 444))
        self.formLayout_10 = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.videoTitleLabel = QLabel(self.groupBox)
        self.videoTitleLabel.setObjectName(u"videoTitleLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.videoTitleLabel)

        self.renderOutputTitle = QLineEdit(self.groupBox)
        self.renderOutputTitle.setObjectName(u"renderOutputTitle")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.renderOutputTitle)

        self.videoDirectoryLabel = QLabel(self.groupBox)
        self.videoDirectoryLabel.setObjectName(u"videoDirectoryLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.videoDirectoryLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.renderOutputDir = QLineEdit(self.groupBox)
        self.renderOutputDir.setObjectName(u"renderOutputDir")

        self.horizontalLayout.addWidget(self.renderOutputDir)

        self.renderBrowseDirBtn = QPushButton(self.groupBox)
        self.renderBrowseDirBtn.setObjectName(u"renderBrowseDirBtn")

        self.horizontalLayout.addWidget(self.renderBrowseDirBtn)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)


        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.renderResW = QSpinBox(self.groupBox_2)
        self.renderResW.setObjectName(u"renderResW")

        self.horizontalLayout_2.addWidget(self.renderResW)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.renderResH = QSpinBox(self.groupBox_2)
        self.renderResH.setObjectName(u"renderResH")

        self.horizontalLayout_2.addWidget(self.renderResH)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.videoFormatLabel = QLabel(self.groupBox_2)
        self.videoFormatLabel.setObjectName(u"videoFormatLabel")

        self.horizontalLayout_4.addWidget(self.videoFormatLabel)

        self.renderOutputFormat = QComboBox(self.groupBox_2)
        self.renderOutputFormat.addItem("")
        self.renderOutputFormat.addItem("")
        self.renderOutputFormat.addItem("")
        self.renderOutputFormat.addItem("")
        self.renderOutputFormat.setObjectName(u"renderOutputFormat")

        self.horizontalLayout_4.addWidget(self.renderOutputFormat)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.renderFpsSb = QDoubleSpinBox(self.groupBox_2)
        self.renderFpsSb.setObjectName(u"renderFpsSb")

        self.horizontalLayout_5.addWidget(self.renderFpsSb)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.renderAudioCheck = QCheckBox(self.groupBox_2)
        self.renderAudioCheck.setObjectName(u"renderAudioCheck")

        self.horizontalLayout_3.addWidget(self.renderAudioCheck)

        self.renderCursorCheck = QCheckBox(self.groupBox_2)
        self.renderCursorCheck.setObjectName(u"renderCursorCheck")

        self.horizontalLayout_3.addWidget(self.renderCursorCheck)

        self.renderTextCheck = QCheckBox(self.groupBox_2)
        self.renderTextCheck.setObjectName(u"renderTextCheck")

        self.horizontalLayout_3.addWidget(self.renderTextCheck)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.renderTabTabs.addTab(self.renderTabVideoTab, "")
        self.renderTabAudioTab = QWidget()
        self.renderTabAudioTab.setObjectName(u"renderTabAudioTab")
        self.verticalLayout_6 = QVBoxLayout(self.renderTabAudioTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_2 = QScrollArea(self.renderTabAudioTab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 436, 434))
        self.formLayout_11 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.scrollArea_2)

        self.renderTabTabs.addTab(self.renderTabAudioTab, "")
        self.renderTabPacingTab = QWidget()
        self.renderTabPacingTab.setObjectName(u"renderTabPacingTab")
        self.verticalLayout_8 = QVBoxLayout(self.renderTabPacingTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_3 = QScrollArea(self.renderTabPacingTab)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 436, 434))
        self.formLayout_12 = QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_8.addWidget(self.scrollArea_3)

        self.renderTabTabs.addTab(self.renderTabPacingTab, "")

        self.verticalLayout_4.addWidget(self.renderTabTabs)


        self.retranslateUi(renderOp)
        self.renderBrowseDirBtn.clicked.connect(self.renderOutputDir.update)

        self.renderTabTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(renderOp)
    # setupUi

    def retranslateUi(self, renderOp):
        self.groupBox.setTitle(QCoreApplication.translate("renderOp", u"Video Metadata", None))
        self.videoTitleLabel.setText(QCoreApplication.translate("renderOp", u"Video Title", None))
        self.renderOutputTitle.setPlaceholderText(QCoreApplication.translate("renderOp", u"Demo video title", None))
        self.videoDirectoryLabel.setText(QCoreApplication.translate("renderOp", u"Video Directory", None))
        self.renderOutputDir.setPlaceholderText(QCoreApplication.translate("renderOp", u"Demo directory", None))
        self.renderBrowseDirBtn.setText(QCoreApplication.translate("renderOp", u"Browse", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("renderOp", u"Video Settings", None))
        self.label.setText(QCoreApplication.translate("renderOp", u"Resolution", None))
        self.label_2.setText(QCoreApplication.translate("renderOp", u"Width:", None))
        self.label_3.setText(QCoreApplication.translate("renderOp", u"Height", None))
        self.videoFormatLabel.setText(QCoreApplication.translate("renderOp", u"Video Format", None))
        self.renderOutputFormat.setItemText(0, QCoreApplication.translate("renderOp", u"mp4", None))
        self.renderOutputFormat.setItemText(1, QCoreApplication.translate("renderOp", u"avi", None))
        self.renderOutputFormat.setItemText(2, QCoreApplication.translate("renderOp", u"mov", None))
        self.renderOutputFormat.setItemText(3, QCoreApplication.translate("renderOp", u"mkv", None))

        self.label_4.setText(QCoreApplication.translate("renderOp", u"Frames per second", None))
        self.renderAudioCheck.setText(QCoreApplication.translate("renderOp", u"With Audio", None))
        self.renderCursorCheck.setText(QCoreApplication.translate("renderOp", u"With Cursor", None))
        self.renderTextCheck.setText(QCoreApplication.translate("renderOp", u"With Textboxes", None))
        self.renderTabTabs.setTabText(self.renderTabTabs.indexOf(self.renderTabVideoTab), QCoreApplication.translate("renderOp", u"Video", None))
        self.renderTabTabs.setTabText(self.renderTabTabs.indexOf(self.renderTabAudioTab), QCoreApplication.translate("renderOp", u"Audio", None))
        self.renderTabTabs.setTabText(self.renderTabTabs.indexOf(self.renderTabPacingTab), QCoreApplication.translate("renderOp", u"Pacing", None))
        pass
    # retranslateUi

