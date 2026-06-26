import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)

print("Axis=0 (Column Sum)")
print(np.sum(arr,axis=0))

print("Axis=1 (Row Sum)")
print(np.sum(arr,axis=1))

print("Column Mean")
print(np.mean(arr,axis=0))

print("Row Mean")
print(np.mean(arr,axis=1))

print("Maximum Column Values")
print(np.max(arr,axis=0))

print("Maximum Row Values")
print(np.max(arr,axis=1))