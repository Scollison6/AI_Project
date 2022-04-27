import random
import Player

class linearRandomAgent(Player.Player):
    def turn(self, value, numPlayers, prevValue, actions):
        choice = random.randrange(0,12)
        if choice > value-1:
            return 't'
        else:
            return 's'
