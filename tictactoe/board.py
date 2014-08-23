#!/usr/bin/python
'''
BOARD class

play(player_num, row, col)
   player_num plays at the given row and column

play2(boardID)
   same as play but the board is updated by passing the
   board ID

boardID()
   return the boardID

full()
   returns true if the board is fully populated

win(player_num)
   returns true if player_num wins

possible_plays(self, player_num)
   returns a list of the possible plays by their board ID
'''

import numpy as np

def boardID_to_board(boardID):
    board = np.zeros(shape=(3,3), dtype=int)
    for k in range(8, -1, -1):
       while boardID >= 3**k:
          board[k/3][k%3] += 1
          boardID -= 3**k
    return board

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

   def play2(self, boardID):
      self.board = boardID_to_board(boardID)

   '''
   return the ID of the given board layout.
   Each layout has a unique ID.
   [  ]  [  ]  [  ]
   [  ]  [  ]  [  ]
   [  ]  [  ]  [  ]

   there are a total of 3**9 = 19683 possible
   configurations. Not all of them are possible
   obtain.
   '''
   def boardID(self):
      ID = 0;

      for ind, el in enumerate(self.board.flatten()):
         ID += el * 3**ind

      return ID

   def full(self):
      return not(0 in self.board)

   def win(self, player_num):
      win = False

      # check by row
      win = win or all(x == player_num for x in self.board[0])
      win = win or all(x == player_num for x in self.board[1])
      win = win or all(x == player_num for x in self.board[2])

      # check by column
      win = win or all(x == player_num for x in self.board[:,0])
      win = win or all(x == player_num for x in self.board[:,1])
      win = win or all(x == player_num for x in self.board[:,2])

      # check diagonals
      win = win or ((self.board[0][0] == player_num) \
               and (self.board[1][1] == player_num) \
               and (self.board[2][2] == player_num))
      win = win or ((self.board[0][2] == player_num) \
               and (self.board[1][1] == player_num) \
               and (self.board[2][0] == player_num))

      return win

   def possible_plays(self, player_num):

      play = []

      for ii in range(3):
         for jj in range(3):
            if self.board[ii][jj] == 0:
               self.board[ii][jj] = player_num
               play.append(self.boardID())
               self.board[ii][jj] = 0

      return play


##########################################################
'''
testing the board class
'''

'''
brd = BOARD()
brd.play(1,1,2)
brd.play(1,0,1)
print "is full? %r" % brd.full()
print "board ID is %d" % brd.boardID()

print "1 wins ? %r" % brd.win(1)

brd.play(1,0,0)
print "board ID is %d" % brd.boardID()
brd.play(1,0,1)
print "1 wins ? %r" % brd.win(1)
brd.play(1,0,2)
brd.play(2,1,0)
print "1 wins ? %r" % brd.win(1)
brd.play(2,1,1)
brd.play(2,1,2)
print brd.possible_plays(1)
brd.play(1,2,0)
brd.play(1,2,1)
brd.play(1,2,2)
print "is full? %r" % brd.full()
print "board ID is %d" % brd.boardID()

print "1 wins ? %r" % brd.win(1)
'''
