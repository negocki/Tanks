from PyQt5.QtCore import QObject
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QObject, Qt, QTimer
import random
from game import Game
from gameobjects import Bullet
from xmlparser import XMLParse


class GameWindow(QDialog):

    def __init__(self):
        self.width = 16
        self.height = 16

        self.xmlp = XMLParse()


        self.tankgame = Game()
        self.terrain_generated = False
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

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_tick) # starting timer
        self.timer.start(500)
    # self.ui.pushButton.clicked.connect(self.butonClick)
    def time_tick(self):
        for bullet, i in enumerate(self.tankgame.gamelevel.bullets):
            self.tankgame.gamelevel.bullets[bullet].move()
            if ((self.tankgame.gamelevel.bullets[bullet].x_pos < 0) or (
                self.tankgame.gamelevel.bullets[bullet].x_pos > self.width) or (
                        self.tankgame.gamelevel.bullets[bullet].y_pos < 0) or (
                self.tankgame.gamelevel.bullets[bullet].y_pos > self.height)):
                del (self.tankgame.gamelevel.bullets[bullet])
        # TODO enemy tank move
        self.tankgame.gamelevel.bullet_collision_check()
        self.display_map()  # refreshing screen

    def display_map(self):
        self.tankgame.gamelevel.next_turn() # increasing turn number
        for j in range(16):
            gfxgrass = []
            gfxrock = []
            gfxtank = []
            gfxapc = []
            gfxbullet = []
            gfxbuilding = []

            for i in range(16):

                choose = True  # bool(random.getrandbits(1))
                if choose:  # todo terrain not changing
                    gfxgrass.append(self.scene.addPixmap(self.grass)) # displaying grass and dirt randomly
                else:
                    gfxgrass.append(self.scene.addPixmap(self.dirt))

                if not j%2==0:
                    gfxgrass[i].setOffset(i*32+32,16+26*j)
                else:
                    gfxgrass[i].setOffset(i * 32 + 16, 16 + 26 * j)

                if self.tankgame.gamelevel.map[j][i] == 1: # indestructable obstacle
                    gfxrock.append(self.scene.addPixmap(self.mount))
                    if not j%2 == 0:
                        gfxrock[len(gfxrock)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxrock[len(gfxrock) - 1].setOffset(i * 32 + 16, 16 + 26 * j)

                if self.tankgame.gamelevel.map[j][i] == 2: # destructable building
                    gfxbuilding.append(self.scene.addPixmap(self.building))
                    if not j%2 == 0:
                        gfxbuilding[len(gfxbuilding)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxbuilding[len(gfxbuilding) - 1].setOffset(i * 32 + 16, 16 + 26 * j)

                detected_tank = self.tankgame.gamelevel.check_for_player_tank(i, j)
                detected_enemy = self.tankgame.gamelevel.check_for_enemy_tank(i, j)

                if detected_tank != -1: # player tank
                    gfxtank.append(self.scene.addPixmap(self.tank))
                    if not j%2 == 0:
                        gfxtank[len(gfxtank)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxtank[len(gfxtank) - 1].setOffset(i * 32 + 16, 16 + 26 * j)

                if detected_enemy != -1 and len(self.tankgame.gamelevel.enemies)>0: # enemy tanks
                    gfxapc.append(self.scene.addPixmap(self.apc))
                    if not j%2 == 0:
                        gfxapc[len(gfxapc)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxapc[len(gfxapc) - 1].setOffset(i * 32 + 16, 16 + 26 * j)

                if self.tankgame.gamelevel.check_for_bullet(i, j): # bullets
                    gfxbullet.append(self.scene.addPixmap(self.bullet))
                    if not j%2 == 0:
                        gfxbullet[len(gfxbullet)-1].setOffset(i * 32 + 32, 16 + 26 * j) # offset for hexgrid
                    else:
                        gfxbullet[len(gfxbullet) - 1].setOffset(i * 32 + 16, 16 + 26 * j)


        self.ui.graphicsView.setScene(self.scene)

    def keyPressEvent(self, event): # keyboard handling

        if event.key() == Qt.Key_Q:
            self.tankgame.gamelevel.players[0].rotation = 6
            if ((self.tankgame.gamelevel.players[0].y_pos > 0) and (
                self.tankgame.gamelevel.players[0].x_pos > 0)):  # TODO q and z bug at corner
                if (self.tankgame.gamelevel.players[0].y_pos % 2 != 0):
                    collision = self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos,
                                                               self.tankgame.gamelevel.players[0].y_pos - 1)
                else:
                    collision = self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos - 1,
                                                               self.tankgame.gamelevel.players[0].y_pos - 1)
                if not collision:
                    self.tankgame.gamelevel.players[0].move(6)  # going up-left
                    self.xmlp.addAction("playermove", "6")
                    # self.xmlp.saveState(self.tankgame.gamelevel)

        if event.key() == Qt.Key_A:
            self.tankgame.gamelevel.players[0].rotation = 5
            if (self.tankgame.gamelevel.players[0].x_pos > 0):
                if (not (self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos - 1,
                                                                 self.tankgame.gamelevel.players[0].y_pos))):
                    self.tankgame.gamelevel.players[0].move(5)  # going left
                    self.xmlp.addAction("playermove", "5")


        if event.key() == Qt.Key_S:
            if (len(self.tankgame.gamelevel.bullets) < self.tankgame.gamelevel.maxbullets):
                self.tankgame.gamelevel.bullets.append(Bullet(self.tankgame.gamelevel.players[0].x_pos,
                                                              self.tankgame.gamelevel.players[0].y_pos,
                                                     self.tankgame.gamelevel.players[0].rotation))
                self.xmlp.addAction("shoot", str(self.tankgame.gamelevel.players[0].rotation))

        if event.key() == Qt.Key_Z:
            self.tankgame.gamelevel.players[0].rotation = 4
            collision = False
            if ((self.tankgame.gamelevel.players[0].y_pos < self.height) and
                    (self.tankgame.gamelevel.players[0].x_pos > 0)):
                if (self.tankgame.gamelevel.players[0].y_pos % 2 != 0):
                    collision = self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos,
                                                               self.tankgame.gamelevel.players[0].y_pos + 1)
                else:
                    collision = self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos - 1,
                                                               self.tankgame.gamelevel.players[0].y_pos + 1)
                if (not (collision)):
                    self.tankgame.gamelevel.players[0].move(4)  # going down-left
                    self.xmlp.addAction("playermove", "4")

        if event.key() == Qt.Key_X:
            self.tankgame.gamelevel.players[0].rotation = 3
            collision = False
            if ((self.tankgame.gamelevel.players[0].y_pos < self.height)
                and (self.tankgame.gamelevel.players[0].x_pos < self.width - 1)):
                if (self.tankgame.gamelevel.players[0].y_pos % 2 != 0):
                    collision = self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos + 1,
                                                               self.tankgame.gamelevel.players[0].y_pos + 1)
                else:
                    collision = self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos,
                                                               self.tankgame.gamelevel.players[0].y_pos + 1)
                if (not (collision)):
                    self.tankgame.gamelevel.players[0].move(3)  # going down-right
                    self.xmlp.addAction("playermove", "3")

        if event.key() == Qt.Key_D:
            self.tankgame.gamelevel.players[0].rotation = 2
            if (self.tankgame.gamelevel.players[0].x_pos < self.width - 1):
                if (not (self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos + 1,
                                                        self.tankgame.gamelevel.players[0].y_pos))):  # collision check
                    self.tankgame.gamelevel.players[0].move(2)  # going right
                    self.xmlp.addAction("playermove", "2")

        if event.key() == Qt.Key_E:
            self.tankgame.gamelevel.players[0].rotation = 1
            collision = False
            if self.tankgame.gamelevel.players[0].y_pos > 0 and self.tankgame.gamelevel.players[0].x_pos < self.width - 1:
                if self.tankgame.gamelevel.players[0].y_pos % 2 != 0:
                    collision = self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos + 1,
                                                               self.tankgame.gamelevel.players[0].y_pos - 1)
                else:
                    collision = self.tankgame.gamelevel.check_collision(self.tankgame.gamelevel.players[0].x_pos,
                                                               self.tankgame.gamelevel.players[0].y_pos - 1)
                if (not (collision)):
                    self.tankgame.gamelevel.players[0].move(1)  # going up-right
                    self.xmlp.addAction("playermove", "1")

        for bullet, i in enumerate(self.tankgame.gamelevel.bullets):
            self.tankgame.gamelevel.bullets[bullet].move()
            if ((self.tankgame.gamelevel.bullets[bullet].x_pos < 0) or
                    (self.tankgame.gamelevel.bullets[bullet].x_pos > self.width) or
                    (self.tankgame.gamelevel.bullets[bullet].y_pos < 0) or
                    (self.tankgame.gamelevel.bullets[bullet].y_pos > self.height)):
                del (self.tankgame.gamelevel.bullets[bullet])

        self.tankgame.gamelevel.bullet_collision_check()
        self.display_map()  # refreshing screen


    def butonClick(self):
        self.scene = QGraphicsScene(0, 0, 50, 50)
        self.item = QGraphicsEllipseItem(10, 10, 40, 40)
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)
