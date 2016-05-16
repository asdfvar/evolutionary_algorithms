import board
import player

Board = board.board()

player1 = player.player(1)
player2 = player.player(2)

win = Board.checkWin()
while( win == 0):
   move = player1.makePlay(Board)
   Board.play(move)
   win = Board.checkWin()
   if win > 0: continue
   if win < 0: break
