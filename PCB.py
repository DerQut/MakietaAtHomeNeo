import PyQt6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

import assets
import logicElements


class Board(QWidget):
    def __init__(self, contentView: QWidget, template: str):
        super().__init__()

        self.packages: [Package] = []
        self.template = template
        self.contentView = contentView

        contentView.boards.append(self)


class Package(QWidget):
    def __init__(self, board: Board, gate: logicElements.Gate):
        super().__init__()
        self.board = board
        self.gate = gate

        mainHStack = QHBoxLayout()
        inputsVStack = QVBoxLayout()
        outputsVStack = QVBoxLayout()

        board.packages.append(self)
