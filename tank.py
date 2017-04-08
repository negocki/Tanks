import numpy as np
class Level:
    def __init__(self,file): #opening file with map and loading it to 2D list
        width = 16
        height = 10
        self.map = []
        for i in range(0,height):
            x = []
            for j in range(0,width):
                x.append(0)
            self.map.append(x)
        fmap = open(file,'r')
        print("Wczytuje ",file)
        readdata = fmap.read()
        #print(readdata)
        #TODO load from file to array

        fmap.close()

    #TODO displaying map in console

#TODO game mechanics




if(__name__ == "__main__"):
    mapka = Level("map1.txt")
    print(mapka.map)