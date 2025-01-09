import time
import pyautogui
import pygame
import random

from cell import Mine
from grid import Grid

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 10  # Number of rows and columns
CELL_SIZE = 40  # Size of each cell in pixels
MINE_COUNT = 20  # Number of mines

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
RED = (255, 0, 0)

mine_image = pygame.image.load("assets/mine.png")
number_images = [pygame.image.load("assets/revealed.png"), pygame.image.load("assets/1.png"), pygame.image.load("assets/2.png"), pygame.image.load("assets/3.png"), pygame.image.load("assets/4.png"), pygame.image.load("assets/5.png"), pygame.image.load("assets/6.png"), pygame.image.load("assets/7.png"), pygame.image.load("assets/8.png")]
unrevealed_image = pygame.image.load("assets/blank.png")
flagged_image = pygame.image.load("assets/flag.png")

mine_image = pygame.transform.scale(mine_image, (CELL_SIZE, CELL_SIZE))
number_images = [pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE)) for img in number_images]
unrevealed_image = pygame.transform.scale(unrevealed_image, (CELL_SIZE, CELL_SIZE))
flagged_image = pygame.transform.scale(flagged_image, (CELL_SIZE, CELL_SIZE))

# Initialize screen
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Font for numbers
font = pygame.font.Font(None, 36)

def create_grid():
    """Creates a grid with randomly placed mines."""
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Place mines
    mines = 0
    while mines < MINE_COUNT:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if grid[row][col] == -1:
            continue
        grid[row][col] = -1
        mines += 1

        # Update numbers around the mine
        for i in range(-1, 2):
            for j in range(-1, 2):
                ni, nj = row + i, col + j
                if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE and grid[ni][nj] != -1:
                    grid[ni][nj] += 1

    return grid

def draw_grid(grid):
    """Draws the Minesweeper grid."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            # Draw cell content
            cell_content = grid.grid_data[row][col].to_string()
            if cell_content == "X":  # Mine
                screen.blit(mine_image, (x, y))
                continue

            elif cell_content == "#":
                screen.blit(unrevealed_image, (x, y))
                continue
            
            elif cell_content == "F":
                screen.blit(flagged_image, (x, y))
                continue

        
            img = number_images[int(cell_content)]
            screen.blit(img, (x, y))
            
first_click = True

def main():
    global first_click
    """Main game loop."""
    grid = Grid(GRID_SIZE, GRID_SIZE, 5)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos_x, pos_y = pygame.mouse.get_pos()
                if event.button  == 1:
                    x, y =  (pos_x // CELL_SIZE, pos_y // CELL_SIZE)
                    print("Clicked %s, %s" % (pos_x // CELL_SIZE, pos_y // CELL_SIZE))
                    is_alive = grid.click(y, x)

                    if grid.wincheck():
                        pygame.display.flip()
                        draw_grid(grid)
                        
                        pyautogui.alert("You Win!")
                        print("You Win!")
                        return

                    if not is_alive or (not grid.losscheck(y, x) and not first_click):
                        grid.grid_data[y][x] = Mine()
                        grid.grid_data[y][x].revealed = True
                        draw_grid(grid)

                        pygame.display.flip()

                        pyautogui.alert("Ya dun fucked up!")
                        time.sleep(1)
                        return

                    first_click = False
                    
                elif event.button == 3:
                    print("Flagging %s, %s" % (pos_x // CELL_SIZE, pos_y // CELL_SIZE))
                    
                    grid.flag(pos_y // CELL_SIZE, pos_x // CELL_SIZE)

        # Clear screen
        screen.fill(BLACK)

        # Draw the grid
        draw_grid(grid)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
