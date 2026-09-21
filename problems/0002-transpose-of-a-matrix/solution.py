def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    i, j = len(a[0]), len(a)
    out = [[0] * j for _ in range(i)]

    
    for i in range(len(a[0])):
        for j in range(len(a)):
            out[i][j] = a[j][i]
    return out