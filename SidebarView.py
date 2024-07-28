import PyQt6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from assets import *
from Color import *


class SidebarView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(int(parent.width()/3))

        self.parent = parent

        color = Color(MacColoursDark.sidebarInactiveColour)
        zStack = QStackedLayout()
        zStack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        zStack.addWidget(color)

        self.setLayout(zStack)
