import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    matrix_arr = np.array(matrix)
    if mode == 'column':
        matrix_arr = matrix_arr.T

    n_r, n_c = len(matrix_arr), len(matrix_arr[0])

    # otherwise, assume we're computing the mean of each row
    sums = np.array([sum(r)/n_c for r in matrix_arr])
    return sums.tolist()
