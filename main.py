import sys, os
from isu.app import Isu
from PySide6.QtWidgets import *
from isu.view.window import Win
import nimporter
from inm import demo, draw
from inm import 

d = demo.DemoModel()

def main():
    a = QApplication(sys.argv)
    w = Win(a)
    w.show()
    sys.exit(a.exec())

main()