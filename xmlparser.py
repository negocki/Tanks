from xml.dom.minidom import *


class XMLParse:

    def __init__(self):
        self.dom = Document()
        self.root = self.dom.createElement("game")
        self.dom.appendChild(self.root)

    def addAction(self,action,value): # saving action to xml
        turn = self.dom.createElement("turn")
        self.root.appendChild(turn)

        x = self.dom.createElement(action)
        turn.appendChild(x)
        txt = self.dom.createTextNode(value)
        x.appendChild(txt)
        self.saveXML()
        print(self.dom.toxml())

    def saveState(self,level): # saving map tiles to xml for future use
        turn = self.dom.createElement("turn")
        self.root.appendChild(turn)
        for i in range(level.height):
            for j in range(level.width):
                x = self.dom.createElement("tile")
                x.setAttribute("x", str(j))
                x.setAttribute("y", str(i))
                turn.appendChild(x)
                txt = self.dom.createTextNode(str(level.map[j][i]))

                x.appendChild(txt)
                print("dodano ",j,i)
        print(self.root.toxml())
        self.saveXML()

    def saveXML(self):
        self.dom.writexml(open('save.xml', 'w'),indent="    ",addindent="   ",newl="\n")
