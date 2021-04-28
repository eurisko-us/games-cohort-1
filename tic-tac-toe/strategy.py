from game import Game
from minimax import Minimax
class Strategy:
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
        return minimax.best_move()

