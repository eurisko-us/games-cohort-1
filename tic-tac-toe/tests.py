from game import Game
from strategies.dumb_strategy import DumbStrategy
from strategies.reverse_dumb_strategy import ReverseDumbStrategy

# Test 1: Dumb Strategy vs Dumb Strategy
game = Game([DumbStrategy, DumbStrategy], logging=False)
winner = game.play_game()
assert winner == -1, "Dumb vs. Dumb Strategy winner test"
assert game.board == [[0, 1, 0], [1, 0, 1], [0, 1, 0]], "Dumb vs. Dumb Strategy board test"

# Test 2: Reverse Dumb Strategy vs Dumb Strategy
game = Game([ReverseDumbStrategy, DumbStrategy], logging=False)
winner = game.play_game()
assert winner == 0, "Reverse Dumb vs. Dumb Strategy winner test"
assert game.board == [[1, 1, -1], [-1, -1, -1], [0, 0, 0]], "Reverse Dumb vs. Dumb Strategy board test"

# Test 3: Reverse Dumb Strategy vs Dumb Strategy
game = Game([DumbStrategy, ReverseDumbStrategy], logging=False)
winner = game.play_game()
assert winner == 0, "Dumb vs. Reverse Dumb Strategy winner test"
assert game.board == [[0, 0, 0], [-1, -1, -1], [-1, 1, 1]], "Dumb vs. Reverse Dumb Strategy board test"

# If we get to this point, all tests have passed successfully!
print("All tests passed successfully!")
