import time
import pygame
import numpy as np
import matplotlib.pyplot as plt


'''
Anthony Jardiel López Pérez || 2271557
No logré implementar las cadenas de markov. Lo siento, inge.
'''


col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)

DIMX = 100
DIMY = 70


def update(surface, cur, sz):
    DeadLife = 0
    DeadDead = 0
    LifeLife = 0
    LifeDead = 0
    population = 0

    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_about_to_die
            LifeDead += 1

        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            col = col_alive
            population += 1
            LifeLife = population - LifeDead

        col = col if cur[r, c] == 1 else col_background
        pygame.draw.rect(surface, col, (c*sz, r*sz, sz-1, sz-1))

        DeadDead = int((DIMX*DIMY) - population)
    print("================================== each iteration ===============================")
    print(f'Population: {population}')
    print(f'Dead to Life: {DeadLife}')
    print(f'Dead to Dead: {DeadDead}')
    print(f'Life to Dead: {LifeDead}')
    print(f'Life to Life: {LifeLife}')


    np.random.seed(3)
    StatesData = ["Life", "Dead"]

    TransitionStates = [["LiLi", "LiDe"], ["DeDe", "DeLi"]]
    TransitionMatrix = [[(LifeLife/(LifeLife+LifeDead)), (LifeDead/(LifeLife+LifeDead))],
                            [DeadLife/(DeadLife+DeadDead), DeadDead/(DeadLife+DeadDead)]]

    MarkovChain = list()
    TodayPrediction = StatesData[0]

    for r, c in np.ndindex(cur.shape):

        if TodayPrediction == "Life":
            TransCondition = np.random.choice(
                TransitionStates[0], replace=True, p=TransitionMatrix[0])

            if TransCondition == "LiLi":
                pass

            else:
                TodayPrediction = "Dead"

        elif TodayPrediction == "Dead":
            TransCondition = np.random.choice(
                TransitionStates[1], replace=True, p=TransitionMatrix[1])

            if TransCondition == "DeDe":
                pass
            
            else:
                TodayPrediction = "Life"
        MarkovChain.append(TodayPrediction)

    return nxt


def init(dimx, dimy):
    cells = np.zeros((dimy, dimx))

    pattern = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
                            1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
                            1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                            1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0,
                            0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                            0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    pos = (3, 3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]
        :pos[1]+pattern.shape[1]] = pattern
    return cells

def main(dimx, dimy, cellsize):
    generation = 0
    plot = init(dimx, dimy)
    plt.plot(plot)
    plt.show()
    plt.figure()
    plt.hist(plot)
    plt.show()
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = init(dimx, dimy)

    while True:
        generation += 1
        print(f'Generation: {generation}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(col_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()

        time.sleep(0.0001)
    


if __name__ == "__main__":
    main(DIMX, DIMY, 8)
