class Player():
    def __init__(self,name,x,y):
        self.name = name 
        self.x = x
        self.y = y
        self.oldPosition = 1

    def updateXY(self,newX,newY):
        self.x = newX
        self.y = newY