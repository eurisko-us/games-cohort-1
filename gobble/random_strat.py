import random

class RandomStrategy:

    def __init__(self):
        self.name = 'random'

    def decide_movement(self, pieces, board):
        possible_moves = []
        sizes = ['small', 'medium', 'large']
        for i in range(len(pieces)):
            if pieces[i] != 0:
                if i == 0:
                    for space in board.items():
                        if space[1] is None:
                            possible_moves.append((sizes[i], space[0]))
                else:
                    smaller = sizes[:i]
                    for space in board.items():
                        if space[1] is None or space[1] in smaller:
                            possible_moves.append((sizes[i], space[0]))
        return random.choice(possible_moves)