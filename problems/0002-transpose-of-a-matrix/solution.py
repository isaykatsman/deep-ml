def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    a_r = len(a)
    a_c = len(a[0])

    aT = [[0] * a_r for _ in range(a_c)]

    for i in range(a_r):
        for j in range(a_c):
            aT[j][i] = a[i][j]
    return aT