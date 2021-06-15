class Player():
    def __init__(self,name,x,y):
        self.name = name 
        self.x = x
        self.y = y
        self.oldPosition = 1
        self.playerCards = []
        self.room = ()

    def updateXY(self,newX,newY):
        self.x = newX
        self.y = newY

    def showHand(self):
        return self.playerCards

class Players():
    def __init__(self):
        self.allPlayersDict = {}
    def createPlayers(self):
        scar = Player('Ms Scarlett',24,7)
        green = Player('Rev Green',0,14)
        self.addPlayersDict(scar,self.allPlayersDict)
        self.addPlayersDict(green,self.allPlayersDict)
    def addPlayersDict(self,player,dict):
        dict[player.name] = player

p = Players()
p.createPlayers()
