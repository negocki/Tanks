class Level:
    width = 16
    height = 10 #default
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

        # TODO more tiles