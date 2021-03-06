from game import Game
class Node:
    def __init__(self,state,parent,move,depth):
        self.state = state
        self.parent = parent
        self.difference = move
        self.depth = depth
        self.value = None
        self.terminal = False if Game.check_for_completion(state) is None else True
        self.children = []

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




