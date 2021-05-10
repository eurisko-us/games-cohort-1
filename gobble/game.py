class Game:
    def __init__(self, strat_1, strat_2, state = 0, k = 2):
        self.strategies = [strat_1(1), strat_2(2)]
        if state == 0:
            self.state = [[None for i in range(3)] for j in range(3)]
        else:
            self.state = state
        self.active_player = 1

    def run_game(self):
        while Game.check_for_completion(self.state) is None:
            move, strength = self.strategies[self.active_player-1].move(self.state)
            if self.state[move[0]][move[1]] is None:
                self.state[move[0]][move[1]] = (self.active_player, strength)
            elif self.state[move[0]][move[1]] < strength:
                self.state[move[0]][move[1]] = (self.active_player, strength)
            self.active_player = 1 if self.active_player == 2 else 2
        
        return Game.check_for_completion(self.state)


    @staticmethod
    def check_for_completion(state):
        #horizontal
        for row in state:
            if row.count(None) == 0:
                if row[0][0] == row[1][0] == row[2][0]:
                    return row[0][0]
        #vertical
        for i in range(3):
            if state[0][i] is not None and state[1][i] is not None and state[2][i] is not None:
                if state[0][i][0] == state[1][i][0] == state[2][i][0]:
                    return state[1][i][0]

        #diagonal
        if state[0][0] is not None and state[1][1] is not None and state[2][2] is not None and state[2][0] is not None and state[0][2] is not None:
            if state[0][0][0] == state[1][1][0] == state[2][2][0]:
                return state[0][0][0]
            elif state[0][2][0] == state[1][1][0] == state[2][0][0]:
                return state[1][1][0]
        
        #draw
        draw = True
        for i in range(3):
            for j in range(3):
                if state[i][j] is None:
                    draw = False
                    break

        if draw: return 'Draw'

        return None