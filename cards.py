import random
deck = {}

class Card():
    def __init__(self,name):
        self.name = name
        deck[name] = self

    def __str__(self):
        return self.name


class Cards():
    def __init__(self):
        self.cards = []

    def makeEnvelope(self):
        self.cards = list(deck.keys())
        temp = self.cards[:6]
        random.shuffle(temp)
        self.cards[:6] = temp
        murderer = self.cards[:6].pop()
        self.cards.remove(murderer)

        temp = self.cards[5:11]
        random.shuffle(temp)
        self.cards[5:11] = temp
        murderWeapon = self.cards[5:11].pop()
        self.cards.remove(murderWeapon)

        temp = self.cards[12:]
        random.shuffle(temp)
        self.cards[12:] = temp
        murderRoom = self.cards[12:].pop()
        self.cards.remove(murderRoom)

        env = Envelope()
        env.envelope.extend([murderer,murderWeapon,murderRoom])
        print(env)
        return env

    def createCard(self):
        scarlett = Card('Miss Scarlett')
        green = Card('Rev Green')
        mustard = Card('Colonel Mustard')
        plum = Card('Professor Plum')
        peacock = Card('Mrs Peacock')
        orchid = Card('Dr Orchid')
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

class Envelope():
    def __init__(self):
         self.envelope = []

    def __str__(self):
        return ' '.join(self.envelope)

c = Cards()
c.createCard()
env = c.makeEnvelope()