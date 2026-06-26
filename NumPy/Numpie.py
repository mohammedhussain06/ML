import numpy as np



#Create from list and creating numpy array from methods 

# arr = np.array([1, 2, 3, 4, 5])

# print(arr, type(arr))



# arr1 = np.array([1, 2, 3, 4, 5, "prime"])

# print(arr1, type(arr1), arr1.dtype, arr1.shape)



# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(arr2d, arr2d.shape)



# zero = np.zeros((2, 3), dtype= "int64")

# print(zero, zero.shape)



# ones = np.ones((2, 3), dtype= "int64")

# print(ones, ones.shape)



# fill = np.full((2, 3), 100)

# print(fill, fill.shape)



# i = np.eye(3)

# print(i, i.shape)



# new = np.arange(1, 10)

# print(new, new.shape)



# kine = np.linspace(0, 11, 2) evenly spaced arrays

# print(kine, kine.shape)



# Properties

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr.shape)   #dimensions = m x n

print(arr.size)    #tot els = 9

print(arr.dtype)

print(arr.ndim)

float_arr = arr.astype(np.float64)

print(float_arr, float_arr.dtype)



arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr, arr.shape)

reshaped = arr.reshape((3, 2))

print(reshaped, reshaped.shape)

flattened = arr.flatten()



arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2d)

print(np.sum(arr2d))

sum_of_columns = np.sum(arr2d, axis = 0)

print(sum_of_columns)

sum_of_rows = np.sum(arr2d, axis = 1)

print(sum_of_rows)

print(arr2d[0:2, 1:2])