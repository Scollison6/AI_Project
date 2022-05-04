# Introduction

**Screw Your Neighbor** is a popular card game. This project allows your play this game with other human or bots. There are 3 types of bots: a linear random agent, a totally random agent and a learning agent using **Q-learning**.

# How to Play

- Run `Startgame.py` to start a game, give inputs of number of players, types of players( `1: human, 2: linear AI, 3: learning AI, 4: Random AI` ) and numbers of rounds to play.

  Example:

  ```shell
  > py Startgame.py
  How many players will be playing?
  2
  What type of player is #1? 1: human, 2: linear AI, 3: learning AI, 4: Random AI
  3
  What type of player is #2? 1: human, 2: linear AI, 3: learning AI, 4: Random AI
  2
  How many rounds would you like to play?1
  ```

- Run `Records.py` allows recording the winner of each round in a game into a txt file and build a pie chart base on the winning percentage of each player. 

