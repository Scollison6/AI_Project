from Cards import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.top = 0
        i = 0
        while i < 4:
            j = 0
            if i == 0:
                sut = 'Spades'
            elif i == 1:
                sut = 'Hearts'
            elif i == 2:
                sut = 'Diamonds'
            else:
                sut = 'Clubs'
            while j < 13:
                if j == 0:
                    val = 'Ace'
                elif j == 12:
                    val = 'King'
                elif j == 11:
                    val = 'Queen'
                elif j == 10:
                    val = 'Jack'
                else:
                    val = str(j + 1)
                card = Card(j + 1, val + ' of ' + sut,val[0]+sut[0])
                self.cards.append(card)
                j = j + 1
            i = i + 1


    def getTopCard(self):
        return self.cards[self.top]

    def dealTopCard(self):
        self.top = self.top+1
        return self.cards[self.top-1]

    def getTop(self):
        return self.top

    def getCard(self, index):
        return self.cards[index]

    def shuffle(self):
        random.shuffle(self.cards)
        self.top = 0

    def swap(self, index, i):
        tmp = self.cards[index]
        self.cards[index] = self.cards[i]
        self.cards[i] = tmp

