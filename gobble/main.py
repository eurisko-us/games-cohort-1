from game import Game
from strategies.minimax_strategy import MinimaxStrategy
from strategies.random_strategy import RandomStrategy
import time

start = time.time()
last_log = time.time()
print("Starting")
# Win counter is [Minimax, Random, Ties]
win_counter = [0, 0, 0]
games_passed = 0

# While 3 minutes haven't passed yet
strats = [RandomStrategy, MinimaxStrategy]
while time.time() - start < 3 * 60:
    games_passed += 1
    # Play games
    game = Game(strats, 2)
    winner = game.play_game()
    if winner == 1 and strats[0] == MinimaxStrategy or\
        winner == -1 and strats[1] == MinimaxStrategy:
        winning_strat = 0
    elif winner == 1 and strats[0] == RandomStrategy or\
        winner == -1 and strats[1] == RandomStrategy:
        winning_strat = 1
    else:
        winning_strat = 2
    win_counter[winning_strat] += 1

    # Alternate strategies
    strats = strats[::-1]

    # Periodic logs
    if time.time() - last_log > 15:
        print("Games passed:", games_passed)
        last_log = time.time()


print("======")
print("Games passed:", games_passed)
print("Win counter format: [Minimax, Random, Tie]")
print("Final wins after 3 minutes:")
print(win_counter)
print("Win percents after 3 minutes:")
print([v/games_passed for v in win_counter])
