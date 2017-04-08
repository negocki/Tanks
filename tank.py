import numpy as np
class Level:
    width = 16
    height = 10
    def __init__(self,file): #opening file with map and loading it to 2D list
        self.map = []
        for i in range(0,self.height):
            x = []
            for j in range(0,self.width):
                x.append(0)
            self.map.append(x)
        fmap = open(file,'r')
        print("Wczytuje ",file)
        for i in range(0,self.height):
            line = fmap.readline()
            #print(line)
            for j in range(0,self.width):
                self.map[i][j] = int(line[j]) #string from file to int in list
        fmap.close()


    def display_map(self):
        for i in range(0,self.height):
            if(i%2==0):
                print(" ",end="")
            for j in range(0,self.width):
                if(self.map[i][j]==0):
                    print(".", end=" ") #empty field
                elif(self.map[i][j]==1):
                    print("#",end=" ") #obstacle
                else:
                    print("%",end=" ") #destructible obstacle
            print()
    #TODO displaying map in console


# TODO game mechanics




if(__name__ == "__main__"):
    mapka = Level("map1.txt")
    mapka.display_map()