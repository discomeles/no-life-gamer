import numpy as np

# placeholder for the source code
# add another line

# Checking the status of a cell

# Calculating the sum of cells around The Cell
def calculate(A, i, j):
    result = (A[i-1, j-1]+A[i-1, j]+A[i-1, j+1]+
              A[i, j-1]+A[i, j+1]+
              A[i+1, j-1]+A[i+1, j]+A[i+1, j+1])
    return result

# If cell is on the edge
def edgy(A, i, j):
    dimensiot = np.shape(A)
    pass

def check_submatrix(A, i: int, j: int):
    if i == 0:
        if j == 0:
            pass
    else:
        pass