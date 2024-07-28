import sys

import PyQt6
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from ContentView import *


def main():
    app = QApplication(sys.argv)

    contentView = ContentView(app)
    contentView.show()

    contentView.setWindowTitle("Makieta@HomeNeo")

    app.setStyle("fusion")
    app.setFont(QFont("Helvetica", int(16*contentView.guiScale)))

    app.exec()

    return 0


if __name__ == "__main__":
    main()
