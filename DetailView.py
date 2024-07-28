import PyQt6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from Color import *
from assets import *


class DetailView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        color = Color(MacColoursDark.bgColour)
        zStack = QStackedLayout()
        zStack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        zStack.addWidget(color)

        self.setLayout(zStack)
