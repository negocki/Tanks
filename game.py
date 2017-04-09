from level import Level
from os import system
from time import sleep
import msvcrt
import sys

class Game():
    gamelevel = Level("map1.txt",16,10)
    game_not_over = True
    def __init__(self):
        self.gamelevel.display_map()
        print()

    def gameLoop(self):
        while(self.game_not_over):
            if(sys.stdin.read(1)=="q"):
                system('cls') #clearing console
                self.gamelevel.display_map()
                print()
                sleep(1)
                #msvcrt.getch()

            #TODO main game loop
# TODO game mechanics
