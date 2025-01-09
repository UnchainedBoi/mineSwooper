from grid import *
from cell import *


new_grid = Grid(10, 10, 10)
while new_grid.action(input("Action:")):
    new_grid.pront()
    if new_grid.wincheck():
        print("You Win!")
        break

new_grid.pront(reveal=True)


