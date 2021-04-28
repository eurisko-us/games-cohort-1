from game import Game
from dumb_strategy import DumbStrategy
from reverse_dumb_strategy import ReverseDumbStrategy

game = Game([DumbStrategy, ReverseDumbStrategy])
game.play_game()
