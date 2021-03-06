#!/usr/bin/python

import player
import board
import random
import numpy as np

# mix weights from two players to make
# a new set of weights.
def mixWeights(weights1, weights2):
   nu = 0.0125
   newWeights = np.zeros(len(weights1))
   for i in range(len(weights1)):
      ZeroOrOne = np.random.randint(0,2)
      if ZeroOrOne == 0:
         weight = weights1[i]
      elif ZeroOrOne == 1:
         weight = weights2[i]
      newWeights[i] = weight
   # re-normalize the weights
   newWeights += np.random.randn(len(newWeights))*nu
   newWeights -= min(newWeights)
   newWeights /= (max(newWeights) - min(newWeights))
   return newWeights
   

N_players = 24

players = []
for ii in range(N_players):
   players.append(player.player())

for i_game in range(100):
   print "\n\nRound %d" % i_game
   random.shuffle(players)

   # have each compete
   for i_player in range(0,len(players), 2):
      player1 = i_player
      player2 = i_player+1

      # define the players
      players[player1].set_player_num(1)
      players[player2].set_player_num(2)

      # define the board
      brd = board.BOARD()

      # start competition
      while not(brd.full()) and \
            not(brd.win(1)) and \
            not(brd.win(2)):

         # player 1
         if not(brd.full()) and \
            not(brd.win(1)) and \
            not(brd.win(2)):

            possible_plays = brd.possible_plays(1)

            # select the best play of all the possible plays
            play = players[player1].play(possible_plays)
            brd.play2(play)

         # player 2
         if not(brd.full()) and \
            not(brd.win(1)) and \
            not(brd.win(2)):

            possible_plays = brd.possible_plays(2)

            # select the best play of all the possible plays
            play = players[player2].play(possible_plays)
            brd.play2(play)

      if brd.win(1):
         print "player 1 wins"
         players[player1].win  = True
         players[player2].lose = True
      elif brd.win(2):
         print "player 2 wins"
         players[player1].lose = True
         players[player2].win  = True
      else:
         print "DRAW"
      print brd.board

   # kill losers and breed winners
   Losers = []
   Winners = []
   for i in range(len(players)-1,-1,-1):
      if players[i].lose == True:
         Losers.append(players.pop(i))
      elif players[i].win == True:
         Winners.append(players[i])

   # reset winners
   for i_player,plyr in enumerate(players):
      players[i_player].win = False
      players[i_player].lose = False

   for i in range(len(Winners)):
      Winners[i].win = False
      Winners[i].lose = False

   for i in range(len(Losers)):
      Losers[i].win = False
      Losers[i].lose = False

   while len(players) < N_players:
      winner1 = random.choice(Winners)
      winner2 = random.choice(Winners)
      newPlayer = player.player()
      newPlayer.weights = mixWeights(winner1.weights, winner2.weights)
      players.append(newPlayer)
