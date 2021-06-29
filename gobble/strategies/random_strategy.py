import random

class RandomStrategy:
    def __init__(self, num):
        self.num = num

    def move(self, board, pieces):
        return random.choice([
            (x, y, size)
            for x in range(len(board))
            for y in range(len(board[x]))
            for size in range(1, 4)
            if pieces[self.num][size] > 0
            if board[x][y]["size"] < size
        ])
