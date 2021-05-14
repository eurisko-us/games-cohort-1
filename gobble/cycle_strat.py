class CycleStrategy:

    def __init__(self):
        self.name = 'Cycle'

    def decide_movement(self, pieces, board):
        sizes = ['small', 'medium', 'large']
        for i in range(len(pieces)):
            if pieces[i] != 0:
                if i == 0:
                    for space in board.items():
                        if space[1] is None:
                            return (sizes[i], space[0])
                else:
                    smaller = sizes[:i]
                    for space in board.items():
                        if space[1] is None or space[1] in smaller:
                            return (sizes[i], space[0])
