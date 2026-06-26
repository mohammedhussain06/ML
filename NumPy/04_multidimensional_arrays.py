import numpy as np

# 1D Array
arr1 = np.array([1, 2, 3])

# 2D Array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 3D Array
arr3 = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr2)
print(arr3)

print("Dimensions :", arr3.ndim)
print("Shape :", arr3.shape)
print("Size :", arr3.size)

# Indexing

print(arr2[1][2])
print(arr3[1][0][1])

# Slicing

print(arr2[:,1])
print(arr2[0,:])