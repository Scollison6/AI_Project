import matplotlib.pyplot as plt
from Neighbor import startgame

def save_records():
    records = startgame()
    players = []
    for type in records[0]:
      if type == 4:
        players.append('Random')
      elif type == 1:
        players.append('Human')
      elif type == 2:
        players.append('linear')
      elif type == 3:
        players.append('QLearning')

    with open((' vs '.join(players)) + '.txt', 'w') as f:
      f.write((' vs '.join(players)) + '. Total ' + str(len(records[2])) + ' rounds.\n')
      for result in records[2]:
        f.write(result)
        f.write('\n')


    explode = [0] * len(players)
    max_index = records[1].index(max(records[1]))
    explode[max_index] = 0.08

    fig, ax = plt.subplots()
    ax.pie(records[1], labels = players, 
          autopct = lambda p:f'{p:.2f}%, {p*sum(records[1])/100 :.0f} wins',
          explode = explode, 
          shadow = True)

    ax.set_title('Winning percentages')
    
    plt.savefig((' vs '.join(players)) + '.png')

save_records()