from level import Level


class Game():
    gamelevel = Level("map1.txt",16,10)
    def __init__(self):
        self.gamelevel.display_map()
        print()
# TODO game mechanics
