import numpy as np
import player
import cards
import random

class GameState():
    def __init__(self):
      self.playersDict = {}

    def enterNumPlayers(self):
        numPlayers = input('Please enter the number of players: ')
        playerNum = 0
        playerNamesDict = {'1':'Miss Scarlett', '4':'Reverend Green'}

        try:
            while playerNum < int(numPlayers):
                print('Player List:')
                for i in playerNamesDict :
                    print(i, playerNamesDict[i])
                playerSelection = input('Choose Player:\n')
                if playerSelection == '1' and playerSelection in playerNamesDict.keys():
                  scar = player.p.allPlayersDict['Miss Scarlett']
                  self.playersDict['Miss Scarlett'] = scar
                  playerNum += 1 
                  del playerNamesDict['1']
                elif  playerSelection == '4' and playerSelection in playerNamesDict.keys():
                  green = player.p.allPlayersDict['Reverend Green']
                  self.playersDict['Reverend Green'] = green
                  playerNum += 1
                  del playerNamesDict['4']
                else:
                  print('Please Select a Valid Character')
                print('Characters Selected:', ', '.join(self.playersDict)) #can choose the same character
        except ValueError:
            print('Please enter an integer')

    def dealCards(self):
        cardsToDeal = cards.c.cards
        random.shuffle(cardsToDeal)
        counter = 0
        noOfPlayers,playersList = len(list(self.playersDict.values())),list(self.playersDict.values())
        for card in cardsToDeal:
            playersList[counter].playerCards.append(card)
            if counter < (noOfPlayers-1):
                counter += 1 
            else:
                counter = 0
            print(card)

        for player in self.playersDict.values():
            print(player.showHand())


gs = GameState()
gs.enterNumPlayers()
gs.dealCards()