#!/usr/bin/python

import numpy as np

class player:
   def __init__(self):
      self.weights = np.random.rand(3**9)
      self.player_num = 0
      self.win = False
      self.lose = False

   def set_player_num(self, player_num):
      self.player_num = player_num

   # returns the boardID number to play
   def play(self, playlist):
      MaxWeight = -float("Inf")

      for val in playlist:
         weight = self.weights[val]

         if weight > MaxWeight:
            MaxWeight = weight
            MaxVal = val

      return MaxVal

'''
tom = player()
'''

'''
print "play %d selection" % tom.play(np.array([4, 9, 23, 7]))
'''
