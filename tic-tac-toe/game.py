class Game:
    def __init__(self,strat_1,strat_2):
        self.strategies = [strat_1(1),strat_2(2)]
        self.state = [[0 for i in range(3)] for j in range(3)]
        self.active_player = 1

    def run_game(self):
        while Game.check_for_completion(self.state) is None:
            move = self.strategies[self.active_player-1].move(self.state)
            self.state[move[0]][move[1]] = self.active_player
            self.active_player = 1 if self.active_player == 2 else 2
        
        return Game.check_for_completion(self.state)


    @staticmethod
    def check_for_completion(state):
        #horizontal
        for row in state:
            if row[0]==row[1] and row[1] == row[2] and row[0] != 0:
                return row[0]
        #vertical
        for i in range(3):
            if state[0][i] == state[1][i] and state[1][i] == state[2][i] and state[1][i] != 0:
                return state[1][i]

        #diagonal
        if state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[0][0] != 0:
            return state[0][0]
        elif state[0][2] == state[1][1] and state[1][1] == state[2][0] and state[1][1] != 0:
            return state[1][1]
        
        #draw
        draw = True
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    draw = False
                    break

        if draw: return 'Draw'

        return None