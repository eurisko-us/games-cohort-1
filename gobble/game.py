class Game:
    # Game takes in some strategies
    def __init__(self, strategies, k, logging=False):
        # Go through the strategies and initialize them with their player num
        initialized_strategies = [strategies[0](1), strategies[1](-1)]
        self.strategies = initialized_strategies

        self.k = k
        self.current_strategy = 1
        self.turn_number = 0
        self.logging = logging

        # Board is a list of rows of each move {"player": 0, "size": 0}
        # Sizes range from 0-3:
        # 0 is none
        # 1 is small
        # 2 is medium
        # 3 is large
        self.board = [[{'player': 0, 'size': 0} for _ in range(3)] for _ in range(3)]
        self.pieces = {player: {size: k for size in range(1, 4)} for player in [1, -1]}

    # Return the strategy number who is the winner, otherwise return -1
    def test_for_winner(self):
        # Test every row, column, and diagonal for same thing.
        # But make sure it's not 0 (clear)

        # Rows (easiest one)
        for row in self.board:
            if self.is_arr_repeated(row):
                return row[0]["player"]

        # Columns (also pretty easy)
        # Transpose rows to get columns:
        columns = list(zip(*self.board))
        for column in columns:
            if self.is_arr_repeated(column):
                return column[0]["player"]

        # Top left to bottom right diagonal
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        if self.is_arr_repeated(diagonal1):
            return diagonal1[0]["player"]

        # Top right to bottom left diagonal
        diagonal2 = [self.board[2][0], self.board[1][1], self.board[0][2]]
        if self.is_arr_repeated(diagonal2):
            return diagonal2[0]["player"]

        # If current player doesn't have pieces left
        if max(x for player in self.pieces.values() for x in player.values()) == 0:
            return 0

        # If current player can't make a move
        if max(x for x in self.pieces[self.current_strategy].keys() if x != 0) <=\
            min(space["size"] for row in self.board for space in row):
            return 0

        # If no one won, return -1
        return 0

    # Return if someone won on a specific row/column/diagonal
    def is_arr_repeated(self, arr):
        return arr[0]['player'] == arr[1]['player'] == arr[2]['player'] and arr[0]['player'] != 0

    # If current player doesn't have pieces left
    # If current player can't make a move
    def check_tie(self):
        if sum(self.pieces[-self.current_strategy].values()) == 0:
            return True

        if max(x for x, v in self.pieces[-self.current_strategy].items() if v != 0) <=\
            min(space["size"] for row in self.board for space in row):
            return True
        return False

    # Let each strategy take a turn until someone wins
    def play_game(self):
        # Set winner variable for later
        winner = 0

        # Loop infinitely until...
        while True:
            # Ask strategy where it wants to move
            strat = 0 if self.current_strategy == 1 else 1
            xpos_to_move, ypos_to_move, size = self.strategies[strat].move(self.board, self.pieces)

            # Make sure strategy gives a valid position
            assert 0 <= xpos_to_move < 3
            assert 0 <= ypos_to_move < 3

            # Make sure strategy doesn't overwrite someone else's move
            assert self.board[xpos_to_move][ypos_to_move]["size"] < size

            # Make sure player actually has piece
            assert self.pieces[self.current_strategy][size] > 0

            # Actually make the move!
            self.board[xpos_to_move][ypos_to_move] = {"player": self.current_strategy, "size": size}
            self.pieces[self.current_strategy][size] -= 1

            # Check if anyone won the game
            winner = self.test_for_winner()
            if winner != 0:
                break

            # Check for a tie
            if self.check_tie():
                break

            # Increment turn number and switch to next strategy
            self.turn_number += 1
            self.current_strategy *= -1

            if self.logging:
                print("Turn", self.turn_number-1)
                self.print_board()
                print("")

        # Someone either won or tied, and the results
        # Are in the winner variable
        if self.logging:
            if winner == 0:
                print("The game was a tie!")
            else:
                print("We have a winner!!!")
                print(f"Congratulations to {type(self.strategies[winner]).__name__}!")

        # Print the board to show the monitor what happened
        self.print_board()

        # Return the winner in case we want to use the results for something
        return winner

    def print_board(self):
        # If logging is disabled, just return
        if not self.logging:
            return

        print_table = {
            0: " ",
            1: "X",
            -1: "O"
        }
        for row in range(len(self.board)):
            # Print out each element
            print(" | ".join(print_table[element] for element in self.board[row]))

            if row < 2:
                # Print out a bunch of dashes
                print("--+---+--")
