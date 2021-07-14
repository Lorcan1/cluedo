import rooms,gamesetup,random
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


    def assignWeaponsToRooms(self):
        roomsList = list(rooms.r.rooms.values())
        random.shuffle(roomsList)
        counter = 0
        for weapon in weaponsDict.values():
          weapon.room = roomsList[counter].name
          counter += 1

    def centreWeaponInRoom(self):
        for weapon in weaponsDict.values():
            sizeList = []
            roomEntranceRow, roomEntranceCol = self.getInsideRoomCoords(weapon)
            print(weapon.room, roomEntranceRow,roomEntranceCol)
            directions = ((0,1),(1,0),(-1,0),(0,-1))
            for d in directions:
                longestSide = 0
                selectedRow = roomEntranceRow + (d[0])
                selectedCol = roomEntranceCol + (d[1])
                for i in range(2,10):
                    if gamesetup.gs.board[selectedRow][selectedCol] == 3:
                        longestSide += 1
                        print('Longest Side' , longestSide,selectedRow,selectedCol,i)
                        selectedRow = roomEntranceRow + (d[0]*i)
                        selectedCol = roomEntranceCol + (d[1]*i)
                    else:
                        break
                sizeList.append(longestSide)
                longestSide = 0
                print('gggggggggggggggggggggggggggggggggggggggggg')
                print(weapon.room)
                print(sizeList)
                print('gggggggggggggggggggggggggggggggggggggggggg')

    def getInsideRoomCoords(self,weapon):
        roomEntranceRow, roomEntranceCol = rooms.r.rooms[weapon.room].entrances[0][0],rooms.r.rooms[weapon.room].entrances[0][1]
        directions = ((0,1),(1,0),(-1,0),(0,-1))
        for d in directions:
            sizeList = []
            longestSide = 0
            selectedRow = roomEntranceRow + (d[0])
            selectedCol = roomEntranceCol + (d[1])
            if gamesetup.gs.board[selectedRow][selectedCol] == 4:
                return selectedRow,selectedCol


w = Weapons()
w.createWeapons()
w.assignWeaponsToRooms()

#get all the weapons in a list 
#shuffle the rooms and assign them - probably in gamesetup 
#place in centre of room - probably in gameplay 

