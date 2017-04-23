from PyQt5.QtCore import QObject
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QObject, Qt
import random
from game import Game
class GameWindow(QDialog):


    def __init__(self):
        self.tankgame = Game()
        QMainWindow.__init__(self)
        self.ui = loadUi('./dialog.ui',self) #todo rendering game level on screen
        self.scene = QGraphicsScene(0, 0, 570, 460)
        # self.item = QGraphicsEllipseItem(20, 20, 40, 40)
        self.grass = QtGui.QPixmap("gfx/grass.png")  # loading tiles
        self.dirt = QtGui.QPixmap("gfx/dirt.png")
        self.mount = QtGui.QPixmap("gfx/Mountain.png")
        self.tank = QtGui.QPixmap("gfx/Tank.png")
        self.apc = QtGui.QPixmap("gfx/APC.png")
        self.bullet = QtGui.QPixmap("gfx/Target.png")
        self.building = QtGui.QPixmap("gfx/Building.png")
        self.display_map()
    # self.ui.pushButton.clicked.connect(self.butonClick)

    def display_map(self):
        for j in range(16):
            gfxgrass = []
            gfxrock = []
            gfxtank = []
            gfxapc = []
            gfxbullet = []
            gfxbuilding = []
            for i in range(16):
                choose = bool(random.getrandbits(1))
                if choose:
                    gfxgrass.append(self.scene.addPixmap(self.grass)) # displaying grass and dirt randomly
                else:
                    gfxgrass.append(self.scene.addPixmap(self.dirt))

                if j%2==0:
                    # if not choose:
                       # gfxrock[len(gfxrock)-1].setOffset(i * 32 + 32, 16 + 26 * j)
                    gfxgrass[i].setOffset(i*32+32,16+26*j)
                else:
                    #if not choose:
                       # gfxrock[len(gfxrock)-1].setOffset(i * 32 + 16, 16 + 26 * j)
                    gfxgrass[i].setOffset(i * 32 + 16, 16 + 26 * j)

                if self.tankgame.gamelevel.map[j][i] == 1: # indestructable obstacle
                    gfxrock.append(self.scene.addPixmap(self.mount))
                    if j%2 == 0:
                        gfxrock[len(gfxrock)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxrock[len(gfxrock) - 1].setOffset(i * 32 + 16, 16 + 26 * j)

                if self.tankgame.gamelevel.map[j][i] == 2: # destructable building
                    gfxbuilding.append(self.scene.addPixmap(self.building))
                    if j%2 == 0:
                        gfxbuilding[len(gfxbuilding)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxbuilding[len(gfxbuilding) - 1].setOffset(i * 32 + 16, 16 + 26 * j)

                detected_tank = self.tankgame.gamelevel.check_for_player_tank(i, j)
                detected_enemy = self.tankgame.gamelevel.check_for_enemy_tank(i, j)

                if detected_tank != -1: # player tank
                    gfxtank.append(self.scene.addPixmap(self.tank))
                    if j%2 == 0:
                        gfxtank[len(gfxtank)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxtank[len(gfxtank) - 1].setOffset(i * 32 + 16, 16 + 26 * j)

                if detected_enemy != -1 and len(self.tankgame.gamelevel.enemies)>0: # enemy tanks
                    gfxapc.append(self.scene.addPixmap(self.apc))
                    if j%2 == 0:
                        gfxapc[len(gfxapc)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxapc[len(gfxapc) - 1].setOffset(i * 32 + 16, 16 + 26 * j)

                if self.tankgame.gamelevel.check_for_bullet(i, j): # bullets
                    gfxbullet.append(self.scene.addPixmap(self.bullet))
                    if j%2 == 0:
                        gfxbullet[len(gfxbullet)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxbullet[len(gfxbullet) - 1].setOffset(i * 32 + 16, 16 + 26 * j)


        self.ui.graphicsView.setScene(self.scene)

    def keyPressEvent(self, event): # keyboard handling

        if event.key() == Qt.Key_Q:
            print() # todo tank moving



    def butonClick(self):
        self.scene = QGraphicsScene(0, 0, 50, 50)
        self.item = QGraphicsEllipseItem(10, 10, 40, 40)
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)
