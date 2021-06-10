import numpy as np
from player import players,Player

class GameState():
    def __init__(self):
      self.playersDict = {}

    def enterNumPlayers(self):
        numPlayers = input('Please enter the number of players: ')
     #   players = Players()
        try:
            for x in range(int(numPlayers)):
                playerSelection = input('Please Choose Your Player: \n1. Ms Scarlett\n2. Rev Green\n' )
                if playerSelection == '1':
                  scar = Player('Ms Scarlett',0,9) #not correct starting location
                  self.playersDict['Ms Scarlett'] = scar
                elif  playerSelection == '2':
                  green = Player('Rev Green',0,14)#not correct starting location
                  self.playersDict['Rev Green'] = green
                print('Characters Selected:', ', '.join(self.playersDict)) #can choose the same character
        except ValueError:
            print('Please enter an integer')

gs = GameState()
gs.enterNumPlayers()

#TODO
#Put players in starting positions and let user move player