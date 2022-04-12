from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtXml import QDomDocument, QDomNodeList

class DemoLoad(QTableWidgetItem):
    title: str
    path: str
    hasAudio: bool = False
    hasScript: bool = False
    xml: QXmlStreamReader

    def __init__(self, path: QFile, parent = None):
        super(DemoLoad, self).__init__(parent)
        self.xml = QXmlStreamReader(path.readAll())
        while (not self.xml.atEnd()):
            self.xml.readNext()
        # if self.xml.hasError():
        #     parent.
