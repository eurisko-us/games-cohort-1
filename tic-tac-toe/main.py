from game import Game
from strategies.dumb_strategy import DumbStrategy
from strategies.reverse_dumb_strategy import ReverseDumbStrategy
from strategies.minimax_strategy import MinimaxStrategy
from strategies.random_strategy import RandomStrategy
import time

start = time.time()
last_log = time.time()
print("Starting")
win_counter = {
    1: 0,
    0: 0,
    -1: 0
}
games_passed = 0

# While 3 minutes haven't passed yet
strats = [RandomStrategy, MinimaxStrategy]
while time.time() - start < 3 * 60:
    games_passed += 1
    # Play games
    game = Game(strats)
    winner = game.play_game()
    win_counter[winner] += 1

    # Alternate strategies
    strats = strats[::-1]

    # Periodic logs
    if (time.time() - start) % 10 < .1:
        print("Games passed:", games_passed)

print("======")
print("Final wins after 3 minutes:")
print(win_counter)
