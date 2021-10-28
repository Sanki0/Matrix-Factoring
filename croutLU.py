import numpy as np

def crout(A):
    lA = len(A)
    L = np.zeros((lA, lA))
    U = np.zeros((lA, lA))

    for k in range(0, lA):
        U[k, k] = 1

        for j in range(k, lA):
            sum0 = sum([L[j, s] * U[s, k] for s in range(0, j)])
            L[j, k] = A[j, k] - sum0

        for j in range(k+1, lA):
            sum1 = sum([L[k, s] * U[s, j] for s in range(0, k)])
            U[k, j] = (A[k, j] - sum1) / L[k, k]

    return L, U


A = np.array([[6,2,1,-1],
            [2,4,1,0],
            [1,1,4,-1],
            [-1,0,-1,3]])
print(crout(A))