class Game:
    # Game takes in some strategies
    def __init__(self, strategies, logging=True):
        # Go through the strategies and initialize them with their player num
        initialized_strategies = []
        for strategy_num, strategy in enumerate(strategies):
            initialized_strategies.append(strategy(strategy_num))
        self.strategies = initialized_strategies

        self.current_strategy = 0
        self.turn_number = 0
        self.logging = logging

        # Board size (rows, columns)
        self.board_size = (3, 3)

        # Board is a list of rows of each move
        # A -1 is clear, a 0 is strategy 0, a 1 is strategy 1, etc.
        self.board = [[-1 for _ in range(self.board_size[1])] for _ in range(self.board_size[0])]

    # Return the strategy number who is the winner, otherwise return -1
    def test_for_winner(self):
        # Test every row, column, and diagonal for same thing.
        # But make sure it's not -1 (clear)

        # Rows (easiest one)
        for row in self.board:
            if self.is_arr_repeated(row) and row[0] != -1:
                return row[0]

        # Columns (also pretty easy)
        # Transpose rows to get columns:
        columns = list(zip(*self.board))
        for column in columns:
            if self.is_arr_repeated(column) and column[0] != -1:
                return column[0]

        # Top left to bottom right diagonal
        diagonal1 = [
            self.board[row][column]
            for row in range(self.board_size[0])
            for column in range(self.board_size[1])
        ]
        if self.is_arr_repeated(diagonal1) and diagonal1[0] != -1:
            return diagonal1[0]

        # Top right to bottom left diagonal
        diagonal2 = [
            self.board[row][column]
            for row in range(self.board_size[0])
            for column in range(self.board_size[1]-1, -1, -1)
        ]
        if self.is_arr_repeated(diagonal2) and diagonal2[0] != -1:
            return diagonal2[0]

        # If no one won, return -1
        return -1

    # Return if all elements in array are equal
    def is_arr_repeated(self, arr):
        # "Slick" way that assumes arr has elements
        # return len(arr) == arr.count(arr[0])

        # "Simple" way that is probably slightly faster
        # Also keep in mind that this only works for arrays of length 3
        return arr[0] == arr[1] == arr[2]

    # Check if every space is filled (checks for a tie, even if there is a winner)
    def check_tie(self):
        for row in self.board:
            for element in row:
                if element == -1:
                    return False
        return True

    # Let each strategy take a turn until someone wins
    def play_game(self):
        # Set winner variable for later
        winner = -1

        # Loop infinitely until...
        while True:
            # Ask strategy where it wants to move
            xpos_to_move, ypos_to_move = self.strategies[self.current_strategy].move(self.board)

            # Make sure strategy gives a valid position
            assert 0 <= xpos_to_move < self.board_size[0]
            assert 0 <= ypos_to_move < self.board_size[1]

            # Make sure strategy doesn't overwrite someone else's move
            assert self.board[xpos_to_move][ypos_to_move] == -1

            # Actually make the move!
            self.board[xpos_to_move][ypos_to_move] = self.current_strategy

            # Check if anyone won the game
            winner = self.test_for_winner()
            if winner != -1:
                break

            # Check for a tie
            if self.check_tie():
                break

            # Increment turn number and switch to next strategy
            self.turn_number += 1
            self.current_strategy = self.turn_number % len(self.strategies)

        # Someone either won or tied, and the results
        # Are in the winner variable
        if self.logging:
            if winner == -1:
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
            0: "X",
            1: "O",
            -1: " "
        }
        for row in range(len(self.board)):
            # Print out each element
            print(" | ".join(print_table[element] for element in self.board[row]))

            if row < self.board_size[0]-1:
                # Print out a bunch of dashes
                print("--+---+--")
