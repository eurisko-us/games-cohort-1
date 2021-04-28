class ReverseDumbStrategy:
    def __init__(self, num):
        self.player_num = num

    # Choose the last available position by looping backwards
    def move(self, board):
        for row in range(2, -1, -1):
            for column in range(2, -1, -1):
                if board[row][column] == -1:
                    return (row, column)
        # There should never be an error here
        # Because move isn't called if there was a tie
