import numpy as np

def Richardson(a, b, x, n):
    tol = 1e-3
    max_iter = 100
    cambio_rel = 1
    cont = 0
    y = np.zeros_like(x)
    while (cambio_rel>tol) and (cont<max_iter):
        print("x=["+(" "*4).join(list(map('{:5.3}'.format,x)))+"]")
        for i in range(n):
            y[i] = x[i] - np.dot(a[i,:],x[:])+b[i]
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

a = np.array([[0.5, -0.2, 0.5], [0.1, 0.6, 0.4], [-0.3, 0.1, 0.0]], dtype='f4')
n = len(a)
b = np.array([-1, 6.5, 0.7], dtype='f4')
x = np.array([0, 0, 0], dtype='f4')

Richardson(a, b, x, n)
