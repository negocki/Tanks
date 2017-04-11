class Bullet():
    x_pos = 0
    y_pos = 0
    rotation = 1
    def __init__(self,x,y,rot):
        self.x_pos = x
        self.y_pos = y
        self.rotation = rot
    def move(self):
        if (self.rotation == 1):
            if(self.y_pos%2 == 0):
                self.y_pos -= 1
            else:
                self.y_pos -= 1
                self.x_pos += 1
            #up-right
        elif (self.rotation == 2):
            self.x_pos += 1
            self.rotation = 2
            #right
        elif (self.rotation == 3):
            if (self.y_pos % 2 == 0):
                self.y_pos += 1
            else:
                self.y_pos += 1
                self.x_pos += 1
            #down-right
        elif (self.rotation == 4):
            if (not(self.y_pos % 2 == 0)):
                self.y_pos += 1
            else:
                self.y_pos += 1
                self.x_pos -= 1
            #down-left
        elif (self.rotation == 5):
            self.x_pos -= 1
            #left
        elif (self.rotation == 6):
            if (not(self.y_pos % 2 == 0)):
                self.y_pos -= 1
            else:
                self.y_pos -= 1
                self.x_pos -= 1
            #up-left

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

    def move(self,dir):
        if (dir == 1):
            self.rotation = 1
            if(self.y_pos%2 == 0):
                self.y_pos -= 1
            else:
                self.y_pos -= 1
                self.x_pos += 1
            #up-right
        elif (dir == 2):
            self.x_pos += 1
            self.rotation = 2
            #right
        elif (dir == 3):
            self.rotation = 3
            if (self.y_pos % 2 == 0):
                self.y_pos += 1
            else:
                self.y_pos += 1
                self.x_pos += 1
            #down-right
        elif (dir == 4):
            if (not(self.y_pos % 2 == 0)):
                self.y_pos += 1
            else:
                self.y_pos += 1
                self.x_pos -= 1
            self.rotation = 4
            #down-left
        elif (dir == 5):
            self.x_pos -= 1
            self.rotation = 5
            #left
        elif (dir == 6):
            self.rotation = 6
            if (not(self.y_pos % 2 == 0)):
                self.y_pos -= 1
            else:
                self.y_pos -= 1
                self.x_pos -= 1
            #up-left
        #TODO check collision and move
class PlayerTank(Tank):
    lifes = 3
    tank_symbol = "@"
    score = 0
    def __init__(self,x,y,rot):
        self.x_pos = x
        self.y_pos = y
        self.rotation = rot
