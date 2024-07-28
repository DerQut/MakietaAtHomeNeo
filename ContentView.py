import PyQt6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from SidebarView import *
from DetailView import *


class ContentView(QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()

        self.app = app

        self.resolution = (self.app.screens()[0].size().width(), self.app.screens()[0].size().height())

        self.setFixedHeight(int(self.resolution[1] / 3 * 2))
        self.setFixedWidth(int(self.resolution[0] / 3 * 2))

        self.navigationSplitView = QWidget(self)
        hStack = QHBoxLayout()
        self.navigationSplitView.setLayout(hStack)

        self.sidebarView = SidebarView(self)
        self.detailView = DetailView(self)

        self.setCentralWidget(self.navigationSplitView)
