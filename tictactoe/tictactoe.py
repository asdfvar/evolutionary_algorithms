#!/usr/bin/python

import board
import player

Board = board.board()

player1 = player.player(1)
player2 = player.player(2)

for k in range(10000):
   Board.reset()
   win = 0

   while( win == 0):
      move = player1.makePlay(Board)
      Board.play(move)
      win = Board.checkWin()
      if win != 0: continue
      move = player2.makePlay(Board)
      Board.play(move)
      win = Board.checkWin()
      if win != 0: continue

   if player1.playerNum == win:
      player1.score += 1
   if player2.playerNum == win:
      player2.score += 1

   Board.reset()
   win = 0

   while( win == 0):
      move = player2.makePlay(Board)
      Board.play(move)
      win = Board.checkWin()
      if win != 0: continue
      move = player1.makePlay(Board)
      Board.play(move)
      win = Board.checkWin()
      if win != 0: continue

   if player1.playerNum == win:
      player1.score += 1
   if player2.playerNum == win:
      player2.score += 1

   if player1.score > player2.score:
      player1.incrementPlays(0.1)
      player2.decrementPlays(0.1)
   elif player2.score > player1.score:
      player2.incrementPlays(0.1)
      player1.decrementPlays(0.1)
   else:
      player1.adjustWeights(0.01)
      player2.adjustWeights(0.01)


   player1.resetPlays()
   player2.resetPlays()
   player1.score = 0
   player2.score = 0

Board.reset()
win = 0

while( win == 0):
   move = player1.makePlay(Board)
   Board.play(move)
   win = Board.checkWin()
   print Board.board
   print
   if win != 0: continue
   move = player2.makePlay(Board)
   Board.play(move)
   win = Board.checkWin()
   print Board.board
   print
   if win != 0: continue
