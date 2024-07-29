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

        self.outputsView = OutputsView(self)
        self.vStack.addWidget(self.outputsView)

        self.vStack.addStretch()

        buttonsHStack = QHBoxLayout()

        self.newButton = QPushButton("Nowa makieta")
        self.newButton.setFixedHeight(int(48 * self.guiScale))

        self.startButton = QPushButton("Uruchom")
        self.startButton.setFixedHeight(int(48 * self.guiScale))
        self.startButton.setStyleSheet(f"background-color: rgba{QPalette().accent().color().getRgb()};")
        self.startButton.setFont(QFont("!", int(18 * self.guiScale)))

        buttonsHStack.addWidget(self.newButton)
        buttonsHStack.addWidget(self.startButton)

        self.vStack.addLayout(buttonsHStack)

        self.zStack.addWidget(self.vContainer)

        self.zStack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.setLayout(self.zStack)


class InputsView(QWidget):
    def __init__(self, sidebarView: SidebarView):
        super().__init__()

        self.sidebarView = sidebarView

        self.entries = []

        self.setFixedHeight(int(216*self.sidebarView.guiScale))
        dummyLayout = QVBoxLayout()
        self.vContainer = QWidget()
        self.vContainer.setFixedWidth(int(336*self.sidebarView.guiScale))
        self.superVStack = QVBoxLayout()

        labelsHStack = QHBoxLayout()

        idLabel = QLabel("id:")
        decLabel = QLabel("dec:")
        binaryLabel = QLabel("binary:")
        buttonSpacer = QWidget()

        idLabel.setFont(QFont("Courier"))
        decLabel.setFont(QFont("Courier"))
        binaryLabel.setFont(QFont("Courier"))
        binaryLabel.setAlignment(Qt.AlignmentFlag.AlignLeading)

        idLabel.setFixedWidth(int(42*self.sidebarView.guiScale))
        decLabel.setFixedWidth(int(60*self.sidebarView.guiScale))
        binaryLabel.setFixedWidth(int(132*self.sidebarView.guiScale))
        buttonSpacer.setFixedWidth(int(24*self.sidebarView.guiScale))

        labelsHStack.addWidget(idLabel)
        labelsHStack.addStretch()
        labelsHStack.addWidget(decLabel)
        labelsHStack.addStretch()
        labelsHStack.addWidget(binaryLabel)
        labelsHStack.addWidget(buttonSpacer)

        self.superVStack.addLayout(labelsHStack)

        self.vStack = QVBoxLayout()
        self.vStack.setSpacing(0)
        self.superVStack.addLayout(self.vStack)
        self.vContainer.setLayout(self.superVStack)
        self.superVStack.addStretch()

        i = 0
        while i < len(self.sidebarView.contentView.inputSequence):
            entry = InputEntryView(self, i, self.sidebarView.contentView.inputSequence[i])
            self.entries.append(entry)
            self.vStack.addWidget(entry)
            i = i + 1

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.vContainer)
        dummyLayout.addWidget(self.scrollArea)

        self.setLayout(dummyLayout)

    def update(self):
        i = 0
        while i < len(self.entries):
            self.entries[i].identificator = i
            self.entries[i].idLabel.setText(str(i))
            i = i + 1


class InputEntryView(QWidget):
    def __init__(self, inputsView: InputsView, identificator: int, value: int):
        super().__init__()

        self.value = value
        self.identificator = identificator

        self.setFixedHeight(int(60*inputsView.sidebarView.guiScale))

        self.inputsView = inputsView
        hStack = QHBoxLayout()

        self.idLabel = QLabel(str(self.identificator))
        self.idLabel.setFont(QFont("Courier"))
        self.idLabel.setFixedWidth(int(42*self.inputsView.sidebarView.guiScale))
        hStack.addWidget(self.idLabel)
        hStack.addStretch()

        self.decimalField = QLineEdit(str(self.value))
        self.decimalField.setMaxLength(3)
        self.decimalField.setFont(QFont("Courier"))
        self.decimalField.setFixedWidth(int(60 * self.inputsView.sidebarView.guiScale))
        hStack.addWidget(self.decimalField)
        hStack.addStretch()

        self.binaryField = QLineEdit(f'{self.value:08b}')
        self.binaryField.setMaxLength(8)
        self.binaryField.setFont(QFont("Courier"))
        self.binaryField.setFixedWidth(int(132 * self.inputsView.sidebarView.guiScale))
        hStack.addWidget(self.binaryField)
        hStack.addStretch()

        self.deleteButton = QPushButton("✕")
        self.deleteButton.setFont(QFont("!", int(12*inputsView.sidebarView.guiScale)))
        self.deleteButton.setFixedWidth(int(24*inputsView.sidebarView.guiScale))
        self.deleteButton.setFixedHeight(int(24 * inputsView.sidebarView.guiScale))
        hStack.addWidget(self.deleteButton)

        self.setLayout(hStack)

        self.binaryField.textChanged.connect(self.binaryFormat)
        self.decimalField.textChanged.connect(self.decimalFormat)
        self.deleteButton.clicked.connect(self.remove)

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

        if int(self.decimalField.text()) > 255:
            self.decimalField.setText("255")

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

    def remove(self):
        self.inputsView.entries.remove(self)
        self.deleteLater()
        self.inputsView.update()


class OutputsView(QWidget):
    def __init__(self, sidebarView: SidebarView):
        super().__init__()
        self.sidebarView = sidebarView

        self.entries = []

        self.setFixedHeight(int(276 * self.sidebarView.guiScale))
        dummyLayout = QVBoxLayout()
        self.vContainer = QWidget()
        self.vContainer.setFixedWidth(int(336 * self.sidebarView.guiScale))
        self.superVStack = QVBoxLayout()
        self.vStack = QVBoxLayout()
        self.vStack.setSpacing(0)
        self.superVStack.addLayout(self.vStack)
        self.vContainer.setLayout(self.superVStack)
        self.superVStack.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.vContainer)
        dummyLayout.addWidget(self.scrollArea)

        self.setLayout(dummyLayout)
