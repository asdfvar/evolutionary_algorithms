#!/usr/bin/python
'''
BOARD class

play(player_num, row, col)
   player_num plays at the given row and column

boardID()
   return the boardID

check_if_full()
   returns true if the board is fully populated

check_if_win(player_num)
   returns true if player_num wins
'''

import numpy as np

class BOARD:
   def __init__(self):
      self.board = np.zeros(shape=(3,3), dtype=int)

   '''
   player_num = 1 or 2 at the given row
   and column
   '''
   def play(self, player_num, row, col):

      if row < 0 or row > 2:
         print "row must be 0, 1, or 2"
         return

      if col < 0 or col > 2:
         print "col must be 0, 1, or 2"
         return

      self.board[row, col] = player_num

   '''
   return the ID of the given board layout.
   Each layout has a unique ID.
   [  ]  [  ]  [  ]
   [  ]  [  ]  [  ]
   [  ]  [  ]  [  ]
   '''
   def boardID(self):
      ID = 0;

      for ind, el in enumerate(self.board.flatten()):
         ID += el * 3**ind

      return ID

   def check_if_full(self):
      return not(0 in self.board)

   def check_if_win(self, player_num):
      win = False

      # check by row
      win = win or all(x == player_num for x in self.board[0])
      win = win or all(x == player_num for x in self.board[1])
      win = win or all(x == player_num for x in self.board[2])

      # check by column
      win = win or all(x == player_num for x in self.board[:][0])
      win = win or all(x == player_num for x in self.board[:][1])
      win = win or all(x == player_num for x in self.board[:][2])

      # check diagonals
      win = win or (self.board[0][0] == player_num)
      win = win or (self.board[1][1] == player_num)
      win = win or (self.board[2][2] == player_num)
      win = win or (self.board[0][2] == player_num)
      win = win or (self.board[1][1] == player_num)
      win = win or (self.board[2][1] == player_num)

      return win


##########################################################
'''
testing the board class
'''

brd = BOARD()
brd.play(1,1,2)
brd.play(1,0,1)
print "is full? %r" % brd.check_if_full()
print "board ID is %d" % brd.boardID()

print "1 wins ? %r" % brd.check_if_win(1)

brd.play(1,0,0)
brd.play(1,0,1)
print "1 wins ? %r" % brd.check_if_win(1)
brd.play(1,0,2)
brd.play(2,1,0)
print "1 wins ? %r" % brd.check_if_win(1)
brd.play(2,1,1)
brd.play(2,1,2)
brd.play(1,2,0)
brd.play(1,2,1)
brd.play(1,2,2)
print "is full? %r" % brd.check_if_full()
print "board ID is %d" % brd.boardID()

print "1 wins ? %r" % brd.check_if_win(1)
