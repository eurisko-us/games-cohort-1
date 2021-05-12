class Game:
    def __init__(self,strat_1,strat_2,state = 0, k = 3):
        self.strategies = [strat_1(1),strat_2(2)]
        self.pieces = [[val for val in range(1,4) for _ in range(k)] for player_num in range(2)]

        if state == 0:
            self.state = [[{'player':0,'size':0} for i in range(3)] for j in range(3)]
        else:
            self.state = state
        self.active_player = 1

    def run_game(self):
        while True:
            current_state = Game.check_for_completion(self.state,self.pieces)
            if isinstance(current_state, str):
                break

            move,size = self.strategies[self.active_player-1].move(self.state,self.pieces)
            if self.state[move[0]][move[1]]['size'] < size and size in self.pieces[self.active_player - 1]:
                self.state[move[0]][move[1]] = {'player':self.active_player, 'size':size}
                self.pieces[self.active_player-1].remove(size)
            post_move_state = Game.check_for_completion(self.state, self.pieces)
            self.active_player = 1 if self.active_player == 2 else 2

            if current_state == post_move_state and post_move_state is not None:
                break
        
        return Game.check_for_completion(self.state, self.pieces)


    @staticmethod
    def check_for_completion(state, game_pieces):
        #draw
        draw = True
                
        for i in range(3):
            for j in range(3):
                if state[i][j]['player'] == 0 and len(game_pieces[0])>0 and len(game_pieces[1])>0:
                    draw = False
                    break
        

        possible_moves = [[],[]]
        for row in state:
            for space in row:
                if space['size']==2:
                    for i in range(2):
                        if 3 in game_pieces[i]:
                            possible_moves[i].append(3)
                elif space['size']==1:
                    for i in range(2):
                        if 3 in game_pieces[i]:
                            possible_moves[i].append(3)
                        if 2 in game_pieces[i]:
                            possible_moves[i].append(2)

        if len(possible_moves[0]) > 0 and len(possible_moves[1])>0:
            draw = False
        elif len(possible_moves[0]) == 0 and len(possible_moves[1])>0:
            return '2'
        elif len(possible_moves[1]) == 0 and len(possible_moves[0])>0:
            return '1'

        if draw: return 'Draw'

        #horizontal
        for row in state:
            if row[0]['player']==row[1]['player'] and row[1]['player'] == row[2]['player'] and row[0]['player'] != 0:
                return row[0]['player']
        #vertical
        for i in range(3):
            if state[0][i]['player'] == state[1][i]['player'] and state[1][i]['player'] == state[2][i]['player'] and state[1][i]['player'] != 0:
                return state[1][i]['player']

        #diagonal
        if state[0][0]['player'] == state[1][1]['player'] and state[1][1]['player'] == state[2][2]['player'] and state[0][0]['player'] != 0:
            return state[0][0]['player']
        elif state[0][2]['player'] == state[1][1]['player'] and state[1][1]['player'] == state[2][0]['player'] and state[1][1]['player'] != 0:
            return state[1][1]['player']
        
        
        return None