#!/usr/bin/python

import player
import board
import random
import numpy as np

N_players = 2

players = []
for ii in range(N_players):
   players.append(player.player())

for i_game in range(1):
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

   # breed winners, kill losers

print brd.full()
print brd.win(1)
print brd.win(2)
print brd.board
