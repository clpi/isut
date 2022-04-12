from PySide6.QtCore import *
from typing import Type
import sys
from PySide6.QtWidgets import *


def app() -> QCoreApplication:
    match QApplication.instance():
        case None: return QApplication(sys.argv)
        case ins: return ins

def browseDir(base: QWidget, msg: str,
              cwd: str = QDir.currentPath(),
              ft: str = "All folders (*.dir)") -> str | None:
    dir_name, ok = QFileDialog.getExistingDirectory(base, msg, cwd)
    if ok: return dir_name; return None


def browseFile(base: QWidget, msg: str,
             cwd: str = QDir.currentPath(),
             ft: str = "All Files (*.*)") -> str | None:
    file_name, ok = QFileDialog.getOpenFileName(base, msg, cwd, ft)
    if ok: return file_name; return None

def show(name: str, widget: Type[QWidget] | Type[QMainWindow]):
    if name == "__main__":
        print(f"Showing {widget.__name__}")
        a = app()
        if type(widget) == QMainWindow:
            w = widget(parent=None)
        else:
            mw = QMainWindow(parent=None)
            w = widget(parent=mw)
        w.show()
        sys.exit(a.exec())

def showUi(widget):
    a = app()
    w = widget()
    w.setupUi(w)
    w.show()
    sys.exit(a.exec())

