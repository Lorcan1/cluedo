import player
import numpy as np
import gamesetup
import random,rooms

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
        self.turnCount = 0
        self.movesMade = []

    def startPosition(self,playerDict): #this should probably be in gamesetup
        for player in playerDict.values():
            self.board[player.x][player.y] = -1
    def rollDice(self,playerDict):# decide who goes first
        rollList = []
        for player in playerDict.values():
            rollCheck = input(f'{player.name} press 1 to roll the dice!: \n')
            if rollCheck == '1':
                roll = random.randint(1, 6)
                print(f'{player.name} rolled a:',roll)
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
        playerDictValueList = list(playerDict.values())
        playerDictKeysList = list(playerDict.keys())
        print(f"{playerDictKeysList[turn]} rolled higher and therfore {playerDictKeysList[turn]} goes first")
        while running == True:
            print(f"{playerDictKeysList[turn]}'s turn")
            rollCheck = input(f'{playerDictKeysList[turn]} press 1 to roll the dice and move!: \nPress 2 to make an Accusation!: \n')
            if rollCheck == '1':
                self.turnCount = random.randint(1, 6)
                print('You rolled a:',self.turnCount)
            else:
                print('Please press 1')
            while 0 < self.turnCount:
                if playerDictValueList[turn].oldPosition == 2:
                    self.enterRoom(playerDictValueList[turn].x,playerDictValueList[turn].y,playerDictValueList[turn])
                command = input(f'Does {playerDictValueList[turn].name} wish to move Up, Down. Left or Right: \n')
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
                self.turnCount -= 1 
            self.movesMade = []
            if turn == (len(playerDictValueList)-1):
                turn = 0
            else: 
                turn =+ 1 
           # running = False
    def movePieceUp(self,selectedPlayer):
        newX = selectedPlayer.x +1
        newY = selectedPlayer.y
        self.checkValidPosition(selectedPlayer.x,selectedPlayer.y,newX,newY,selectedPlayer)
    def movePieceDown(self,selectedPlayer):
        newX = selectedPlayer.x -1
        newY = selectedPlayer.y
        self.checkValidPosition(selectedPlayer.x,selectedPlayer.y,newX,newY,selectedPlayer)
    def movePieceLeft(self,selectedPlayer):
        newX = selectedPlayer.x
        newY = selectedPlayer.y -1
        self.checkValidPosition(selectedPlayer.x,selectedPlayer.y,newX,newY,selectedPlayer)
    def movePieceRight(self,selectedPlayer):
        newX = selectedPlayer.x
        newY = selectedPlayer.y +1
        self.checkValidPosition(selectedPlayer.x,selectedPlayer.y,newX,newY,selectedPlayer)
    def checkValidPosition(self,x,y,newX,newY,selectedPlayer):
        self.movesMade.append((x,y))
        if (((25< newX) or (newX < 0) or (25 < newY) or (newY < 0)) or (self.board[newX][newY] == 3 or self.board[newX][newY] == 4) or ((newX,newY) in self.movesMade)) and gamesetup.gs.playerEnterRoom == False:
            print('invalid move')
            self.turnCount += 1
        else:
            temp = self.board[newX][newY] 
            self.board[newX][newY] = -1
            self.board[x][y] = selectedPlayer.oldPosition
            selectedPlayer.oldPosition = temp   
            print('valid move')
            selectedPlayer.updateXY(newX,newY)
            if temp == 2 and self.turnCount > 1: # ask player whether they wish to enter room,gives them an extra turn however # and diceroll has at least one left
                self.enterRoom(newX,newY,selectedPlayer)
        print(self.board)
    def enterRoom(self,newX,newY,selectedPlayer):
        roomBool = input('Do you wish to enter room: \n')
        if roomBool in ['Yes','Y' ,'yes','y']:
            gamesetup.gs.playerEnterRoom = True
            for room in list(rooms.r.rooms.values()):
                if (newX,newY) in room.entrances:
                    selectedPlayer.room = room.name
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for d in directions:
                if self.board[newX + d[0]][newY + d[1]] == 4:
                    print('yarppp')
                    self.checkValidPosition(newX,newY,newX + d[0],newY + d[1],selectedPlayer)
                   # self.centrePlayerInRoom(selectedPlayer)
                    if self.turnCount > 0: #needs to be player.turncount
                        accBool = input('Do you wish to make a suggestion: \n')
                        if accBool in ['Yes','Y' ,'yes','y']:
                            self.makeSuggestion(selectedPlayer)
            self.turnCount = 0
        gamesetup.gs.playerEnterRoom = False
    def makeSuggestion(self,selectedPlayer):
        charSelectDict = {1:'Miss Scarlett',2:'Professor Plum',3:'Mrs Peacock',
        4:'Reverend Green',5:'Colonel Mustard',6:'Dr Orchid'}
        weapSelectDict = {1:'Candle Stick',2:'Dagger',3:'Lead Pipe',
        4:'Revolver',5:'Rope',6:'Wrench'}
        print('Who is the murderer?')
        for i in charSelectDict:
            print(str(i)+'.',charSelectDict[i]) 
        suggestedMurderer = input('Choose from the list: \n')
        print('What was the murder weapon?: \n')
        for i in weapSelectDict:
            print(str(i)+'.',weapSelectDict[i])
        suggestedWeapon = input('Choose from the list: \n')
        suggestedRoom = selectedPlayer.room
        suggestedMurderer = player.p.allPlayersDict[charSelectDict[int(suggestedMurderer)]]
        self.moveSuspect(selectedPlayer,suggestedMurderer)
    def moveSuspect(self,selectedPlayer,suggestedMurderer):
        print(selectedPlayer)
        print(suggestedMurderer)
        if selectedPlayer.name == suggestedMurderer.name:
            pass
        else:
            suggestedMurderer.room = selectedPlayer.room  #room name
            self.board[suggestedMurderer.x][suggestedMurderer.y] = suggestedMurderer.oldPosition
            suggestedMurderer.x, suggestedMurderer.y =  rooms.r.rooms[suggestedMurderer.room].entrances[0][0],rooms.r.rooms[suggestedMurderer.room].entrances[0][1]
            self.board[suggestedMurderer.x][suggestedMurderer.y] = -1 
         #   self.checkValidPosition(suggestedMurderer.x,suggestedMurderer.y,suggestedMurderer.x,suggestedMurderer.y,suggestedMurderer)
          #  self.centrePlayerInRoom(suggestedMurderer)
            self.enterRoom(suggestedMurderer.x,suggestedMurderer.y,suggestedMurderer)
    # def centrePlayerInRoom(self,selectedPlayer):
    #     directions = [(0,1),(1,0),(-1,0),(0,-1)]
    #     for d in directions:
    #         for i in range(1,5):
    #             if self.board[selectedPlayer.x + d[0]][selectedPlayer.y + d[1]] == 3:
    #                # selectedPlayer.x, selectedPlayer.y = selectedPlayer.x + d[0],selectedPlayer.y + d[1]
    #                 self.board[selectedPlayer.x][selectedPlayer.y] = 4
    #                 self.board[selectedPlayer.x + d[0]][selectedPlayer.y + d[1]] = -1
    #                 selectedPlayer.x, selectedPlayer.y = selectedPlayer.x + d[0],selectedPlayer.y + d[1]
    #                 print(selectedPlayer.name,d)
    #                 break
    #             elif self.board[selectedPlayer.x + d[0]][selectedPlayer.y + d[1]] == 4:
    #                 pass
    #             elif self.board[selectedPlayer.x + d[0]][selectedPlayer.y + d[1]] == -1:
    #                 d = d*i
    #                 print(d)

        

        #ask for murderer - move to room
        #ask for weapon - move to room


    # def returnPosisiton(self):
    # 	print(x,y)

gp = Gameplay()
gp.startPosition(player.p.allPlayersDict)
gp.rollDice(gamesetup.gs.playersDict)
print(gp.board)

#TODO
#move player(token?) to centre of room
#add secret passageway
#add room name to player
#REMOVE ROOM ONCE PLAYER HAS LEFT ROOM


#Rules
#you may not move onto a space you already touched this turn
#You must be in the room that you mention in your suggestion
#if player has more than one suggestion card, they only show you one
#once player sees one card. turn is over
#if you make an an accusation and are wrong you loose

#Lessons
#PUTTING FILE NAMES IN CAPS WOULD BE EASIER TO READ

# 2 1
# 1 1 
# 2 1
# 4 1 
# 3 1

# 21 
# 11
# 21
# -11
# -11
# 41

21
11
21
-11
41
-11