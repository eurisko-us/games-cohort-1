import random
from game import Game
from minimax import Minimax
class TestStrategy:
    def __init__(self,player_num):
        self.player_num = player_num


    def move(self,current_game):
        for x in range(len(current_game)):
            for y in range(len(current_game[0])):
                if current_game[x][y] == 0:
                    return (x,y)

class MinimaxStrategy:
    def __init__(self,player_num):
        self.player_num = player_num

    def move(self,current_game):
        minimax = Minimax(current_game,self.player_num)
        move = minimax.best_move()
        return move

class RandomStrategy:
    def __init__(self,player_num):
        self.player_num = player_num

    def move(self,current_game):
        empty_spaces = []
        for x in range(len(current_game)):
            for y in range(len(current_game[0])):
                if current_game[x][y] == 0:
                    empty_spaces.append((x,y))

        return random.choice(empty_spaces)

