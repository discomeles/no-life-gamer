import numpy as np

# Matrix for testing purposes
def test_matrix():
    m_test = np.array([[0,0,0,0,0,0],
                       [0,0,0,1,1,0],
                       [0,1,1,1,1,0],
                       [0,0,0,1,0,0],
                       [0,0,1,0,0,0],
                       [0,0,0,0,0,0]])
    return m_test

# Function for creating random matrix
def create_random_matrix(a: int,b: int):
    rng = np.random.default_rng()
    return rng.integers(low=0, high=2, size=(a,b))

# Function for a x b matrix of zeros
def create_zero_matrix(a: int,b: int):
    return np.zeros((3,3), dtype=int)

# Checking the status of a cell which is alive
def evaluate_sum_alive(sum):
    # The cell will continue living
    if sum == 2 or sum == 3:
        return 1
    # The cell dies of underpopulation, if sum is 0 or 1
    # The cell dies of overpopulation, if sum is in range 3,8
    else:
        return 0

# Checking the status of a cell which is dead
def evaluate_sum_dead(sum):
    # The cell comes alive, if sum is 3
    if sum == 3:
        return 1
    else:
        return 0


# Calculating the sum of cells around The Cell
def calculate(A, i, j):
    result = (A[i-1, j-1]+A[i-1, j]+A[i-1, j+1]+
              A[i, j-1]+A[i, j+1]+
              A[i+1, j-1]+A[i+1, j]+A[i+1, j+1])
    return result

# If cell is on the edge
def edge_cell(A, i, j):
    dimensiot = np.shape(A)
    pass

def check_submatrix(A, i: int, j: int):
    if i == 0:
        if j == 0:
            pass
    else:
        pass

def main():
    tm = test_matrix()
    result = calculate(tm, 2,2)
    print(result)

if __name__=="__main__":
    main()