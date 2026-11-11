import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    # assume the matrix is 2x2
    trA = matrix[0][0] + matrix[1][1]
    detA = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # compute the eigenvalues via the pen-and-paper derived formula
    eval1 = (trA + math.sqrt(trA**2 - 4 * detA)) * 0.5
    eval2 = (trA - math.sqrt(trA**2 - 4 * detA)) * 0.5

    return sorted([eval1, eval2], key=lambda x: -x)
