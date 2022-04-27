import random
from Player import Player

class qLearningAgent(Player):
    def __init__(self, name, type, index):
        Player.__init__(self, name, type, index)
        
        self.qvalues = {} #list of q values indexed by (state, action), action being either 's' or 't'
        self.alpha = 0.2
        self.discount = 0.3

    def turn(self, value, numPlayers, prevValue, actions):
        return self.computeActionFromQValues(prevValue)


    def getQValue(self, state, action):
        if (state, action) in self.qvalues:
            return self.qvalues[(state, action)]
        else:
            return 0.0

    def updateQValues(self, state, action, nextState, reward):
        curVal = self.getQValue(state, action)
        nextVal = self.computeValueFromQValues(nextState)
        
        self.qvalues[(state, action)] = self.alpha * (reward + self.discount * nextVal) \
                                        + (1-self.alpha) * curVal
        
    def computeActionFromQValues(self, state):
        tradeVal = self.getQValue(state, 't')
        stayVal = self.getQValue(state, 's')
        
        if (stayVal > tradeVal):
            return 's'
        else:
            return 't'
        
    def computeValueFromQValues(self, state):
        tradeVal = self.getQValue(state, 't')
        stayVal = self.getQValue(state, 's')
        
        if (stayVal > tradeVal):
            return stayVal
        else:
            return tradeVal
