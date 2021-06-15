class Player():
    def __init__(self,name,x,y):
        self.name = name 
        self.x = x
        self.y = y
        self.oldPosition = 1
        self.playerCards = []

    def updateXY(self,newX,newY):
        self.x = newX
        self.y = newY

    def showHand(self):
        return self.playerCards