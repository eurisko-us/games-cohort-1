letters = ['x', 'o']

def check_win(board):
    horizontal = check_horizontal(board)
    vertical = check_vertical(board)
    diagonal = check_diagonal(board)
    if horizontal is not None and vertical is not None and diagonal is not None and horizontal != vertical != diagonal:
        return 'Draw'
    if horizontal is not None:
        return horizontal
    if vertical is not None:
        return vertical
    if diagonal is not None:
        return diagonal
    return None

def check_horizontal(board):
    for row in board:
        for letter in letters:
            if row.count(letter) == 3:
                return letter

def check_vertical(board):
    transposed_board = [[row[i] for row in board] for i in range(3)]
    for column in transposed_board:
        for letter in letters:
            if column.count(letter) == 3:
                return letter

def check_diagonal(board):
    diagonal = [board[index][index] for index in range(3)]
    reverse_diagonal = [board[index][- 1 - index] for index in range(3)]
    for letter in letters:
        if diagonal.count(letter) == 3 or reverse_diagonal.count(letter) == 3:
            return letter