class Bullet():
    x_pos = 0
    y_pos = 0
    rotation = 1
    def __init__(self,x,y,rot):
        self.x_pos = x
        self.y_pos = y
        self.rotation = rot
    def move(self):
        print() # TODO move bullet to next tile
    def check_collision(self):
        print() #TODO checking for player or enemy or obstacle


class Tank():
    x_pos=0
    y_pos=0
    rotation=1
    tank_symbol = "X"
    def __init__(self,x,y,rot):
        self.x_pos = x
        self.y_pos = y
        self.rotation = rot

class PlayerTank(Tank):
    lifes = 3
    tank_symbol = "@"
    def __init__(self,x,y,rot):
        self.x_pos = x
        self.y_pos = y
        self.rotation = rot
