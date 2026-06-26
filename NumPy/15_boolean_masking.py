import numpy as np

arr = np.arange(10)

print(arr>5)

print(arr[arr>5])

print(arr[(arr>2)&(arr<8)])

print(arr[arr%2==0])