class Room():
    def __str__(self):
        return self.name

class Kitchen(Room):
    def __init__(self):
        self.name = 'Kitchen'

class Ballroom(Room):
    def __init__(self):
        self.name = 'Ballroom'

class Conservatory(Room):
    def __init__(self):
        self.name = 'Conservatory'

class DiningRoom(Room):
    def __init__(self):
        self.name = 'Dining Room'

class BilliardRoom(Room):
    def __init__(self):
        self.name = 'Billiard Room'

class Library(Room):
    def __init__(self):
    	self.name = 'Library'

class Lounge(Room):
    def __init__(self):
        self.name = 'Lounge'

class Hall(Room):
    def __init__(self):
        self.name = 'Hall'

class Study(Room):
    def __init__(self):
        self.name = 'Study'