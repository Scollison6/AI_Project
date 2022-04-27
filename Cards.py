class Card:
    def __init__(self, value, name, sh):
        self.name = name
        self.value = value
        self.shorthand = sh
        self.faceUp = False

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getSH(self):
        return self.shorthand

    def getFaceUp(self):
        return self.faceUp

    def flipCard(self):
        self.faceUp = not self.faceUp
