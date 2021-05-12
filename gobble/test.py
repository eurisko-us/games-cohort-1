from game import Game
from strategy import TestStrategy
from strategy import RandomStrategy

ttt = Game(RandomStrategy,RandomStrategy)
print(ttt.run_game())
print("\n")
games = []
for _ in range(10000):
    if _%2 == 0:
        t = Game(RandomStrategy, RandomStrategy)
        games.append(t.run_game())
    else:
        t = Game(RandomStrategy, RandomStrategy)
        games.append(t.run_game())

# print("Random wins "+str((games.count(1)/len(games))*100)+"% of the time")
# print("Minmax wins "+str((games.count(2)/len(games))*100)+"% of the time")
# print("A Draw happens "+str((games.count("Draw")/len(games))*100)+"% of the time")
