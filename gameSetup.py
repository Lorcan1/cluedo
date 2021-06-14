import numpy as np
from player import Player

class GameState():
    def __init__(self):
      self.playersDict = {}
      self.playerEnterRoom = False

    def enterNumPlayers(self):
        numPlayers = input('Please enter the number of players: ')
        playerNum = 0
        try:
            while playerNum < int(numPlayers):
                playerSelection = input('Please Choose Your Player: \n1. Ms Scarlett\n4. Rev Green\n' )
                if playerSelection == '1':
                  scar = Player('Ms Scarlett',24,7)
                  self.playersDict['Ms Scarlett'] = scar
                  playerNum += 1 
                elif  playerSelection == '4':
                  green = Player('Rev Green',0,14)
                  self.playersDict['Rev Green'] = green
                  playerNum += 1
                else:
                  print('Please Select a Valid Character')
                print('Characters Selected:', ', '.join(self.playersDict)) #can choose the same character
        except ValueError:
            print('Please enter an integer')

gs = GameState()
gs.enterNumPlayers()