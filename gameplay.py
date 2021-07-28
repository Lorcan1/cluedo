import player
import numpy as np
import gamesetup
import random,rooms,cards,canvas,weapons
# from weapons import weaponsDict

class Gameplay:
    def __init__(self):
    # This array "squareType" stores what kind of square each square on the board is, which determines if it can be accessed by counters
     # Squares that are marked 0 are inaccessible by the player (they are out of bounds)
     # Squares that are marked 1 are pathways that the player can walk on
     # Sqaures that are marked 2 are pathway squares that are adjacent to room entrances - this is needed so we can exit rooms easily
     # Sqaures that are marked 3 are squares inside rooms - they cannot be accessed directly
     # Sqaures that are marked 4 are room squares that are adjacent to room entrances
     # All negative squares are occupied by another user (e.g. -1 is an occupied pathway square
        # gui2 = gui.Gui()
        self.turnCount = 0
        self.movesMade = []

    def startPosition(self,playerDict): #this should probably be in gamesetup
        for player in playerDict.values():
            gamesetup.gs.board[player.x][player.y] = -1
    def rollDice(self,playerDict):# decide who goes first
        rollList = []
        for player in playerDict.values():
            rollCheck = input(f'{player.name} press 1 to roll the dice!: \n')
            if rollCheck == '1':
                roll = random.randint(1, 6)
                print(f'{player.name} rolled a:',roll)
                canvas.c.updateWidget((f'{player.name} rolled a:',roll))
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
        canvas.c.updateWidget((f"{playerDictKeysList[turn]} rolled higher and therfore {playerDictKeysList[turn]} goes first"))
        while running == True:
            print(f"{playerDictKeysList[turn]}'s turn")
            rollCheck = input(f'{playerDictKeysList[turn]} press 1 to roll the dice and move!: \nPress 2 to make an Accusation!: \n')
            if rollCheck == '1':
                self.turnCount = random.randint(1, 6)
                print('You rolled a:',self.turnCount)
                while 0 < self.turnCount:
                    if playerDictValueList[turn].oldPosition == 2: #ask if they wanted to enter room if they finised last turn on an entrance
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
               # gui.gui.placePlayersOnBoard()
            elif rollCheck == '2':
                accusation = self.makeSuggestion(playerDictValueList[turn],1)
                counter = 0
                for i in range(len(accusation)):
                    if accusation[i] == cards.env.envelope[i]:
                        counter += 1 
                if counter == 3: 
                    print('You win')
                else: #player must be removed from game 
                    print('You lose')


           # running = False
    def movePieceUp(self,selectedPlayer):
        newX = selectedPlayer.x +1
        newY = selectedPlayer.y
        if self.checkValidPosition(selectedPlayer.x,selectedPlayer.y,newX,newY,selectedPlayer) != False:
            canvas.c.updateWidget((f'{selectedPlayer.name} moved up to:',selectedPlayer.x,selectedPlayer.y))
        player.p.movePlayerOnBoard(selectedPlayer)
    def movePieceDown(self,selectedPlayer):
        newX = selectedPlayer.x -1
        newY = selectedPlayer.y
        if self.checkValidPosition(selectedPlayer.x,selectedPlayer.y,newX,newY,selectedPlayer) != False:
            canvas.c.updateWidget((f'{selectedPlayer.name} moved down to:',selectedPlayer.x,selectedPlayer.y))
        player.p.movePlayerOnBoard(selectedPlayer)
    def movePieceLeft(self,selectedPlayer):
        newX = selectedPlayer.x
        newY = selectedPlayer.y -1
        self.checkValidPosition(selectedPlayer.x,selectedPlayer.y,newX,newY,selectedPlayer)
        player.p.movePlayerOnBoard(selectedPlayer)
    def movePieceRight(self,selectedPlayer):
        newX = selectedPlayer.x
        newY = selectedPlayer.y +1
        self.checkValidPosition(selectedPlayer.x,selectedPlayer.y,newX,newY,selectedPlayer)
        player.p.movePlayerOnBoard(selectedPlayer)
    def checkValidPosition(self,x,y,newX,newY,selectedPlayer):
        self.movesMade.append((x,y))
        if selectedPlayer.inRoom == True:
            newX,newY = self.leaveRoom(selectedPlayer)
        if (((25< newX) or (newX < 0) or (25 < newY) or (newY < 0)) or gamesetup.gs.board[newX][newY] in [-1,0,3,4] or ((newX,newY) in self.movesMade)):
            print('invalid move')
            self.turnCount += 1
            return False
        else:
            temp = gamesetup.gs.board[newX][newY] 
            gamesetup.gs.board[newX][newY] = -1
            gamesetup.gs.board[x][y] = selectedPlayer.oldPosition
            selectedPlayer.oldPosition = temp   
            print('valid move')
            selectedPlayer.updateXY(newX,newY)
            if temp == 2 and self.turnCount > 1: # ask player whether they wish to enter room,gives them an extra turn however # and diceroll has at least one left
                self.enterRoom(newX,newY,selectedPlayer)
        print(gamesetup.gs.board)
    def enterRoom(self,newX,newY,selectedPlayer,isSuspect=False):
        if isSuspect is False:
            roomBool = input('Do you wish to enter room: \n')
        else:
            roomBool = 'Yes'
        if roomBool in ['Yes','Y' ,'yes','y']:
            selectedPlayer.inRoom = True
            for room in list(rooms.r.rooms.values()):
                if (newX,newY) in room.entrances:
                    selectedPlayer.room = room.name
                    self.movePlayerIntoRoom(selectedPlayer)
                    if self.turnCount > 0 and isSuspect is False: #needs to be player.turncount
                        accBool = input('Do you wish to make a suggestion: \n')
                        if accBool in ['Yes','Y' ,'yes','y']:
                            self.makeSuggestion(selectedPlayer)
            self.turnCount = 0
    def movePlayerIntoRoom(self,selectedPlayer):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for d in directions:
            if gamesetup.gs.board[selectedPlayer.x + d[0]][selectedPlayer.y + d[1]] == 4:
                temp = gamesetup.gs.board[selectedPlayer.x][selectedPlayer.y] 
                gamesetup.gs.board[selectedPlayer.x + d[0]][selectedPlayer.y + d[1]] = -1
                gamesetup.gs.board[selectedPlayer.x][selectedPlayer.y] = selectedPlayer.oldPosition
                selectedPlayer.oldPosition = temp
                selectedPlayer.x = selectedPlayer.x + d[0]
                selectedPlayer.y = selectedPlayer.y + d[1]
                player.p.movePlayerOnBoard(selectedPlayer)
                self.centrePlayerInRoom(selectedPlayer)
                print(gamesetup.gs.board)

    def leaveRoom(self,selectedPlayer):
        newX,newY = rooms.r.rooms[selectedPlayer.room].entrances[0][0], rooms.r.rooms[selectedPlayer.room].entrances[0][1]
        selectedPlayer.inRoom = False
        selectedPlayer.room = ()
        return newX,newY

    def makeSuggestion(self,selectedPlayer,isSuggestion=0):
        charSelectDict = {1:'Miss Scarlett',2:'Professor Plum',3:'Mrs Peacock',
        4:'Reverend Green',5:'Colonel Mustard',6:'Dr Orchid'}
        weapSelectDict = {1:'Candlestick',2:'Dagger',3:'Lead Pipe',
        4:'Revolver',5:'Rope',6:'Wrench'}
        print('Who is the murderer?')
        for i in charSelectDict:
            print(str(i)+'.',charSelectDict[i]) 
        suggestedMurderer = input('Choose from the list: \n')
        print('What was the murder weapon?: \n')
        for i in weapSelectDict:
            print(str(i)+'.',weapSelectDict[i])
        suggestedWeapon = input('Choose from the list: \n')
        suggestedMurderer = charSelectDict[int(suggestedMurderer)]
        suggestedWeapon = weapSelectDict[int(suggestedWeapon)]
        suggestedMurdererCharacter = player.p.allPlayersDict[suggestedMurderer] #needs the player object to be moved as opposed to a string name
        self.moveSuspect(selectedPlayer,suggestedMurdererCharacter)
        weapons.w.moveWeapon(suggestedWeapon,selectedPlayer.room)
        if isSuggestion == 1:
            roomSelectDict = {1:'Kitchen',2:'Ballroom',3:'Conservatory',
            4:'Dining Room',5:'Billiard Room',6:'Library',7:'Lounge',8:'Hall',9:'Study'}
            for i in roomSelectDict:
                print(str(i)+'.',roomSelectDict[i])
            suggestedRoom = input('Choose from the list: \n')
            suggestedRoom = roomSelectDict[int(suggestedRoom)]
            accusation = (suggestedMurderer,suggestedWeapon,suggestedRoom)
            return accusation
        else:
            suggestedRoom = selectedPlayer.room
            suggestion = (suggestedMurderer,suggestedWeapon,suggestedRoom)
            self.checkCards(selectedPlayer,suggestion)
    def moveSuspect(self,selectedPlayer,suggestedMurderer):
        print(selectedPlayer)
        print(suggestedMurderer)
        if selectedPlayer.name == suggestedMurderer.name:
            pass
        else:
            suggestedMurderer.room = selectedPlayer.room  #room name
            gamesetup.gs.board[suggestedMurderer.x][suggestedMurderer.y] = suggestedMurderer.oldPosition
            suggestedMurderer.x, suggestedMurderer.y =  rooms.r.rooms[suggestedMurderer.room].entrances[0][0],rooms.r.rooms[suggestedMurderer.room].entrances[0][1]
            gamesetup.gs.board[suggestedMurderer.x][suggestedMurderer.y] = -1 
         #   self.checkValidPosition(suggestedMurderer.x,suggestedMurderer.y,suggestedMurderer.x,suggestedMurderer.y,suggestedMurderer)
          #  self.centrePlayerInRoom(suggestedMurderer)
            suggestedMurderer.oldPosition = 2
            self.enterRoom(suggestedMurderer.x,suggestedMurderer.y,suggestedMurderer,True)
    def centrePlayerInRoom(self,selectedPlayer):
        directions = ((0,1),(1,0),(-1,0),(0,-1))
        playerRow = selectedPlayer.x
        playerCol = selectedPlayer.y
        selectedPlayer.oldPosition = 4 #this needs to be changed

        for d in directions:
            playerRow = selectedPlayer.x
            playerCol = selectedPlayer.y
            playerRow = playerRow + (d[0])
            playerCol = playerCol + (d[1])
            for i in range(1,5):
                if gamesetup.gs.board[playerRow][playerCol] == 1:
                    print(playerRow,playerCol)
                    print('break')
                    break
                elif gamesetup.gs.board[playerRow][playerCol] == 3:
                    print('yyyyyyy')
                    print(playerRow,playerCol)
                    print('yyyyyyy')
                    temp = gamesetup.gs.board[playerRow][playerCol] 
                    gamesetup.gs.board[playerRow][playerCol] = -1
                    gamesetup.gs.board[selectedPlayer.x][selectedPlayer.y] = selectedPlayer.oldPosition
                    selectedPlayer.x, selectedPlayer.y = playerRow,playerCol
                    print('return')
                    selectedPlayer.oldPosition = temp
                    player.p.movePlayerOnBoard(selectedPlayer)
                    return
                else:
                    playerRow = playerRow + (d[0]*i)
                    playerCol = playerCol + (d[1]*i)
                    print('zzzzzzzzzzzz')
                    print(d,i)
                    print('zzzzzzzzzzzz')
                    print(gamesetup.gs.board[playerRow][playerCol])
                     #kind of working for moving player, but its starting on the 2 
                    #instead of the 4 and changing it to 1 (because olPosition is one
                    #but its leaving its orginal position ok so its the second old position)

     

   # This function checks the players suggestion against other players cards
    def checkCards(self,selectedPlayer,suggestion): #NEEDS TO BE TESTED FOR THREE PLAYERS IE DOES IT STOP IF PLAYER HAS A CARD
        cards = []
        returnedCard = False
        for pName in gamesetup.gs.playersDict:
            if pName != selectedPlayer.name and returnedCard == False: #iterate players apart from player whos turn it is
                for card in gamesetup.gs.playersDict[pName].playerCards: 
                    for s in suggestion:
                        if card == s: 
                            cards.append(card)
                            returnedCard = True
        if len(cards) is not 0: #if player has more than one card, display a random one 
            print(random.choice(cards))

        #ask for murderer - move to room
        #ask for weapon - move to room


    # def returnPosisiton(self):
    # 	print(x,y)

gp = Gameplay()





# gp.startPosition(player.p.allPlayersDict)
# print('hiiiiiirngoerngoeni')
# gp.rollDice(gamesetup.gs.playersDict)
# print(gp.board)


#TODO
#move player(token?) to centre of room
#add secret passageway
#add room name to player
  #REMOVE ROOM ONCE PLAYER HAS LEFT ROOM
#make player object same in allPlayersDict and PlayersDict - easier fix to this
#players coordinates are updated even when move is invalid
#line 122 needs to be removed in gameplay, need a board class 


#Rules
#you may not move onto a space you already touched this turn
#You must be in the room that you mention in your suggestion
#if player has more than one suggestion card, they only show you one
#once player sees one card. turn is over
#if you make an an accusation and are wrong you loose

#Lessons
#PUTTING FILE NAMES IN CAPS WOULD BE EASIER TO READ
#COMMENT MORE
#FIX SUBLIME