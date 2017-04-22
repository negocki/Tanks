from PyQt5.QtCore import QObject
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

class GameWindow(QDialog):


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = loadUi('./dialog.ui',self) #todo rendering game level on screen
       # self.ui.pushButton.clicked.connect(self.butonClick)


    def butonClick(self):
        self.scene = QGraphicsScene(0, 0, 50, 50)
        self.item = QGraphicsEllipseItem(10, 10, 40, 40)
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)
