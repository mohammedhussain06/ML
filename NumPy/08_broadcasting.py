import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr+10)

vector = np.array([1,2,3])

print(arr+vector)

column = np.array([
    [10],
    [20]
])

print(arr+column)

# Scalar Broadcasting

print(arr*5)