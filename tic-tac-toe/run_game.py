import random
from game import Game
from check_win import check_win
from exceptions import ForfietException

letters = ['x', 'o']

def random_strat(board, turn):
    random_spot = (0, 0)
    while board[random_spot[0]][random_spot[1]] is not None:
        random_spot = (random.randint(0,2), random.randint(0,2))
    return random_spot


def my_strat(board, turn):
    if turn == 0:
        return (0,0)
    elif turn == 2:
        if board[2][2] is None:
            return (2,2)
        elif board[0][2] is None:
            return (0,2)
        elif board[2][0] is None:
            return (2,0)
    elif turn == 4:
        if board[0][2] is None:
            return (0,2)
        elif board[2][1] is None:
            return (2,1)
        elif board[1][1] is None:
            return (1,1)
    elif turn == 6:
        situation = 0
        if board[0][0] == 'x' and board[2][0] == 'x' and board[2][2] == 'x':
            situation = 1
        elif board[0][0] == 'x' and board[0][2] == 'x' and board[2][2] == 'x':
            situation = 2
        if situation == 1:
            if board[1][0] is None:
                return (1,0)
            elif board[2][1] is None:
                return (2,1)
            elif board[1][1] is None:
                return (1,1)
        elif situation == 2:
            if board[1][0] is None:
                return (1,0)
            elif board[1][0] is None:
                return (2,1)
            elif board[1][1] is None:
                return (1,1)
    raise ForfietException(turn)

def minimax_strat(board, turn): #minimax
    best_score = -1000000
    for x in range(3):
        for y in range(3):
            if board[x][y] is None:
                current_letter = letters[turn % 2]
                board[x][y] = current_letter
                score = minimax_algorithm(board, turn, current_letter, False)
                board[x][y] = None
                if score == 1:
                    return (x,y)
                elif score > best_score:
                    best_score = score
                    best_move = (x,y)
    return best_move

def minimax_algorithm(board, depth, current_letter, maximizing):
    result = check_win(board)
    if current_letter == 'x':
        scores = {'x': 1 + depth, 'o': -1 - depth, 'draw': 0}
    elif current_letter == 'o':
        scores = {'x': -1 - depth, 'o': 1 + depth, 'draw': 0}

    if result is not None:
        return scores[result]

    if maximizing:
        best_score = -1000000
        for x in range(3):
            for y in range(3):
                if board[x][y] is None:
                    current_letter = letters[1 - depth % 2]
                    board[x][y] = current_letter
                    score = minimax_algorithm(board, depth + 1, current_letter, False)
                    board[x][y] = None
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = 1000000
        for x in range(3):
            for y in range(3):
                if board[x][y] is None:
                    current_letter = letters[1 - depth % 2]
                    board[x][y] = current_letter
                    score = minimax_algorithm(board, depth + 1, current_letter, True)
                    board[x][y] = None
                    best_score = min(best_score, score)
        return best_score
    return best_score

strats = [random_strat, my_strat, minimax_strat] #dont run the minimax strat unless u want to waste hours waiting for it to finish
'''#118
for strat_1 in strats: #9 total games
    for strat_2 in strats:
        wins = Game([strat_1, strat_2]).run_simulations(1000, False)
        print('\n', strat_1.__name__, 'vs', strat_2.__name__, '\n', wins)
print()'''
#119
wins = Game([random_strat, minimax_strat]).run_simulations(100, False)
print('\n', random_strat.__name__, 'vs', minimax_strat.__name__, '\n', wins)
print('expected to draw more while winning more than random strat due to going second')

wins = Game([minimax_strat, random_strat]).run_simulations(100, False)
print('\n', minimax_strat.__name__, 'vs', random_strat.__name__, '\n', wins)
print('expected to draw more while losing the rest for example, I have no idea why the strat sucks, I coded it my own way, got crappy numbers, then I followed the video and got the same numbers but it do destory my strat (in local testing) with the first turn advantage given to my strat')
print()


