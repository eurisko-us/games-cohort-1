class DumbStrategy:
    def __init__(self, num):
        self.player_num = num

    # Choose the first available position
    def move(self, board):
        for row in range(3):
            for column in range(3):
                if board[row][column] == -1:
                    return (row, column)
        # There should never be an error here
        # Because move isn't called if there was a tie
