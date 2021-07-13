weaponsDict = {}

class Weapon():
    def __init__(self,name):
        self.name = name
        self.room = None
        weaponsDict[name] = self

    def __str__(self):
        return self.name

class Weapons():

    def createWeapons(self):
        dagger = Weapon('Dagger')
        revolver = Weapon('Revolver')
        leadPipe = Weapon('Lead Pipe')
        wrench = Weapon('Wrench')
        candlestick = Weapon('Candlestick')
        rope = Weapon('Rope')


w = Weapons()
w.createWeapons()

#get all the weapons in a list 
#shuffle the rooms and assign them - probably in gamesetup 
#place in centre of room - probably in gameplay 

