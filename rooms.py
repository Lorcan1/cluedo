class Room():
    def __str__(self):
        return self.name

class Kitchen(Room):
    def __init__(self):
        self.name = 'Kitchen'
        self.entrances = [(7,4)]


class Ballroom(Room):
    def __init__(self):
        self.name = 'Ballroom'
        self.entrances = [(5,7),(8,9),(8,14),(5,16)]

class Conservatory(Room):
    def __init__(self):
        self.name = 'Conservatory'
        self.entrances = [(5,18)]

class DiningRoom(Room):
    def __init__(self):
        self.name = 'Dining Room'
        self.entrances = [(12,8),(16,6)]

class BilliardRoom(Room):
    def __init__(self):
        self.name = 'Billiard Room'
        self.entrances = [(9,17),(13,22)]

class Library(Room):
    def __init__(self):
    	self.name = 'Library'
    	self.entrances = [(16,16),(13,20)]

class Lounge(Room):
    def __init__(self):
        self.name = 'Lounge'
        self.entrances = [(18,6)]

class Hall(Room):
    def __init__(self):
        self.name = 'Hall'
        self.entrances = [(17,11),(17,12),(20,15)]

class Study(Room):
    def __init__(self):
        self.name = 'Study'
        self.entrances = [(20,17)]

class Rooms():
    def __init__(self):
        self.rooms = {}

    def createRoom(self):
        kitchenRoom = Kitchen()
        ballroomRoom = Ballroom()
        conservatoryRoom = Conservatory()
        diningRoomRoom = DiningRoom()
        billiardRoomRoom = BilliardRoom()
        libraryRoom = Library()
        loungeRoom = Lounge()
        hallRoom = Hall()
        studyRoom = Study()

        for room in [kitchenRoom,ballroomRoom,conservatoryRoom,
                     diningRoomRoom,billiardRoomRoom,libraryRoom,
                     loungeRoom,hallRoom,studyRoom]:
            self.rooms[room.name] = room
 
r = Rooms()
r.createRoom()
print(r.rooms)
