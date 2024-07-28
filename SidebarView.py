import PyQt6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from assets import *
from Color import *


class SidebarView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(int(parent.width()/3), parent.height())

        self.parent = parent

        color = Color(MacColoursDark.side_bar_inactive_colour)
        zStack = QStackedLayout()
        zStack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        zStack.addWidget(color)

        self.setLayout(zStack)
