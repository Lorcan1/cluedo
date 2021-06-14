from player import Player
import numpy as np
import gamesetup
import random

class Gameplay:
    def __init__(self):
    # This array "squareType" stores what kind of square each square on the board is, which determines if it can be accessed by counters
     # Squares that are marked 0 are inaccessible by the player (they are out of bounds)
     # Squares that are marked 1 are pathways that the player can walk on
     # Sqaures that are marked 2 are pathway squares that are adjacent to room entrances - this is needed so we can exit rooms easily
     # Sqaures that are marked 3 are squares inside rooms - they cannot be accessed directly
     # Sqaures that are marked 4 are room squares that are adjacent to room entrances
     # All negative squares are occupied by another user (e.g. -1 is an occupied pathway square
     
        self.board = np.array([   
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 3, 3, 3, 3, 3, 0, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 4, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 1, 2, 4, 3, 3, 3, 3, 3, 3, 4, 2, 1, 2, 3, 3, 3, 3, 0, 0],
        [3, 3, 3, 3, 4, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 2, 1, 1, 1, 3, 4, 3, 3, 3, 3, 4, 3, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 4, 2, 1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3, 4, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 2, 1, 2, 0, 0],
        [3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 4, 3, 3, 0, 0],
        [3, 3, 3, 3, 3, 3, 4, 3, 1, 1, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 3, 4, 3, 3, 1, 2, 4, 3, 3, 3, 3, 3, 3, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 1, 1, 1, 1, 1, 2, 1, 1, 3, 3, 4, 4, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 0, 0],
        [3, 3, 3, 3, 3, 3, 4, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 4, 2, 1, 2, 1, 1, 1, 1, 1, 0, 0],
        [3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 4, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 0],
        [3, 3, 3, 3, 3, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

        self.oldPosition = 1

    def startPosition(self,playerDict): #this should probably be in gamesetup
        for player in playerDict.values():
            self.board[player.x][player.y] = -1
    def rollDice(self,playerDict):# decide who goes first
        rollList = []
        for player in playerDict.values():
            rollCheck = input('Press 1 to roll the dice: \n')
            if rollCheck == '1':
                roll = random.randint(1, 6)
                if roll in rollList:
                    self.rollDice(playerDict)
                else:
                     print(roll)
                     rollList.append(roll)
            else:
                print('Please press 1')
        startIndex = rollList.index(max(rollList))
        self.playerMover(startIndex,playerDict)
    def playerMover(self,turn,playerDict):
        running = True
        while running == True:
            #first player in list is asked if they want to move 
            playerDictValueList = list(playerDict.values())
            command = input('Do you wish to move Up, Down. Left or Right: \n')
            if command in ['Up', 'U','up','u']:
                self.movePieceUp(playerDictValueList[turn])
            elif command in ['Down','D','down','d']:
                self.movePieceDown(playerDictValueList[turn])
            elif command in ['Left' , 'L' , 'left' , 'l']:
                self.movePieceLeft(playerDictValueList[turn])
            elif command in ['Right' , 'R' , 'right' , 'r']:
                self.movePieceRight(playerDictValueList[turn])
            else:
                print('Enter a valid command!')
            if turn == (len(playerDictValueList)-1):
                turn = 0
            else: 
                turn =+ 1 
           # running = False
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
    def checkValidPosition(self,x,y,newX,newY,player):
        print(newX)
        print(25 < newX)
        if ((25< newX) or (newX < 0) or (25 < newY) or (newY < 0)) or (self.board[newX][newY] == 3 or self.board[newX][newY] == 4) and gamesetup.gs.playerEnterRoom == False:
            print('invalid move')
        else:
            temp = self.board[newX][newY] 
            self.board[newX][newY] = -1
            self.board[x][y] = self.oldPosition 
            self.oldPosition = temp   
            print('valid move')
            player.updateXY(newX,newY)
            if temp == 2: # ask player whether they wish to enter room,gives them an extra turn however 
                roomBool = input('Do you wish to enter room')
                if roomBool in ['Yes','Y' ,'yes','y']:
                    gamesetup.gs.playerEnterRoom = True
                    directions = [(0,1),(1,0),(-1,0),(0,-1)]
                    for d in directions:
                        if self.board[newX + d[0]][newY + d[1]] == 4:
                            print((newX + d[0]),(newY + d[1]))
                            self.checkValidPosition(newX,newY,newX + d[0],newY + d[1],player)
                            accBool = input('DO you wish to make an accusation')
                            if accBool in ['Yes','Y' ,'yes','y']:
                                self.makeAccusation()


        gamesetup.gs.playerEnterRoom = False
        print(self.board)
    def makeAccusation(self):
        print('You made an accustaion')

    # def returnPosisiton(self):
    # 	print(x,y)

gp = Gameplay()
gp.startPosition(gamesetup.gs.playersDict)
gp.rollDice(gamesetup.gs.playersDict)
print(gp.board)

#TODO
#set out of bounds limit
#move player(token?) to centre of room