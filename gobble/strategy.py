import random
from game import Game
from minimax import Minimax
class TestStrategy:
    def __init__(self,player_num):
        self.player_num = player_num


    def move(self,current_game, pieces):
        for x in range(len(current_game)):
            for y in range(len(current_game[0])):
                for size in range(current_game[x][y]['size'],4):
                    if size in pieces[self.player_num-1] and current_game[x][y]['size'] < size:
                        return ((x,y),size)

class MinimaxStrategy:
    def __init__(self,player_num):
        self.player_num = player_num

    def move(self,current_game, current_pieces):
        minimax = Minimax(current_game, current_pieces,self.player_num)
        move = minimax.best_move()
        return move

class RandomStrategy:
    def __init__(self,player_num):
        self.player_num = player_num

    def move(self,current_game, pieces):
        empty_spaces = []
        for x in range(len(current_game)):
            for y in range(len(current_game[0])):
                for size in range(current_game[x][y]['size'],4):
                    if size in pieces[self.player_num-1]:
                        empty_spaces.append(((x,y),size))

        return random.choice(empty_spaces)

