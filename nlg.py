import numpy as np
import pygame

# Matrix for testing purposes
def test_matrix():
    m_test = np.array([[1,0,0,0,0,0],
                       [0,0,0,1,1,0],
                       [0,1,1,1,1,0],
                       [0,0,0,1,0,0],
                       [0,0,1,0,0,1],
                       [1,0,0,0,0,1]])
    return m_test

# Function for creating random matrix
def create_random_matrix(m: int,n: int):
    rng = np.random.default_rng()
    return rng.integers(low=0, high=2, size=(m,n))

# Function for a x b matrix of zeros
def create_zero_matrix(m: int,n: int):
    return np.zeros((m,n), dtype=int)

# Checking the status of a cell which is alive
def evaluate_sum_alive(sum):
    # The cell will continue living
    if sum == 2 or sum == 3:
        return 1
    # The cell dies of underpopulation, if sum < 1
    # The cell dies of overpopulation, if 3 < sum < 8
    else:
        return 0

# Checking the status of a cell which is dead
def evaluate_sum_dead(sum):
    # The cell becomes alive, if sum is 3
    if sum == 3:
        return 1
    else:
        return 0


# Calculating the sum of cells around The Cell
def calculate(A, i, j):
    i_max = np.shape(A)[0]-1
    j_max = np.shape(A)[1]-1
    if i == i_max and j != j_max:
        result = (A[i-1, j-1]+A[i-1, j]+A[i-1, j+1]+
                  A[i, j-1]+A[i, j+1]+
                  A[0, j-1]+A[0, j]+A[0, j+1])
    elif i != i_max and j == j_max:
        result = (A[i-1, j-1]+A[i-1, j]+A[i-1, 0]+
                A[i, j-1]+A[i, 0]+
                A[i+1, j-1]+A[i+1, j]+A[i+1, 0])
    elif i == i_max and j == j_max:
        result = (A[i-1, j-1]+A[i-1, j]+A[i-1, 0]+
            A[i, j-1]+A[i, 0]+
            A[0, j-1]+A[0, j]+A[0, 0])            
    else:
        result = (A[i-1, j-1]+A[i-1, j]+A[i-1, j+1]+
                A[i, j-1]+A[i, j+1]+
                A[i+1, j-1]+A[i+1, j]+A[i+1, j+1])
    return result

def evaluate_cells(A):
    i_ran = np.shape(A)[0]
    j_ran = np.shape(A)[1]
    temp_matrix = create_zero_matrix(i_ran, j_ran)
    for i in range(0, i_ran, 1):
        for j in range(0, j_ran, 1):
            neighbour_value = calculate(A, i, j)
            if A[i][j] == 1:
                cell_value = evaluate_sum_alive(neighbour_value)
            else:
                cell_value = evaluate_sum_dead(neighbour_value)
            temp_matrix[i][j] = cell_value
    return temp_matrix

def game_main():
    pygame.init()

    display = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()

    tiles = []
    tiles.append(pygame.image.load("grass32.png"))
    tiles.append(pygame.image.load("flower32.png"))
    width = 25
    height = 15
    tm = create_random_matrix(15,25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        display.fill((0,0,0))


        for j in range(25):
            for i in range(15):
                value = tm[i][j]
                display.blit(tiles[value], (j*32, i*32))

        rm = evaluate_cells(tm)
        tm = rm.copy()

        pygame.display.flip()
        clock.tick(1)


def main():
    game_main()

if __name__=="__main__":
    main()