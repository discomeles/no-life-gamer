"""Conway's Game of Life Mathematics module for No Life Gamer

This module includes functions which can be used to determine
the evolution of game of life cells. Requires numpy.

Functions:

test_matrix
create_random_matrix
create_zero_matrix
evaluate_sum_alive
evaluate_sum_dead
calculate
evaluate_cells
"""
import numpy as np

def test_matrix():
    """Returns a 6x6 matrix for testing purposes"""
    m_test = np.array([[1,0,0,0,0,0],
                       [0,0,0,1,1,0],
                       [0,1,1,1,1,0],
                       [0,0,0,1,0,0],
                       [0,0,1,0,0,1],
                       [1,0,0,0,0,1]])
    return m_test

def create_random_matrix(m: int,n: int):
    """
    Returns a m x n matrix randomly filled with 0 and 1.

    Parameters:
        m (int): The height of the matrix
        n (int): The width of the matrix
    """
    rng = np.random.default_rng()
    return rng.integers(low=0, high=2, size=(m,n))


def create_zero_matrix(m: int,n: int):
    """
    Returns a m x n matrix filled with 0s.

    Parameters:
        m (int): The height of the matrix
        n (int): The width of the matrix
    """    
    return np.zeros((m,n), dtype=int)


def evaluate_sum_alive(sum: int):
    """
    Evaluates the evolution of a living cell based on the rules
    of Conway's game of life.
    Returns 1 if cell is alive and 0 if the cell is dead.

    Parameters:
        sum (int): The sum of neighbour cells
    """
    # The cell will continue living
    if sum == 2 or sum == 3:
        return 1
    # The cell dies of underpopulation, if sum < 1
    # The cell dies of overpopulation, if 3 < sum < 8
    else:
        return 0

def evaluate_sum_dead(sum):
    """
    Evaluates the evolution of a dead cell based on the rules
    of Conway's game of life.
    Returns 1 if cell is alive and 0 if the cell is dead.

    Parameters:
        sum (int): The sum of neighbour cells
    """
    # The cell becomes alive, if sum is 3
    if sum == 3:
        return 1
    else:
        return 0


# Calculating the sum of cells around The Cell
def calculate_neighbours(A, i, j):
    """
    Calculates the sum of living (1) and dead (0) cells around
    the cell, which is in position (i,j) in matrix A. 
    Edges of the matrix are wrapped around in order to create
    a toroidal surface. Returns the sum of living neightbours.

    Parameters:
    A (NDarray): The game of life matrix
    i (int): row position of the cell
    j (int): column position of the cell
    """
    # i_max is the index of the last row in matrix A
    # j_max is the index of last column in matrix A
    i_max = np.shape(A)[0]-1
    j_max = np.shape(A)[1]-1

    # if i = i_max, position i+1 is 0
    if i == i_max and j != j_max:
        result = (A[i-1, j-1]+A[i-1, j]+A[i-1, j+1]+
                  A[i, j-1]+A[i, j+1]+
                  A[0, j-1]+A[0, j]+A[0, j+1])
        
    # if j = j_max, position j+1 is 0
    elif i != i_max and j == j_max:
        result = (A[i-1, j-1]+A[i-1, j]+A[i-1, 0]+
                A[i, j-1]+A[i, 0]+
                A[i+1, j-1]+A[i+1, j]+A[i+1, 0])
        
    # if both i and j are i_max and j_max
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
    """
    Evaluates the cells of matrix A using the rules of Conway's
    Game of Life. Function determines dimensions of a given matrix,
    creates a temporary matrix of zeros and assigns new calculated
    and evaluated values to it. Returns the matrix of new values.

    Parameters:
    A (NDarray): The game of life matrix
    """
    # determine the range of i and j
    i_ran = np.shape(A)[0]
    j_ran = np.shape(A)[1]
    temp_matrix = create_zero_matrix(i_ran, j_ran)

    # traverse the matrix and evaluate cells
    for i in range(0, i_ran, 1):
        for j in range(0, j_ran, 1):
            neighbour_value = calculate_neighbours(A, i, j)
            # if the current cell is alive
            if A[i][j] == 1:
                cell_value = evaluate_sum_alive(neighbour_value)
            # if the current cell is dead
            else:
                cell_value = evaluate_sum_dead(neighbour_value)
            temp_matrix[i][j] = cell_value
    return temp_matrix