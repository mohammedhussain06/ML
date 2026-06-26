import numpy as np

# Python Loop

numbers = [1,2,3,4,5]

result = []

for i in numbers:
    result.append(i*2)

print(result)

# NumPy Vectorization

arr = np.array([1,2,3,4,5])

print(arr*2)

print(arr+10)

print(arr**2)

print(np.sqrt(arr))

print(np.log(arr))

print(np.sin(arr))