class GameTree:
    def __init__(self, board, pieces, current_player, player, max_depth=None):
        self.board = board
        self.pieces = pieces
        self.current_player = current_player
        self.player = player

        self.children = []
        winner = self.test_for_winner()

        if max_depth == None:
            new_max_depth = None
        else:
            new_max_depth = max_depth - 1

        if winner == None and (max_depth != 0 or max_depth is None):
            next_player = current_player * -1
            for x in range(len(board)):
                for y in range(len(board[x])):
                    for piece_size in range(1, 4):
                        # If player doesn't have piece or piece is too small, continue
                        if pieces[current_player][piece_size] <= 0 or board[x][y]["size"] >= piece_size:
                            continue

                        self.children.append((
                            GameTree(self.new_board(x, y, piece_size), self.new_pieces(piece_size), next_player, player, new_max_depth),
                            (x, y, piece_size)
                        ))

            # Determine state based on children
            if current_player != player:
                self.score = min(x[0].score for x in self.children)
            else:
                self.score = max(x[0].score for x in self.children)
        else:
            # Determine state if there's no children
            self.score = self.get_heuristic()

    def new_board(self, x, y, size):
        board_copy = [[space.copy() for space in row] for row in self.board]
        board_copy[x][y] = {'player': self.current_player, 'size': size}
        return board_copy

    def new_pieces(self, piece_size):
        new_pieces = {k: v.copy() for k, v in self.pieces.items()}
        new_pieces[self.current_player][piece_size] -= 1
        return new_pieces

    def row_to_players(self, row):
        return [x["player"] for x in row]

    def row_heuristic(self, row):
        if row.count(self.player) == 2:
            return 10
        elif row.count(self.player) == 3:
            return 100
        elif row.count(-self.player) == 2:
            return -10
        elif row.count(-self.player) == 3:
            return -100
        return 0

    def get_heuristic(self):
        score = 0
        for row in self.board:
            score += self.row_heuristic(self.row_to_players(row))
        columns = list(zip(*self.board))
        for column in columns:
            score += self.row_heuristic(self.row_to_players(column))
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        score += self.row_heuristic(self.row_to_players(diagonal1))
        diagonal2 = [self.board[2][0], self.board[1][1], self.board[0][2]]
        score += self.row_heuristic(self.row_to_players(diagonal2))
        return score

    def test_for_winner(self):
        for row in self.board:
            if self.is_arr_repeated(row):
                return row[0]["player"]
        columns = list(zip(*self.board))
        for column in columns:
            if self.is_arr_repeated(column):
                return column[0]["player"]
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        if self.is_arr_repeated(diagonal1):
            return diagonal1[0]["player"]
        diagonal2 = [self.board[2][0], self.board[1][1], self.board[0][2]]
        if self.is_arr_repeated(diagonal2):
            return diagonal2[0]["player"]
        if max(x for player in self.pieces.values() for x in player.values()) == 0:
            return 0
        if max(x for x, v in self.pieces[self.current_player].items() if v != 0) <=\
            min(space["size"] for row in self.board for space in row):
            return 0
        return None

    def is_arr_repeated(self, arr):
        return arr[0]['player'] == arr[1]['player'] == arr[2]['player'] and arr[0]['player'] != 0

    def get_length(self):
        return sum(c[0].get_length() for c in self.children) + 1

class MinimaxStrategy:
    def __init__(self, num):
        self.num = num

    def move(self, board, pieces):
        tree = GameTree(board, pieces, self.num, self.num, 1)
        child = max(tree.children, key=lambda x: x[0].score)
        return child[1]

# if __name__ == "__main__":
#     import time
#     start = time.time()
#     board = [
#         [{"player": 0, "size": 0}, {"player": 0, "size": 0},{"player": 1, "size": 1}],
#         [{"player": 1, "size": 1}, {"player": 1, "size": 1},{"player":-1, "size": 1}],
#         [{"player":-1, "size": 1}, {"player": 1, "size": 1},{"player":-1, "size": 1}]
#     ]
#     k = 2
#     pieces = {
#         1:  {1: 2, 2: 0, 3: 0},
#         -1: {1: 2, 2: 0, 3: 0}
#     }
#     n = 1
#     tree = GameTree(board, pieces, 1, 1, n)
#     time_taken = time.time() - start
#     print("Time taken to construct a full game tree:", time_taken)
#     print("Amount of nodes in game tree:", tree.get_length())
#     print("Finished")
