#!/usr/bin/python

import player
import board
import random

N_players = 100

players = []
for ii in range(N_players):
   players.append(player.player())

for i_game in range(20):
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
      while not(brd.check_if_full()) and \
            not(brd.check_if_win(1)) and \
            not(brd.check_if_win(2)):

         print "hello"

         # player 1
         if not(brd.check_if_full()):
            possible_plays = brd.possible_plays(1)
            play = players[player1].play(possible_plays)
            # convert the play board ID to a row and column value
