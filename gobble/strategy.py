import random
from game import Game
from minimax import Minimax
class TestStrategy:
    def __init__(self,player_num, k = 2):
        self.player_num = player_num
        self.k = k
        self.k_count = [0, 0, 0]

    def move(self,current_game):
        for x, row in enumerate(current_game):
            for y, element in enumerate(row):
                if element is None:
                    for strength, count in enumerate(self.k_count):
                        if count + 1 < self.k:
                            self.k_count[strength] += 1
                            return (x,y), strength                   
                elif element[0] != self.player_num and element[1] < self.k:
                    self.k_count[element[1]] += 1
                    return (x,y), element[1] + 1

class MinimaxStrategy:
    def __init__(self,player_num, k = 2):
        self.player_num = player_num
        self.k = k

    def move(self,current_game):
        minimax = Minimax(current_game, self.player_num, self.k)
        move = minimax.best_move()
        return move

class RandomStrategy:
    def __init__(self,player_num, k = 2):
        self.player_num = player_num
        self.k = k
        self.k_count = [0, 0, 0]

    def move(self,current_game):
        empty_spaces = []
        for x, row in enumerate(current_game):
            for y, element in enumerate(row):
                if element is None:
                    for strength, count in enumerate(self.k_count):
                        if count + 1 < self.k:
                            self.k_count[strength] += 1
                            empty_spaces.append([(x,y), strength])
                            break             
                elif element[0] != self.player_num and element[1] < self.k:
                    self.k_count[element[1]] += 1
                    empty_spaces.append([(x,y), element[1] + 1])

        return random.choice(empty_spaces)

