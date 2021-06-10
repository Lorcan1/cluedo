import random
deck = {}

class Card():
    def __init__(self,name):
        self.name = name
        deck[name] = self

    def __str__(self):
        return self.name


class Cards():
    def envelope(self):
        cards = list(deck.keys())
        temp = cards[:6]
        random.shuffle(temp)
        cards[:6] = temp

        temp = cards[6:12]
        random.shuffle(temp)
        cards[6:12] = temp

        temp = cards[12:]
        random.shuffle(temp)
        cards[12:] = tem0p

    def createCard(self):
        scarlett = Card('Miss Scarlett')
        green = Card('Rev Green')
        mustard = Card('Mustard')
        plum = Card('Professor Plum')
        peacock = Card('Mrs Peacock')
        white = Card('Mrs White')
        candleStick = Card('Candle Stick')
        dagger = Card('Dagger')
        leadPipe = Card('Lead Pipe')
        revolver = Card('Revolver')
        rope = Card('Rope')
        wrench = Card('Wrench')
        kitchen = Card('Kitchen')
        ballroom = Card('Ballroom')
        conservatory = Card('Conservatory')
        diningRoom = Card('Dining Room')
        billiardRoom = Card('Billiard Room')
        library = Card('Library')
        lounge = Card('Lounge')
        hall = Card('Hall')
        study = Card('Study')


c = Cards()
c.createCard()