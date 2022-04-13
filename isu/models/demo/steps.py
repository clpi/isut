from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtXml import QDomDocument, QDomNodeList

class DemoSteps(QObject):

    def __init__(self, file: QFile, parent=None):
        reader = QXmlStreamReader(file.readAll())
        while (not reader.atEnd()):
            tty = reader.readNext()
        if reader.hasError():
            print(f"Error: {reader.errorString()}")
            QMessageBox.critical(parent, "Error", reader.errorString())