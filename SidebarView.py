import PyQt6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from assets import *
from Color import *


class SidebarView(QWidget):
    def __init__(self, contentView):
        super().__init__()

        self.setFixedWidth(int(contentView.width()/3))

        self.contentView = contentView
        self.guiScale = contentView.guiScale

        zStack = QStackedLayout()
        vContainer = QWidget()
        vContainer.setContentsMargins(int(6*self.guiScale), int(18*self.guiScale), int(6*self.guiScale), int(6*self.guiScale))
        vStack = QVBoxLayout()
        vStack.setSpacing(int(12*self.guiScale))
        vContainer.setLayout(vStack)

        color = Color(MacColoursDark.sidebarInactiveColour)
        zStack.addWidget(color)

        titleLabel = QLabel("Makieta@Home Neo")
        titleLabel.setFont(QFont("!", int(30 * self.guiScale)))
        vStack.addWidget(titleLabel)

        vStack.addWidget(Divider(MacColoursDark.gray))

        vStack.addStretch()

        zStack.addWidget(vContainer)

        zStack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(zStack)
