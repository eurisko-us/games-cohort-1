import copy
from minimax_node import Node
from game import Game
class Minimax:
    def __init__(self,state,pieces, max_player, N = 3):
        self.root = Node(state, pieces, None,None,0,N)
        self.N = N
        self.active_node = self.root
        self.max_player = max_player
        self.nodes = []
        self.build_tree()

    def next_step(self,player):
        new_nodes = []
        base_state = self.active_node.state
        base_pieces = self.active_node.pieces
        biggest_available_piece = max(base_pieces[player-1])
        for x in range(3):
            for y in range(3):
                if base_state[x][y]['size'] < biggest_available_piece:
                    for size in list(set([i for i in base_pieces[player-1] if i > base_state[x][y]['size']])):
                        possible_state = copy.deepcopy(base_state)
                        possible_pieces = copy.deepcopy(base_pieces)
                        possible_state[x][y] = {'player':player, 'size': size}
                        possible_pieces[player-1].remove(size)
                        new_node = Node(possible_state,possible_pieces, self.active_node,((x,y),size),self.active_node.depth + 1, self.N)
                        self.active_node.children.append(new_node)
                        new_nodes.append(new_node)
        return new_nodes

    def build_tree(self):
        active_player = self.max_player
        queue = [self.root]
        while len(queue) > 0:
            self.active_node = queue[0]
            self.nodes.append(self.active_node)
            if not self.active_node.terminal and self.active_node.depth < self.N:
                queue = queue + self.next_step(active_player)
            del queue[0]
            active_player = 1 if active_player == 2 else 2 

    def best_move(self):
        #print(self.max_player)
        while self.root.value is None:
            self.root.set_value(self.max_player)
        # print(self.root.pieces)
        # print(self.root.state)
        root_values = [child.value for child in self.root.children]
        best_move_index = root_values.index(max(root_values))

        return self.root.children[best_move_index].difference



