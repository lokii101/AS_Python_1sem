# Описать функцию MtrProd, вычисляющую произведение двух матриц.
def MtrProd(A, B):
    if not A or not B:
        raise ValueError()
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    if len(B) != n:
        raise ValueError()
    C = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
C = MtrProd(A, B)
print(C)



