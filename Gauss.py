import numpy as np

A = np.array([[3,2,1],
              [2,3,1],
              [1,2,3]])

B = np.array([[39],
              [34],
              [26]])


casicero = 1e-15 

A = np.array(A,dtype=float) 


AB  = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)


tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]


for i in range(0,n-1,1):

    columna  = abs(AB[i:,i])
    dondemax = np.argmax(columna)

    if (dondemax !=0):
 
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal
AB1 = np.copy(AB)


for i in range(0,n-1,1):
    pivote   = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor  = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor


ultfila = n-1
ultcolumna = m-1
X = np.zeros(n,dtype=float)

for i in range(ultfila,0-1,-1):
    suma = 0
    for j in range(i+1,ultcolumna,1):
        suma = suma + AB[i,j]*X[j]
    b = AB[i,ultcolumna]
    X[i] = (b-suma)/AB[i,i]

X = np.transpose([X])



print('Matriz aumentada:')
print(AB0)

print('eliminación hacia adelante')
print(AB)
print('solución: ')
print(X)