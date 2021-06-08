from player import Player
import gameSetup

class Gameplay:
    def startPosition(self,players): #this should probably be in gamesetup
        for player in players:
    	    gameSetup.gs.board[player.x][player.y] = -1
    def movePieceUp(self,player):
        newX = player.x +1
        newY = player.y
        self.checkValidPosition(player.x,player.y,newX,newY,player)
    def movePieceDown(self,player):
        newX = player.x -1
        newY = player.y
        self.checkValidPosition(player.x,player.y,newX,newY,player)
    def movePieceLeft(self,player):
        newX = player.x
        newY = player.y -1
        self.checkValidPosition(player.x,player.y,newX,newY,player)
    def movePieceRight(self,player):
        newX = player.x
        newY = player.y +1
        self.checkValidPosition(player.x,player.y,newX,newY,player)
    # must allow the player to enter another move is the move is invalid
    def checkValidPosition(self,x,y,newX,newY,player):
        if gameSetup.gs.board[newX][newY] != 1:
            print('invalid move')
        else:
            temp = gameSetup.gs.board[newX][newY] 
            gameSetup.gs.board[newX][newY] = -1
            gameSetup.gs.board[x][y] = gameSetup.gs.oldPosition 
            gameSetup.gs.oldPosition = temp   
            print('valid move')
            player.updateXY(newX,newY)

    # def returnPosisiton(self):
    # 	print(x,y)

gp = Gameplay()
player1 = Player('George',0,9)
player2 = Player('Billy',0,14)
players = [player1,player2]
gp.startPosition(players)

gp.movePieceUp(player2)
print(gameSetup.gs.board)
gp.movePieceDown(player1)
print(gameSetup.gs.board)