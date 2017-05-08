import sys

from gameobjects import *
from level import Level

class Game():
    width = 16
    height = 16
    gamelevel = Level("map1.txt",16,16)
    game_not_over = True
    def __init__(self):
        self.gamelevel.display_map()
        print()