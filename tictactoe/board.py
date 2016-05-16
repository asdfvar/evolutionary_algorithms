import numpy as np

def getId(flattened):
   ID = 0
   for (k, val) in enumerate(flattened): ID += val * 3**k
   return ID

class board:
   def __init__(self):
      self.board = np.zeros(shape=(3,3), dtype=int)

   def play(self, ID):
      flat = np.zeros(9, dtype=int)
      for k in range(8,-1,-1):
         three_k = 3**k
         val = ID / three_k
         flat[k] = val
         ID -= val * three_k
      self.board = flat.reshape(3,3)

   def getPossiblePlays(self, num):
      plays = []
      flat = self.board.flatten()
      for (k, val) in enumerate(flat):
         if val == 0:
            temp = flat
            temp[k] = num
            ID = getId(temp)
            plays.append(ID)
      return plays

   def checkWin(self):
      all1 = self.board == 1
      all2 = self.board == 2
      # check the rows and columns
      for ii in range(3):
         if all1[ii][:]: return 1
         if all2[ii][:]: return 2
         if all1[:][ii]: return 1
         if all2[:][ii]: return 2
      # check the diagonals
      if all(all1.diagonal()): return 1
      if all(all2.diagonal()): return 2
      if all(np.fliplr(all1).diagonal()): return 1
      if all(np.fliplr(all2).diagonal()): return 2
      # check if the board is full
      if all(self.board) return -1
      return 0
