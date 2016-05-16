import math
import board
import numpy as np

def sigmoid(arg):
   return 2.0 / (1.0 + math.exp(arg)) - 1.0

class player:
   def __init__(self, playerNum):
      self.weights = np.random.randn(3**9)
      self.plays = []
      self.playerNum = playerNum
      self.score = 0

   def resetPlays(self):
      self.plays = []

   def adjustWeights(self, nu):
      self.weights += np.random.randn(3**9) * nu

   def incrementPlays(self, nu):
      self.weights[self.plays] += abs(np.random.randn(len(self.plays))) * nu

   def decrementPlays(self, nu):
      self.weights[self.plays] -= abs(np.random.randn(len(self.plays))) * nu

   def makePlay(self, Board):
      possiblePlays = Board.getPossiblePlays(self.playerNum)
      ind = self.weights[possiblePlays].argmax()
      bestPlay = possiblePlays[ind]
      self.plays.append(bestPlay)
      return bestPlay
