import numpy as np

def JacobiRichardson(a, b, x, n):
    tol = 1e-3
    max_iter = 100
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    while (cambio_rel>tol) and (cont<max_iter):
        print("x=["+(" "*4).join(list(map('{:5.3}'.format,x)))+"]")
        for i in range(n):
            idx = [j for j in range(n) if j!=i]
            y[i] = (b[i]-np.dot(a[i, idx],x[idx]))/a[i, i]
        cambio_rel = np.linalg.norm(x-y, np.inf)/np.linalg.norm(y, np.inf)
        x[:] = y[:]
        cont += 1
    print("x=["+(" "*4).join(list(map('{:5.3}'.format,x)))+"]")
    if cambio_rel <= tol:
        print("Metodo converge")
    else:
        print("Metodo no converge")
    print(f"Metodo terminado en {cont} iteraciones.")
    return x, cont

a = np.array([[1, 10], [10, 2]], dtype='f4')
n = len(a)
b = np.array([11, 12], dtype='f4')
x = np.array([0, 0], dtype='f4')

JacobiRichardson(a, b, x, n)