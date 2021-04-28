import random
from exceptions import CheaterException, ForfietException
from board import Board
from check_win import check_win

class Game:
    def __init__(self, strats):
        self.strats = strats
        self.letters = {'x': 0, 'o': 1, None: 2}
        self.board = Board()

    def run_simulations(self, iterations, print_simulations = False):
        self.wins = [0, 0, 0]
        for iteration in range(0, iterations):
            if print_simulations: 
                print('\nIteration:', iteration)
                
            try: 
                self.run_game(iteration, print_simulations)

            except CheaterException as cheater:
                print(cheater, 'cheated on simulation iteration', iteration)
                exit()

            except ForfietException as forfiet:
                turn = forfiet.args[0]
                if print_simulations:
                    print(self.strats[turn % 2].__name__, 'Forfiet on simulation iteration:', iteration, 'turn:', turn)
                self.wins[turn % 2] += 1
                self.board.new_game(turn % 2)
                continue

            winner = check_win(self.board.current_board)
            self.wins[self.letters[winner]] += 1
            self.board.new_game(winner)

        return [win / iterations for win in self.wins]

    def run_game(self, iteration, print_simulations = False):
        random.seed(iteration + 1) #in case of a strat that uses random
        turn = 0
        winner = None
        while check_win(self.board.current_board) is None and winner is None and turn < 8:
            next_move = self.strats[turn % 2](self.board.current_board, turn)
            self.board[next_move] = list(self.letters.keys())[turn % 2]
            if print_simulations:
                print('\nTurn:', turn + 1)
                for row in self.board:
                    print(str(row[0]) + ' | ' + str(row[1]) + ' | ' + str(row[2]))
                    print('------------')
            turn += 1
            winner = check_win(self.board.current_board)
            
            