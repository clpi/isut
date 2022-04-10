# import os, sys
# from typing import Optional, Sequence, Dict, Any
# from PIL import Image
# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
# from PySide6.QtWidgets import (
#     QApplication, QSizePolicy, QWidget, QLabel, QFormLayout, QHBoxLayout,
#     QVBoxLayout, QLineEdit, QLayout, QPushButton, QCheckBox, QComboBox, 
#     QSpinBox, QStackedLayout, QStackedWidget, QFileDialog
#     )
# from isu.view import UiLoader

# class SectionOp(QWidget):

#     ui: QWidget | None = None
#     parent: Any = QCoreApplication.instance()
#     index: int
#     path: str

#     def __init__(self, parent: QWidget | None) -> None:
#         QWidget.__init__(self, parent)
#         UiLoad().loadUi("render.ui", self, parent)

#     def loadUi(self):
#         pass

#     def op(self) -> Section:
#         return Section()

#         # self.opsParamsStack.addWidget(self)

#         # self.shellBrowseImgBtn.clicked.connect(self.browse_shell)
