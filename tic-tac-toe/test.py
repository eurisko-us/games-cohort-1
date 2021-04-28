from game import Game
from strategy import Strategy
from strategy import MinimaxStrategy

ttt = Game(Strategy,MinimaxStrategy)

print(ttt.run_game())