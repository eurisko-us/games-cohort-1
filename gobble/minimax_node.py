from game import Game
class Node:
    def __init__(self,state,pieces,parent,move,depth):
        self.state = state
        self.pieces = pieces
        self.parent = parent
        self.difference = move
        self.depth = depth
        self.value = None
        self.terminal = self.check_terminality()
        self.children = []

    def check_terminality(self):
        #draw
                
        for i in range(3):
            for j in range(3):
                if self.state[i][j]['player'] == 0 and len(self.pieces[0])>0 and len(self.pieces[1])>0:
                    return False
        

        possible_moves = [[],[]]
        for row in self.state:
            for space in row:
                if space['size']==2:
                    for i in range(2):
                        if 3 in self.pieces[i]:
                            possible_moves[i].append(3)
                elif space['size']==1:
                    for i in range(2):
                        if 3 in self.pieces[i]:
                            possible_moves[i].append(3)
                        if 2 in self.pieces[i]:
                            possible_moves[i].append(2)

        if len(possible_moves[0]) == 0 or len(possible_moves[1]) == 0:
            return True



        #horizontal
        for row in self.state:
            if row[0]['player']==row[1]['player'] and row[1]['player'] == row[2]['player'] and row[0]['player'] != 0:
                return True
        #vertical
        for i in range(3):
            if self.state[0][i]['player'] == self.state[1][i]['player'] and self.state[1][i]['player'] == self.state[2][i]['player'] and self.state[1][i]['player'] != 0:
                return True

        #diagonal
        if self.state[0][0]['player'] == self.state[1][1]['player'] and self.state[1][1]['player'] == self.state[2][2]['player'] and self.state[0][0]['player'] != 0:
            return True
        elif self.state[0][2]['player'] == self.state[1][1]['player'] and self.state[1][1]['player'] == self.state[2][0]['player'] and self.state[1][1]['player'] != 0:
            return True
        
        
        return False

    def set_value(self,max_player):
        if self.terminal:
            winner = Game.check_for_completion(self.state)
            if winner == max_player:
                self.value = 1
            elif winner == 'Draw':
                self.value = 0
            else:
                self.value = -1
        elif not self.terminal and (None not in [child.value for child in self.children]):
            if self.depth % 2 == 0:
                self.value = max([node.value for node in self.children])
            else:
                self.value = min([node.value for node in self.children])
        else:
            for node in self.children:
                node.set_value(max_player)




