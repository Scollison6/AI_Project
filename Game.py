from Player import Player
from linearRandomAgent import linearRandomAgent
from qLearningAgent import qLearningAgent

class Game:
    def __init__(self):
        self.active = False
        self.acceptingPlayers = False
        self.players = []
        self.resetPlayers = []
        self.state = 0
        self.round = False
        
    def reset(self):
        self.players.extend(self.resetPlayers)
        self.state = 0
        self.round = False
        self.acceptingPlayers = False

    def setActive(self):
        self.active = not self.active

    def getActive(self):
        return self.active

    def setAcceptingPlayers(self):
        self.acceptingPlayers = not self.acceptingPlayers

    def getAcceptingPlayers(self):
        return self.acceptingPlayers

    def addPlayer(self, type, name, index):
        if type == 1:
            player = Player(name, type, index)
        elif type == 2:
            player = linearRandomAgent(name, type, index)
        elif type == 3:
            player = qLearningAgent(name, type, index)
        self.players.append(player)
        self.resetPlayers.append(player)

    def removePlayer(self, index):
        self.players.remove(self.players[index])


    def getPlayer(self, index):
        return self.players[index]

    def incState(self):
        self.state = self.state + 1
        if self.state == len(self.players):
            self.state = 0

    def getState(self):
        return self.state

    def getNextState(self):
        if self.state + 1 == len(self.players):
            return 0
        else:
            return self.state +1

    def getNumPlayers(self):
        return len(self.players)

    def nextDealer(self):
        tmp = self.players[0]
        self.players.remove(self.players[0])
        self.players.append(tmp)
        
    def getDealer(self):
        return self.players[0]

    def getRound(self):
        return self.round

    def editRound(self):
        self.round = not self.round
