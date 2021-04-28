from game import Game
from strategies.dumb_strategy import DumbStrategy
from strategies.reverse_dumb_strategy import ReverseDumbStrategy

game = Game([ReverseDumbStrategy, DumbStrategy])
game.play_game()
