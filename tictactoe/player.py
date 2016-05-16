import math
import board

def sigmoid(arg):
   return 2.0 / (1.0 + math.exp(arg)) - 1.0

class player:
   def __init__(self, playerNum):
      self.weights = np.random.randn(3**9)
      self.plays = []
      self.playerNum = playerNum

   def adjustWeights(self, nu):
      self.weights += np.random.randn(3**9) * nu

   def resetPlays(self):
      self.plays = []

   def incrementPlays(self, nu):
      self.weights[self.plays] += abs(np.random.randn(len(self.plays))) * nu

   def decrementPlays(self, nu):
      self.weights[self.plays] -= abs(np.random.randn(len(self.plays))) * nu

   def makePlay(self, Board):
      possiblePlays = Board.getPossiblePlays(self.playerNum)
      bestPlay = self.weights[possiblePlays].argmax()
      return bestPlay
