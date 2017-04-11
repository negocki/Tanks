from gameobjects import *
from os import system
class Level:
    width = 16
    height = 10 #default
    maxenemies = 5
    playerscount = 1 #how many players
    players = [playerscount]
    players[0] = PlayerTank(10,5,1)
    enemies = [maxenemies]
    maxbullets = 2
    bullets = [maxbullets]
    bullets[0] = Bullet(-1,-1,6)

    def __init__(self,file,wid,hei): #opening file with map and loading it to 2D list
        self.map = []
        self.width = wid
        self.height = hei
        for i in range(0,self.height):
            x = []
            for j in range(0,self.width):
                x.append(0)
            self.map.append(x)
        fmap = open(file,'r')
        print("Loading ",file)
        for i in range(0,self.height):
            line = fmap.readline()
            #print(line)
            for j in range(0,self.width):
                self.map[i][j] = int(line[j]) #string from file to int in list
        fmap.close()
        print("Level loaded.")
    def check_for_player_tank(self,x,y):  #function for checking if there is a tank at x,y
        for i in range(0,self.playerscount):
            if((self.players[i].x_pos == x) and (self.players[i].y_pos == y)):
                return i
            else:
                return -1
    #TODO check for enemy tank and display it
    def check_for_bullet(self,x,y):
        isbullet = False
        for bullet,i in enumerate(self.bullets):
            if((self.bullets[bullet].x_pos == x) and (self.bullets[bullet].y_pos == y)):
                isbullet = True
        return isbullet
    def check_collision(self,x,y):
        if(self.map[y][x] != 0): #TODO tank collision check
            print("Collision: ",x,y) #collision debug
            return True
        else:
            return False
    def bullet_collision_check(self):
        for ind, bullet in enumerate(self.bullets):
            bullet_x = self.bullets[ind].x_pos
            bullet_y = self.bullets[ind].y_pos
            if(bullet_x>0 and bullet_x<self.width and bullet_y>0 and bullet_y<self.height):
                if(self.map[bullet_y][bullet_x] == 2):
                    self.map[bullet_y][bullet_x] = 0
                    del(self.bullets[ind])
                    print("kolizja z zniszczalnym",bullet_x,bullet_y)
                elif(self.map[bullet_y][bullet_x] == 1):
                    del(self.bullets[ind])
                    print("kolizja z niezniszczalnym",bullet_x,bullet_y)
        #TODO check collision each tick
    def display_map(self):
        system('cls')  # clearing console
        for i in range(0,self.height):
            if(i%2 != 0):
                print(" ",end="")
            for j in range(0,self.width):
                detected_tank = self.check_for_player_tank(j,i)
                if(detected_tank != -1):
                    print(self.players[detected_tank].tank_symbol, end=" ") #printing player tank symbol
                elif(self.check_for_bullet(j,i)):
                    print("o", end=" ")
                elif(self.map[i][j]==0):
                    print(".", end=" ") #empty field
                elif(self.map[i][j]==1):
                    print("#",end=" ") #obstacle
                else:
                    print("%",end=" ") #destructible obstacle
            print()
        print()
        # TODO more tiles