import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(np.dot(A,B))

print(np.matmul(A,B))

print(np.linalg.det(A))

print(np.linalg.inv(A))

print(np.linalg.eig(A))

print(np.trace(A))

print(np.transpose(A))