from gobble import Gobble
from cycle_strat import CycleStrategy
from random_strat import RandomStrategy


cycle = CycleStrategy()
random = RandomStrategy()

game = Gobble(2, [cycle, random])
game.play()

