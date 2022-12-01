import time
import pygame
import numpy as np
import matplotlib.pyplot as plt

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (10, 10, 10)
COLOR_ALIVE_NEXT = (255, 255, 255)

X = 800
Y = 600
DIMX = X / 10
DIMY = Y / 10

POPULATION = 0

DEAD_TO_LIFE = 1
DEAD_TO_DEAD = int(DIMX * DIMY) - POPULATION
LIFE_TO_LIFE = 1
LIFE_TO_DEAD = 1

class markov_chain():
    def __init__(self, DeadLife, DeadDead, LifeLife, LifeDead):
        self.DeadLife = DeadLife
        self.DeadLife = DeadDead
        self.DeadLife = LifeLife
        self.DeadLife = LifeDead

    def Born (self, DeadLife):
        self.DeadLife = DeadLife

def update(screen, cells, size, with_progress=False):
    DeadLife = 0
    DeadDead = 0
    LifeLife = 0
    LifeDead = 0
    population = 0

    update_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1 and alive < 2 or alive > 3:
            LifeDead += 1
            if with_progress:
                color = COLOR_DIE_NEXT

        elif (cells[row, col] == 1 and 2 <= alive <= 3) or (cells[row, col] == 0 and alive == 3):
            update_cells[row, col] = 1
            population += 1
            if with_progress:
                color = COLOR_ALIVE_NEXT
            else:
                DeadLife += 1

        pygame.draw.rect(screen, color, (col * size,
                         row * size, size - 1, size - 1))
        DeadDead = int((DIMX*DIMY) - population)
        # LifeLife = population - DeadLife

    print("================================== each iteration ===============================")
    print(f'Population: {population}')
    print(f'Dead to Life: {DeadLife}')
    print(f'Dead to Dead: {DeadDead}')
    print(f'Life to Dead: {LifeDead}')
    # print(f'Life to Life: {LifeLife}')
    
    return update_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((X, Y))

    cells = np.zeros((int(DIMY), int(DIMX)))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.005)


if __name__ == '__main__':
    main()
