from game import Game
from strategy import TestStrategy
from strategy import MinimaxStrategy
from strategy import RandomStrategy

# ttt = Game(RandomStrategy,MinimaxStrategy,n)
# print(ttt.run_game())
# print("\n")
games = []
for n in [3]:
    for _ in range(200):
        if _%2 == 0:
            t = Game(RandomStrategy, MinimaxStrategy,n)
            winner = t.run_game()
            if winner == 1: 
                games.append('random')
            elif winner == 2:
                games.append('Minimax')
            else:
                games.append('Draw')
        else:
            t = Game(MinimaxStrategy, RandomStrategy,n)
            winner = t.run_game()
            if winner == 1: 
                games.append('Minimax')
            elif winner == 2:
                games.append('random')
            else:
                games.append('Draw')
    print(n)
    print("\tRandom wins "+str((games.count('random')/len(games))*100)+"% of the time")
    print("\tMinmax wins "+str((games.count('Minimax')/len(games))*100)+"% of the time")
    print("\tA Draw happens "+str((games.count("Draw")/len(games))*100)+"% of the time")
    print("\n")
