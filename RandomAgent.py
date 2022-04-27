import random
import Player

class RandomAgent(Player.Player):
    def turn(self, value, numPlayers, prevValue, actions):
        actions = ['t', 's']
        return random.choice(actions)