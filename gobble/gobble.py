from board_space import BoardSpace
from player import Player

class Gobble:

    def __init__(self, k, strats):
        self.players = [Player(strat, k) for strat in strats]
        self.board = None
        self.complete = False
        self.make_board()
        self.current_player = 0
        self.winner = None
        self.last_move = None
        self.turn_count = 0

    def make_board(self):
        board = {}
        for i in range(3):
            for j in range(3):
                new_space = BoardSpace((i,j))
                board.update({(i,j) : new_space})
        for space in board.values():
            space.set_chain(board)
        self.board = board
        return

    def make_move(self):
        player = self.players[self.current_player]
        move = player.move(self.board_copy())
        space = self.board[move[1]]
        if space.check_validity(move[0]):
            space.player = player
            space.piece_size = move[0]
            self.last_move = move[1]
        else:
            print(space.check_validity(move[0]))
            print(move, player.strategy.name)
            self.make_and_print_board()
            raise Exception('INVALID MOVE DUMMY')

    def check_win(self, default = False):
        space = self.board[self.last_move]
        win = space.check_win(self.players[self.current_player], self.board)
        if default:
            new_check = self.check_after_default()
            return new_check
        if win[0] and self.winner is not None:
            if self.winner is None:
                self.winner = win[1]
                self.complete = False
            elif self.winner == win[1]:
                self.complete = True
        return

    def check_after_default(self):
        for space in self.board.values():
            for player in self.players:
                win = space.check_win(player, self.board)
                if win[0]:
                    self.winner = win[1]
                    self.complete = True
                    return True
        return False

    def board_copy(self):
        player_board = {}
        for i in range(3):
            for j in range(3):
                board_space = self.board[(i,j)]
                player_board.update({(i,j) : board_space.piece_size})
        return player_board

    def check_tie_or_default(self):
        if not self.complete:
            no_pieces = []
            for player in self.players:
                if player.pieces == [0,0,0]:
                    no_pieces.append(player)
            if len(no_pieces) == 1:
                winner = [player for player in self.players if player not in no_pieces]
                self.winner = winner[0]
                self.reason = 'NO PIECES'
                self.complete = True
            if len(no_pieces) == 2:
                self.winner = 'TIE'
                self.complete = True
            non_valids = []
            for player in self.players:
                if not player.check_valid_moves(self.board):
                    non_valids.append(player)
            if len(non_valids) == 1:
                winner = [player for player in self.players if player not in non_valids]
                self.winner = winner[0]
                self.reason = 'NO VALID MOVES'
                self.complete = True
            if len(non_valids) == 2:
                self.winner = 'TIE'
                self.complete = True

    def do_turn(self):
        self.turn_count +=1
        self.make_move()
        self.check_win()
        if self.complete:
            print(self.winner.strategy.name,'WON')
            return
        self.check_tie_or_default()
        if self.complete:
            if self.winner != 'TIE':
                something = self.check_win(default = True)
                if something:
                    print(self.winner.strategy.name,'WON')
                    return
                print(self.winner.strategy.name,'WON BY DEFAULT BECAUSE THE OTHER PLAYER HAD:', self.reason)
                return
            else:
                print('GAME ENDED IN TIE')
                return
        self.current_player += 1
        if self.current_player == 2:
            self.current_player = 0

    def make_and_print_board(self):
        board = [[None for _ in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                if self.board[(i,j)].piece_size is None:
                    board[i][j] = (self.board[(i,j)].piece_size)
                else:
                    board[i][j] = (self.board[(i,j)].piece_size, self.board[(i,j)].player.strategy.name)
        for row in board:
            print(row)
    
    def play(self):
        while not self.complete:
            self.do_turn()
        self.make_and_print_board()
        return
