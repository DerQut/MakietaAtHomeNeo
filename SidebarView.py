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

        self.zStack = QStackedLayout()
        self.vContainer = QWidget()
        self.vContainer.setContentsMargins(int(6*self.guiScale), int(18*self.guiScale), int(6*self.guiScale), int(6*self.guiScale))
        self.vStack = QVBoxLayout()
        self.vStack.setSpacing(int(12*self.guiScale))
        self.vContainer.setLayout(self.vStack)

        color = Color(MacColoursDark.sidebarInactiveColour)
        self.zStack.addWidget(color)

        titleLabel = QLabel("Makieta@Home Neo")
        titleLabel.setFont(QFont("!", int(30 * self.guiScale)))
        self.vStack.addWidget(titleLabel)

        self.vStack.addWidget(Divider(MacColoursDark.gray))

        self.inputsView = InputsView(self)
        self.vStack.addWidget(self.inputsView)

        self.vStack.addStretch()
        self.zStack.addWidget(self.vContainer)

        self.zStack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self.zStack)


class InputsView(QWidget):
    def __init__(self, sidebarView: SidebarView):
        super().__init__()

        self.sidebarView = sidebarView

        self.setFixedHeight(int(240*self.sidebarView.guiScale))
        dummyLayout = QVBoxLayout()
        self.vContainer = QWidget()
        self.vContainer.setFixedWidth(int(444*0.75*self.sidebarView.guiScale))
        self.vStack = QVBoxLayout()
        self.vContainer.setLayout(self.vStack)

        i = 0
        while i < len(self.sidebarView.contentView.inputSequence):
            self.vStack.addWidget(InputEntryView(self, i, self.sidebarView.contentView.inputSequence[i]))
            i = i + 1

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidget(self.vContainer)
        dummyLayout.addWidget(self.scrollArea)

        self.setLayout(dummyLayout)


class InputEntryView(QWidget):
    def __init__(self, inputsView: InputsView, identificator: int, value: int):
        super().__init__()

        self.value = value
        self.identificator = identificator

        self.setFixedHeight(int(48*inputsView.sidebarView.guiScale))

        self.inputsView = inputsView
        hStack = QHBoxLayout()

        idLabel = QLabel(str(self.identificator))
        idLabel.setFont(QFont("Courier"))
        idLabel.setFixedWidth(int(60*self.inputsView.sidebarView.guiScale))
        hStack.addWidget(idLabel)
        hStack.addStretch()

        self.decimalField = QLineEdit(str(self.value))
        self.decimalField.setMaxLength(3)
        self.decimalField.setFont(QFont("Courier"))
        self.decimalField.setFixedWidth(int(72 * self.inputsView.sidebarView.guiScale))
        hStack.addWidget(self.decimalField)
        hStack.addStretch()

        self.binaryField = QLineEdit(f'{self.value:08b}')
        self.binaryField.setMaxLength(8)
        self.binaryField.setFont(QFont("Courier"))
        self.binaryField.setFixedWidth(int(132 * self.inputsView.sidebarView.guiScale))
        hStack.addWidget(self.binaryField)

        self.setLayout(hStack)

        self.binaryField.textChanged.connect(self.binaryFormat)
        self.decimalField.textChanged.connect(self.decimalFormat)

    def binaryFormat(self):
        self.binaryField.setText(self.binaryField.text().strip())
        text = list(self.binaryField.text())

        for character in text:
            if character not in ["0", "1"]:
                text.remove(character)
        self.binaryField.setText(''.join(text))
        self.binaryToDecimal()

    def decimalFormat(self):
        self.decimalField.setText(self.decimalField.text().strip())
        text = list(self.decimalField.text())

        for character in text:
            if not character.isdigit():
                text.remove(character)
        self.decimalField.setText(''.join(text))
        self.decimalToBinary()

    def binaryToDecimal(self):
        if self.decimalField.hasFocus():
            return
        newText = str(int(self.binaryField.text(), 2)) if self.binaryField.text() != "" else "0"

        self.decimalField.setText(newText)
        self.inputsView.sidebarView.contentView.inputSequence[self.identificator] = int(newText)

    def decimalToBinary(self):
        if self.binaryField.hasFocus():
            return
        newText = f'{int(self.decimalField.text()):08b}' if self.decimalField.text() != "" else "00000000"

        self.binaryField.setText(newText)
        self.inputsView.sidebarView.contentView.inputSequence[self.identificator] = int(newText, 2)
