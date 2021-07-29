import rooms,gamesetup,random,canvas
from tkinter import *
from PIL import ImageTk,Image
weaponsDict = {}
weaponImgD = {}
weaponImgDict = {}

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
        self.createWeaponImages()

    def createWeaponImages(self):
        for weapon in weaponsDict.values():
            weaponImg = Image.open(weapon.name +'.png')
            weaponImgTemp = weaponImg.resize((40,40),Image.ANTIALIAS)
            weaponImg = ImageTk.PhotoImage(weaponImgTemp)
            weaponImgDict[weapon.name] = weaponImg

    def assignWeaponsToRooms(self):
        roomsList = list(rooms.r.rooms.values())
        random.shuffle(roomsList)
        counter = 0
        for weapon in weaponsDict.values():
          weapon.room = roomsList[counter].name
          counter += 1

    def centreWeaponInRoom(self,weaponImgDict):
        for weapon in weaponsDict.values():
            sizeDict = {}
           # sizeList = []
            roomEntranceRow, roomEntranceCol = self.getInsideRoomCoords(weapon)
            directions = ((0,1),(1,0),(-1,0),(0,-1))
            for d in directions:
                longestSide = 0
                selectedRow = roomEntranceRow + (d[0])
                selectedCol = roomEntranceCol + (d[1])
                for i in range(2,10):
                    if gamesetup.gs.board[selectedRow][selectedCol] == 3:
                        longestSide += 1
                        selectedRow = roomEntranceRow + (d[0]*i)
                        selectedCol = roomEntranceCol + (d[1]*i)
                    else:
                        break
                sizeDict[longestSide] = (d,roomEntranceRow,roomEntranceCol)
                longestSide = 0
            centreRow, centreCol = self.getRoomCentre(sizeDict)
            self.placeWeaponsOnBoard(centreRow,centreCol,weapon,weaponImgDict)

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

    def getRoomCentre(self,sizeDict):
        sizeList = list(sizeDict.keys())
        sizeList.sort(reverse = True)
        print(sizeList)
        longestSides = (sizeList[0],sizeList[1])
        print(longestSides)

        longestSideTuple = sizeDict[longestSides[0]],sizeDict[longestSides[1]]
        print(longestSideTuple)
        direction1, roomEntranceRow, roomEntranceCol = longestSideTuple[0]
        direction2 = longestSideTuple[1][0]
        print(direction1,roomEntranceRow,roomEntranceCol,direction2)

        if direction1 == (1,0) or direction1 == (-1,0): #row
            centreRow = roomEntranceRow + (longestSides[0]//2)*direction1[0]                 
            centreCol = roomEntranceCol + (longestSides[1]//2)*direction2[1]
        else:
            centreCol = roomEntranceCol + (longestSides[0]//2)*direction1[1]                 
            centreRow = roomEntranceRow + (longestSides[1]//2)*direction2[0]

        print(centreRow,centreCol)      
        return centreRow, centreCol

    def placeWeaponsOnBoard(self,centreRow,centreCol,weapon,weaponImgDict):
        global weaponImgD
        weaponImg = weaponImgDict[weapon.name]
        weaponImgD[weapon.name] = weaponImg
        h1,h2 = 44 + 22.92*(centreRow),44 + 22.92*(centreCol +1)
        w1,w2 = 63 + 22.91*(centreCol),63 + 22.91*(centreCol +1)
        canvas.c.canvas.create_image(w1,h1,image=weaponImg, anchor=NW)

    def moveWeapon(self,weaponName,room):
        weapon = weaponsDict[weaponName]
        weapon.room = room
        weaponImg = weaponImgDict[weaponName]
        canvas.c.canvas.delete(weaponImg)
        self.centreWeaponInRoom(weaponImgDict)

w = Weapons()
w.createWeapons()
w.assignWeaponsToRooms()