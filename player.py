import board

class Player():
    def __init__(self,name,x,y,colour):
        self.name = name 
        self.x = x
        self.y = y
        self.oldPosition = 1
        self.playerCards = []
        self.room = ()
        self.colour = colour
        self.token = None

    def updateXY(self,newX,newY):
        self.x = newX
        self.y = newY

    def showHand(self):
        return self.playerCards

class Players():
    def __init__(self):
        self.allPlayersDict = {}
    def createPlayers(self):
        scar = Player('Miss Scarlett',24,7,'red')
        green = Player('Reverend Green',0,14,'green')
        self.addPlayersDict(scar,self.allPlayersDict)
        self.addPlayersDict(green,self.allPlayersDict)
    def addPlayersDict(self,player,dict):
        dict[player.name] = player
    def placePlayersOnBoard(self):
        for p in self.allPlayersDict.values():
            print(p.x ,p.y)
            h1,h2 = 44 + 22.92*(p.x),44 + 22.92*(p.x +1)
            w1,w2 = 63 + 22.91*(p.y),63 + 22.91*(p.y +1)
            p.token = board.b.board.create_rectangle(w1, h1, w2, h2, fill=p.colour)
    def movePlayerOnBoard(self,selectedPlayer):
        board.b.board.delete(selectedPlayer.token)
        h1,h2 = 44 + 22.92*(selectedPlayer.x),44 + 22.92*(selectedPlayer.x +1)
        w1,w2 = 63 + 22.91*(selectedPlayer.y),63 + 22.91*(selectedPlayer.y +1)
        selectedPlayer.token = board.b.board.create_rectangle(w1, h1, w2, h2, fill=selectedPlayer.colour)

p = Players()
p.createPlayers()
