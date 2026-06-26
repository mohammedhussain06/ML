import numpy as np

arr = np.array([1,2,3])

view = arr.view()

copy = arr.copy()

view[0]=100

print(arr)

print(view)

print(copy)