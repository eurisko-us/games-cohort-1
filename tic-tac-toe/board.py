from exceptions import CheaterException

class Board:
    def __init__(self):
        self.boards = [] # winner: board
        self.current_board = [[None for _ in range(3)] for _ in range(3)]
    
    def new_game(self, previous_winner):
        self.boards.append((previous_winner, self.current_board)) 
        self.current_board = [[None for _ in range(3)] for _ in range(3)]

    def __setitem__(self, position, letter):
        if self.current_board[position[0]][position[1]] is None:
            self.current_board[position[0]][position[1]] = letter
        else:
            raise CheaterException(letter)

    def __iter__(self):
        return iter(self.current_board)

    