from PyQt5.QtCore import QObject
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import random
class GameWindow(QDialog):


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = loadUi('./dialog.ui',self) #todo rendering game level on screen
        self.scene = QGraphicsScene(0, 0, 750, 500)
        #self.item = QGraphicsEllipseItem(20, 20, 40, 40)
        self.grass = QtGui.QPixmap("gfx/grass.png")
        self.dirt = QtGui.QPixmap("gfx/dirt.png")
        self.mount = QtGui.QPixmap("gfx/Mountain.png")


        for j in range(16):
            gfxgrass = []
            gfxrock = []
            for i in range(16):
                choose = bool(random.getrandbits(1))
                if(choose):
                    gfxgrass.append(self.scene.addPixmap(self.grass))

                else:
                    gfxgrass.append(self.scene.addPixmap(self.dirt))
                    gfxrock.append(self.scene.addPixmap(self.mount))
                if(j%2==0):
                    if(not choose):
                        gfxrock[len(gfxrock)-1].setOffset(i * 32 + 32, 16 + 26 * j)
                    gfxgrass[i].setOffset(i*32+32,16+26*j)
                else:
                    if (not choose):
                        gfxrock[len(gfxrock)-1].setOffset(i * 32 + 16, 16 + 26 * j)
                    gfxgrass[i].setOffset(i * 32 + 16, 16 + 26 * j)

        self.ui.graphicsView.setScene(self.scene)
       # self.ui.pushButton.clicked.connect(self.butonClick)


    def butonClick(self):
        self.scene = QGraphicsScene(0, 0, 50, 50)
        self.item = QGraphicsEllipseItem(10, 10, 40, 40)
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)
