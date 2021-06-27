import random

class RandomStrategy:
    def __init__(self, num):
        self.num = num

    def move(self, board):
        return random.choice([(x, y)
            for x in range(len(board))
            for y in range(len(board[x]))
            if board[x][y] == 0])
