from minimax_node import Node
from game import Game
class Minimax:
    def __init__(self,state, max_player, k = 2):
        self.k = k
        self.k_count = [0, 0, 0]
        self.root = Node(state, None, None, 0)
        self.active_node = self.root
        self.max_player = max_player
        self.nodes = []
        self.build_tree()
        

    def next_step(self,player):
        new_nodes = []
        base_state = self.active_node.state
        for x in range(3):
            for y in range(3):
                element = self.active_node.state[x][y]
                possible_state = [[y for y in x] for x in base_state]
                if element is None:
                    for strength, count in enumerate(self.k_count):
                        if count + 1 < self.k:
                            possible_state[x][y] = (player, strength)
                            self.k_count[strength] += 1
                            break
                    new_node = Node(possible_state, self.active_node, (x,y), self.active_node.depth + 1)
                    self.active_node.children.append(new_node)
                    new_nodes.append(new_node)
                elif element[0] != player and element[1] < 2 and self.k_count[element[1] + 1] < self.k:
                    possible_state[x][y] = (player, element[1] + 1)
                    new_node = Node(possible_state, self.active_node, (x,y), self.active_node.depth + 1)
                    self.active_node.children.append(new_node)
                    new_nodes.append(new_node)
        return new_nodes

    def build_tree(self):
        active_player = self.max_player
        queue = [self.root]
        while len(queue) > 0:
            self.active_node = queue[0]
            self.nodes.append(self.active_node)
            if not self.active_node.terminal:
                queue = queue + self.next_step(active_player)
            del queue[0]
            active_player = 1 if active_player == 2 else 2 

    def best_move(self):
        while self.root.value is None:
            self.root.set_value(self.max_player)

        root_values = [child.value for child in self.root.children]
        best_move_index = root_values.index(max(root_values))

        return self.root.children[best_move_index].difference



