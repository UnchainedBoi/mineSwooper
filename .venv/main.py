from grid import *
from cell import *


new_grid = Grid(10, 10, 10)
first = True
while new_grid.action(input("Action:"), first=first):
    new_grid.pront()
    if new_grid.wincheck():
        print("You Win!")
        break

new_grid.pront(reveal=True)


