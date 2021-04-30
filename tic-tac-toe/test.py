from game import Game
from strategy import TestStrategy
from strategy import MinimaxStrategy
from strategy import RandomStrategy

ttt = Game(TestStrategy,MinimaxStrategy)
print(ttt.run_game())
print("\n")
games = []
for _ in range(100):
    print(_)
    if _%2 == 0:
        t = Game(RandomStrategy, MinimaxStrategy)
        games.append(t.run_game())
    else:
        t = Game(MinimaxStrategy, RandomStrategy)
        games.append(t.run_game())

print("Random wins "+str((games.count(1)/len(games))*100)+"% of the time")
print("Minmax wins "+str((games.count(2)/len(games))*100)+"% of the time")
print("A Draw happens "+str((games.count("Draw")/len(games))*100)+"% of the time")
