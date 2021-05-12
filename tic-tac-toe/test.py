from game import Game
from strategy import TestStrategy
from strategy import MinimaxStrategy
from strategy import RandomStrategy
from minimax import Minimax
import time

s = time.time()
m = Minimax([[0 for i in range(3)] for j in range(3)],1)
print(len(m.nodes))
e = time.time()
print(len(m.nodes), e-s)

games = []
# for _ in range(100):
#     print(_)
#     if _%2 == 0:
#         t = Game(RandomStrategy, MinimaxStrategy)
#         games.append(t.run_game())
#     else:
#         t = Game(MinimaxStrategy, RandomStrategy)
#         games.append(t.run_game())

# print("Random wins "+str((games.count(1)/len(games))*100)+"% of the time")
# print("Minmax wins "+str((games.count(2)/len(games))*100)+"% of the time")
# print("A Draw happens "+str((games.count("Draw")/len(games))*100)+"% of the time")
