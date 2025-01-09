from random import randint

from cell import *

class Grid:

    def __init__(self, width, height, num_mines):
        self.grid_data: list[list[Cell]] = []
        for w in range(width):
            self.grid_data.append([])
            for h in range(height):
                self.grid_data[w].append(Number(0))
        self.width = width
        self.height = height


        # Mines Placen
        for i in range(num_mines):
            self.grid_data[randint(0, width - 1)][randint(0, height - 1)] = Mine()

        # Nummern Updaten
        for x in range(width):
            for y in range(height):
                cell = self.grid_data[x][y]
                if not isinstance(cell, Number):
                    continue
                for xi in range(-1, 2):
                    for yi in range(-1, 2):
                        if x + xi >= width or y + yi >= height:
                            continue
                        if x + xi < 0 or y + yi < 0:
                            continue
                        if isinstance(self.grid_data[x+xi][y+yi], Mine):
                            cell.value += 1




    def pront(self, reveal=False):
        for outer in self.grid_data:
            for cell in outer:
                print(cell.to_string(reveal) + " ", end="")
            print("")

    def flag(self, x, y):
        if self.grid_data[x][y].revealed:
            return True
        self.grid_data[x][y].flagged ^= True
        return True

    def click(self, x, y):
        if self.grid_data[x][y].revealed:
            return True
        self.grid_data[x][y].revealed = True
        if isinstance(self.grid_data[x][y], Mine):
            print("Ya dun fucked up!")
            return False

        if self.grid_data[x][y].value == 0:
            for xi in range(-1, 2):
                for yi in range(-1, 2):
                    if x + xi >= self.width or y + yi >= self.height:
                        continue
                    if x + xi < 0 or y + yi < 0:
                        continue

                    self.click(x + xi, y + yi)
        return True

    def action(self, mov):
        splt = mov.split(" ")
        splt[1] = int(splt[1])
        splt[2] = int(splt[2])
        if splt[0] == "f":
            return self.flag(splt[2] - 1, splt[1] - 1)
        if splt[0] == "c":
            return self.click(splt[2] - 1, splt[1] - 1)
        print("Invalid Input!")
        return True

    def wincheck(self):
        mine_counter = 0
        hidden_counter = 0
        for outer in self.grid_data:
            for cell in outer:
                if isinstance(cell, Mine):
                    mine_counter += 1
                if not cell.revealed:
                    hidden_counter += 1
        print(f"Mines remaining: {mine_counter}")
        print(f"Cells hidden: {hidden_counter}")
        return mine_counter == hidden_counter




if __name__ == "__main__":
    new_grid = Grid(10, 10, 100)
    new_grid.pront()
