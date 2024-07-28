import PyQt6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from SidebarView import *
from DetailView import *
from Color import *
from assets import *


class ContentView(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app = app

        self.resolution = (self.app.screens()[0].size().width(), self.app.screens()[0].size().height())
        self.guiScale = self.resolution[1]/1080

        self.setFixedHeight(int(self.resolution[1] / 3 * 2))
        self.setFixedWidth(int(self.resolution[0] / 3 * 2))

        self.navigationSplitView = QWidget(self)
        hStack = QHBoxLayout()
        hStack.setSpacing(0)
        hStack.setContentsMargins(0, 0, 0, 0)

        self.sidebarView = SidebarView(self)
        self.detailView = DetailView(self)
        spacer = Color(MacColoursDark.splitColour)
        spacer.setFixedWidth(1)

        hStack.addWidget(self.sidebarView)
        hStack.addWidget(spacer)
        hStack.addWidget(self.detailView)
        self.navigationSplitView.setLayout(hStack)

        self.setCentralWidget(self.navigationSplitView)
