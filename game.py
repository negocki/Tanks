from level import Level


class Game():
    gamelevel = Level("map1.txt",16,10)
    game_not_over = True
    def __init__(self):
        self.gamelevel.display_map()
        print()

    def gameLoop(self):
        while(self.game_not_over):
            print()
            #TODO main game loop
# TODO game mechanics
