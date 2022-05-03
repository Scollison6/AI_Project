from Game import Game
from Deck import Deck


def startgame():
    game = Game()
    deck = Deck()

    game.setActive()
    game.setAcceptingPlayers()

    record = []
    player_types = []
    nums_wins = []

    numPlayers = int(input('How many players will be playing?\n'))
    i = 0
    while i < numPlayers:
        type = int(input('What type of player is #'+str(i+1)+'? 1: human, 2: linear AI, 3: learning AI, 4: Random AI\n'))
        game.addPlayer(type, '#'+str(i), i)
        player_types.append(type)
        i+=1

    wins = [0] * numPlayers
    roundsLeft = int(input('How many rounds would you like to play?'))
    while roundsLeft > 0:

        while game.getNumPlayers() > 0:

            print('Player '+game.getDealer().getName()+' is the dealer')
            deck.shuffle()
            if(game.getDealer().getType() == 0): #is the dealer human?
                input('Press \'d\' to deal the cards.\n')
            else:
                print(game.getDealer().getName()+' has dealt the cards.')
            i = 0
            while i < game.getNumPlayers():

                if game.getPlayer(i).getType() == 1:
                    print('Your card is the ' + str(deck.getCard(i).getName()))
                i = i + 1

            print(str(game.getPlayer(1).getName()) + ' goes first.')
            game.incState()
            game.editRound()
            prev = None
            actions = []
            while game.getState() < game.getNumPlayers() and game.getRound():
                if game.getPlayer(game.getState()).getType() == 1: #human player
                    print('It is your turn, player '+game.getPlayer(game.getState()).getName()+'. You have the '+str(deck.getCard(game.getState()).getName()))
                    result = input('Type \'s\' for stay, or \'t\' for trade.\n')
                elif game.getPlayer(game.getState()).getType() == 3:
                    result = game.getPlayer(game.getState()).turn(deck.getCard(game.getState()).getValue(), game.getNumPlayers(), prev, actions)
                    originalValue = deck.getCard(game.getState()).getValue()
                    qresult = result
                else:
                    result = game.getPlayer(game.getState()).turn(deck.getCard(game.getState()).getValue(), game.getNumPlayers(), prev, actions)

                actions.append(result)

                if game.getState() == 0 and game.getRound():
                    game.editRound()
                    if result == 't':
                        deck.swap(game.getState(), game.getNumPlayers())
                        print(
                            'The Dealer: ' + str(game.getDealer().getName()) + ' flips over the ' + str(
                                deck.getCard(0).getName()) + ' from the top of the deck')
                    else:
                        print(
                            'The Dealer: ' + str(game.getDealer().getName()) + ' flips over the ' + str(
                                deck.getCard(0).getName()))        
                    
                    i = 0
                    min = 14
                    index = -1
                    while i < game.getNumPlayers():
                        if deck.getCard(i).getValue() < min:
                            index = i
                            min = deck.getCard(index).getValue()
                        i = i+1
                    print('The lowest card value was ' + str(min))
                    i = 0
                    while i < game.getNumPlayers():
                        if game.getPlayer(i).getType() == 3:
                            if deck.getCard(i).getValue() == min:
                                nextState = 0
                                nextMove = 's'
                            else:
                                nextState = 13
                                nextMove = 's'
                            game.getPlayer(i).updateQValues(originalValue, qresult, nextState, nextMove,0)  # lost a quarter. bad move, bot.
                        if deck.getCard(i).getValue() == min:
                            game.getPlayer(i).subValue()
                            print(str(game.getPlayer(i).getName()) + ' lost a quarter')
                            if game.getPlayer(i).getValue() <= 0:
                                print('and is out of the game.')
                                game.removePlayer(i)
                                if game.getNumPlayers() == 1:
                                    print(str(game.getPlayer(0).getName())+ ' is the winner!')
                                    record.append(str(game.getPlayer(0).getName())+ ' is the winner!')
                                    wins[game.getPlayer(0).getIndex()] += 1
                                    game.removePlayer(0)
                                    game.setActive()
                            else:
                                print('and has '+str(game.getPlayer(i).getValue())+' coins left.')
                        else:
                            print(str(game.getPlayer(i).getName()) + ' had '+deck.getCard(i).getName()+' and has '+str(game.getPlayer(i).getValue())+' coins left.')

                        i = i+1
                    if game.getActive() == True:
                        game.nextDealer()
                    prev = None


                else:
                    if result == 't':
                        i = game.getNextState()
                        if deck.getCard(i).value == 13:
                            print(str(game.getPlayer(game.getState()).getName())+' tried to trade, but '+str(game.getPlayer(i).getName())+' flipped over a King!')

                            game.incState()

                            if game.getPlayer(game.getState()).getType() == 1:
                                print(str(game.getPlayer(game.getState()).getName()) + ' I\'m guessing you want to stay')

                            prev = None
                        else:

                            deck.swap(game.getState(),i)
                            if game.getPlayer(game.getState()).getType() == 1:
                                print('You traded with '+str(game.getPlayer(i).getName())+'. Your new card is the ' + str(
                                    deck.getCard(game.getState()).getName()))

                            if game.getPlayer(game.getNextState()).getType() == 1:
                                print(str(game.getPlayer(game.getState()).getName())+' has traded with you. Your new card is the ' + str(deck.getCard(i).getName()))
                                #print(game.getState(),game.getNextState(),game.getPlayer(game.getNextState()))
                            print((str(game.getPlayer(game.getState()).getName())+' traded'))
                            game.incState()
                            prev = deck.getCard(game.getState()).getValue()

                    else:
                        print(str(game.getPlayer(game.getState()).getName())+' stayed')
                        game.incState()
                        prev = None


                    
        print('---------------------------------')
        roundsLeft -= 1
        game.reset()
        game.setActive()
        for x in range(0, game.getNumPlayers()):
            game.getPlayer(x).reset()
            x += 1
    for y in range(0, len(wins)):
        print(wins[y])
        nums_wins.append(wins[y])

    return player_types, nums_wins, record


#startgame()
