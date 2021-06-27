class GameTree:
    def __init__(self, board, current_player):
        self.board = board
        self.current_player = current_player

        self.children = []
        winner = self.test_for_winner()
        if winner == None:
            next_player = current_player * -1
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y] != 0:
                        continue

                    self.children.append((GameTree(self.new_board(x, y), next_player), (x, y)))

            # Determine state based on children
            if current_player == -1:
                self.score = min(x[0].score for x in self.children)
            else:
                self.score = max(x[0].score for x in self.children)
        else:
            # Determine state if there's no children
            self.score = winner

    def new_board(self, x, y):
        board_copy = [row.copy() for row in self.board]
        board_copy[x][y] = self.current_player
        return board_copy

    def test_for_winner(self):
        for row in self.board:
            if self.is_arr_repeated(row):
                return row[0]
        columns = list(zip(*self.board))
        for column in columns:
            if self.is_arr_repeated(column):
                return column[0]
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        if self.is_arr_repeated(diagonal1):
            return diagonal1[0]
        diagonal2 = [self.board[2][0], self.board[1][1], self.board[0][2]]
        if self.is_arr_repeated(diagonal2):
            return diagonal2[0]
        if 0 not in [x for row in self.board for x in row]:
            return 0
        return None

    def is_arr_repeated(self, arr):
        return arr[0] == arr[1] == arr[2] and arr[0] != 0

class MinimaxStrategy:
    def __init__(self, num):
        self.num = num

    def move(self, board):
        tree = GameTree(board, self.num)
        child = max(tree.children, key=lambda x: x[0].score*self.num)
        return child[1]
