from gameobjects import *
from os import system
class Level:
    width = 16
    height = 16 #default
    maxenemies = 2
    playerscount = 1 #how many players
    players = [playerscount]
    players[0] = PlayerTank(10,5,1)
    enemies = [maxenemies]
    enemies[0] = Tank(6,1,2)
    #enemies.append(Tank(6,5,2))
    current_enemies = 1
    maxbullets = 1
    bullets = [maxbullets]
    bullets[0] = Bullet(-1,-1,6)
    turn = 0

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
            for j in range(0,self.width):
                self.map[i][j] = int(line[j])  # string from file to int in list
        fmap.close()
        print("Level loaded.")

    def check_for_player_tank(self,x,y):  # function for checking if there is a tank at x,y
        for i in range(0,self.playerscount):
            if((self.players[i].x_pos == x) and (self.players[i].y_pos == y)):
                return i
            else:
                return -1

    def check_for_enemy_tank(self, x, y):  # function for checking if there is a tank at x,y
        for i,tank in enumerate(self.enemies): # TODO more than 1 enemy bug fix
            if self.enemies[i].x_pos == x and self.enemies[i].y_pos == y and self.current_enemies > 0:
                return i
            else:
                return -1
        return -1

    def check_for_bullet(self,x,y):
        isbullet = False
        for bullet,i in enumerate(self.bullets):
            if((self.bullets[bullet].x_pos == x) and (self.bullets[bullet].y_pos == y)):
                isbullet = True
        return isbullet
    def check_collision(self,x,y):
        if self.map[y][x] != 0 or self.check_for_enemy_tank(x,y) != -1 or self.check_for_player_tank(x,y) != -1:
            print("Collision: ",x,y) #collision debug
            return True
        else:
            return False
    def bullet_collision_check(self):
        for ind, bullet in enumerate(self.bullets):
            bullet_x = self.bullets[ind].x_pos
            bullet_y = self.bullets[ind].y_pos
            enemy_tank = self.check_for_enemy_tank(bullet_x,bullet_y)
            if(bullet_x>-1 and bullet_x<self.width and bullet_y>-1 and bullet_y<self.height):
                if(self.map[bullet_y][bullet_x] == 2):
                    self.map[bullet_y][bullet_x] = 0
                    del(self.bullets[ind])
                    print("kolizja z zniszczalnym",bullet_x,bullet_y)
                elif(self.map[bullet_y][bullet_x] == 1):
                    del(self.bullets[ind])
                    print("kolizja z niezniszczalnym",bullet_x,bullet_y)
                elif(enemy_tank != -1):
                    if(len(self.enemies)>0):
                        del(self.bullets[ind])
                        del(self.enemies[enemy_tank])
                        self.current_enemies -= 1
                        self.players[0].score+=100

    def display_map(self):
        system('cls')  # clearing console
        for i in range(0,self.height):
            if(i%2 != 0):
                print(" ",end="")
            for j in range(0,self.width):
                detected_tank = self.check_for_player_tank(j,i)
                detected_enemy = self.check_for_enemy_tank(j,i)
                if(detected_tank != -1):
                    print(self.players[detected_tank].tank_symbol, end=" ") #printing player tank symbol
                elif(detected_enemy != -1 and len(self.enemies)>0):
                    print("X", end=" ")
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

    def next_turn(self):
        self.turn += 1;