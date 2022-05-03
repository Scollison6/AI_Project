import random
from Player import Player

class qLearningAgent(Player):
    def __init__(self, name, type, index):
        Player.__init__(self, name, type, index)
        
        #state is whatever you have in your hand.
        #action is either 's' or 't'.
        #nextState would be what you traded in for. is identical to state if you stayed.
        
        self.qvalues = {} #list of q values indexed by (state, action), action being either 's' or 't'
        self.qvalues[(13, 's')] = 1000
        self.qvalues[(13, 't')] = -1000
        self.qvalues[(0, 's')] = -1000
        self.qvalues[(0, 't')] = 1000
        self.alpha = 0.2
        self.discount = 0.1

    def turn(self, value, numPlayers, prevValue, actions):
        return self.computeActionFromQValues(value)


    def getQValue(self, state, action):
        if (state, action) in self.qvalues:
            #print("I found the QValue of %d %s: %d" % (state, action, self.qvalues[(state, action)]))
            return self.qvalues[(state, action)]
        else:
            #print("I could not find the value %d %s" % (state, action))
            return 0.0

    def updateQValues(self, state, action, nextState, nextAction, reward):
        print('\nUpdate:', state, action, nextState, nextAction, reward, '\n')
        curVal = self.getQValue(state, action)
        nextVal = self.computeValueFromQValues(nextState, nextAction)

        if not((state == 0 and action == 't') or (state == 13 and action == 's') or (state == 0 and action == 's') or (state == 13 and action == 't')):
            self.qvalues[(state, action)] = self.alpha * (reward + self.discount * nextVal) \
                                        + (1-self.alpha) * curVal

        print('\nQVals\n', self.qvalues, '\n')
        
    def computeActionFromQValues(self, state):
        tradeVal = self.getQValue(state, 't')
        stayVal = self.getQValue(state, 's')
        
        if (stayVal == tradeVal):
            return random.choice(['s', 't'])
        if (stayVal > tradeVal):
            return 's'
        else:
            return 't'
        
    def computeValueFromQValues(self, state, action):
        if state == 13:
            return 1000
        else:
            return -1000

        #return self.getQValue(state, action)

        # tradeVal = self.getQValue(state, action)
        # stayVal = self.getQValue(state, action)
        #
        # if (stayVal > tradeVal):
        #     return stayVal
        # else:
        #     return tradeVal
