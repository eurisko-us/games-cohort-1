class BoardSpace:

    def __init__(self, coords):
        self.coords = coords
        self.piece_size = None
        self.player = None
        self.chains = []

    def set_chain(self, board_dict):
        row_chain = [(self.coords[0], i) for i in range(3)]
        self.chains.append(row_chain)
        column_chain = [(i, self.coords[1]) for i in range(3)]
        self.chains.append(column_chain)
        diag_chains = [[(0,0), (1,1), (2,2)], [(2,0), (1,1), (0,2)]]
        for chain in diag_chains:
            if self.coords in chain:
                self.chains.append(chain)
        return

    def check_win(self, player, board_dict):
        for chain in self.chains:
            player_spots = [1 for space in board_dict.values() if space.coords in chain and space.player == player]
            if len(player_spots) == 3:
                return (True, player)
        return (False, player)

    def check_validity(self, piece_size):
        sizes = ['small', 'medium', 'large']
        if self.piece_size is None:
            return True
        if piece_size == 'small':
            return False
        else:
            smaller = sizes[:sizes.index(piece_size)]
            if self.piece_size in smaller:
                return True
            else:
                return False