from window import GameWindow
from PyQt5.QtWidgets import *

import sys

if(__name__ == "__main__"):
    qApp = QApplication(sys.argv)
    app = GameWindow()
    app.show()
    sys.exit(qApp.exec_())

    tankgame = Game()
    tankgame.gameLoop()