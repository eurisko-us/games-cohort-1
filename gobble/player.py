class Player:

    def __init__(self, strategy, k):
        self.strategy = strategy
        self.name = strategy.name
        self.pieces = [k for i in range(3)]

    def move(self, board):
        sizes = ['small', 'medium', 'large']
        move = self.strategy.decide_movement(self.pieces, board)
        self.pieces[sizes.index(move[0])] -= 1
        return move

    def check_valid_moves(self, board):
        sizes = ['small', 'medium', 'large']
        indices = [self.pieces.index(amount) for amount in self.pieces if amount != 0]
        if len(indices) == 3:
            for space in board.values():
                if space.player is None:
                    return True
                if space.piece_size == 'small' or space.piece_size == 'medium':
                    return True
            return False
        for index in indices:
            smaller_sizes = sizes[:index]
            for space in board.values():
                if space.piece_size in smaller_sizes or space.player is None:
                    return True
        return False