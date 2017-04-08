import numpy as np
class Level:
    def __init__(self,file): #opening file with map and loading it to 2D lists
        self.map = []
        for i in range(0,10):
            x = []
            for j in range(0,16):
                x.append(0)
            self.map.append(x)
        fmap = open(file,'r')
        print("Wczytuje ",file)
        readdata = fmap.read()
        #print(readdata)

        
        fmap.close()








if(__name__ == "__main__"):
    mapka = Level("map1.txt")
    print(mapka.map)