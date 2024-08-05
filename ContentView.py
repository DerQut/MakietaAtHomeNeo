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
        DEBUG = True

        self.inputSequence = [0, 1, 3, 2, 3, 1, 255, 1, 2, 3, 4, 5, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.outputGraphs = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        self.boards = []

        self.app = app
        print(self.app.primaryScreen().size())

        shortestScreen = self.app.primaryScreen()
        for screen in self.app.screens():
            if screen.size().height() < shortestScreen.size().height():
                shortestScreen = screen

        self.resolution = (shortestScreen.size().width(), shortestScreen.size().height()) if not DEBUG else (1920, 1080)
        self.guiScale = self.resolution[1]/1080

        self.setFixedHeight(int(self.resolution[1] / 3 * 2))
        self.setFixedWidth(int(self.resolution[0] / 3 * 2))

        self.navigationSplitView = QWidget(self)
        self.hStack = QHBoxLayout()
        self.hStack.setSpacing(0)
        self.hStack.setContentsMargins(0, 0, 0, 0)

        self.sidebarView = SidebarView(self)
        self.detailView = DetailView(self)
        spacer = Color(MacColoursDark.splitColour)
        spacer.setFixedWidth(1)

        self.hStack.addWidget(self.sidebarView)
        self.hStack.addWidget(spacer)
        self.hStack.addWidget(self.detailView)
        self.navigationSplitView.setLayout(self.hStack)

        self.setCentralWidget(self.navigationSplitView)
