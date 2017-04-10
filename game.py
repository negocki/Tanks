from level import Level
from time import sleep
import sys

class Game():
    width = 16
    height = 10
    gamelevel = Level("map1.txt",16,10)
    game_not_over = True
    def __init__(self):
        self.gamelevel.display_map()
        print()

    def gameLoop(self):
        while(self.game_not_over):
            getKey = sys.stdin.read(1)
            if(getKey=="d"):
                if(self.gamelevel.players[0].x_pos < self.width-1):
                    if(not(self.gamelevel.check_collision(self.gamelevel.players[0].x_pos+1,self.gamelevel.players[0].y_pos))): #collision check
                        self.gamelevel.players[0].move(2) #going right

            elif(getKey == "a"): #TODO other tanks collision
                if (self.gamelevel.players[0].x_pos > 0):
                    if (not (self.gamelevel.check_collision(self.gamelevel.players[0].x_pos - 1,self.gamelevel.players[0].y_pos))):
                        self.gamelevel.players[0].move(5) #going left

            elif (getKey == "e"):
                collision = False
                if ((self.gamelevel.players[0].y_pos > 0) and (self.gamelevel.players[0].x_pos<self.width-1)):
                    if(self.gamelevel.players[0].y_pos%2 != 0):
                        collision = self.gamelevel.check_collision(self.gamelevel.players[0].x_pos+1,self.gamelevel.players[0].y_pos-1)
                    else:
                        collision = self.gamelevel.check_collision(self.gamelevel.players[0].x_pos, self.gamelevel.players[0].y_pos-1)
                    if(not(collision)):
                        self.gamelevel.players[0].move(1)  # going up-right

            elif (getKey == "x"):
                collision = False
                if ((self.gamelevel.players[0].y_pos < self.height) and (self.gamelevel.players[0].x_pos<self.width-1)):
                    if(self.gamelevel.players[0].y_pos%2 != 0):
                        collision = self.gamelevel.check_collision(self.gamelevel.players[0].x_pos+1,self.gamelevel.players[0].y_pos+1)
                    else:
                        collision = self.gamelevel.check_collision(self.gamelevel.players[0].x_pos, self.gamelevel.players[0].y_pos+1)
                    if(not(collision)):
                        self.gamelevel.players[0].move(3)  # going down-right

            elif (getKey == "z"):
                collision = False
                if ((self.gamelevel.players[0].y_pos < self.height) and (self.gamelevel.players[0].x_pos>0)):
                    if(self.gamelevel.players[0].y_pos%2 != 0):
                        collision = self.gamelevel.check_collision(self.gamelevel.players[0].x_pos,self.gamelevel.players[0].y_pos+1)
                    else:
                        collision = self.gamelevel.check_collision(self.gamelevel.players[0].x_pos-1, self.gamelevel.players[0].y_pos+1)
                    if(not(collision)):
                        self.gamelevel.players[0].move(4)  # going down-left
            elif (getKey == "q"):
                collision = False
                if ((self.gamelevel.players[0].y_pos > 0) and (self.gamelevel.players[0].x_pos>0)):
                    if(self.gamelevel.players[0].y_pos%2 != 0):
                        collision = self.gamelevel.check_collision(self.gamelevel.players[0].x_pos,self.gamelevel.players[0].y_pos-1)
                    else:
                        collision = self.gamelevel.check_collision(self.gamelevel.players[0].x_pos-1, self.gamelevel.players[0].y_pos-1)
                    if(not(collision)):
                        self.gamelevel.players[0].move(6)  # going up-left

            print()
            self.gamelevel.display_map()
            print()


            #TODO main game loop
# TODO game mechanics
