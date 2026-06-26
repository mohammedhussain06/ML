# NumPy Cheat Sheet

## What is NumPy?

**NumPy (Numerical Python)** is a Python library for fast numerical
computing. It provides: - Multidimensional arrays (`ndarray`) -
Mathematical functions - Linear algebra - Random number generation -
Statistical operations

------------------------------------------------------------------------

# Import

``` python
import numpy as np
```

------------------------------------------------------------------------

# Creating Arrays

``` python
np.array([1,2,3])
np.array([[1,2],[3,4]])
np.zeros((2,3))
np.ones((3,3))
np.empty((2,2))
np.eye(3)
np.identity(4)
np.arange(0,10,2)
np.linspace(0,1,5)
np.random.rand(3)
np.random.randn(3)
np.random.randint(1,10,(2,2))
```

------------------------------------------------------------------------

# Array Information

``` python
arr.ndim      # Number of dimensions
arr.shape     # Shape
arr.size      # Total elements
arr.dtype     # Data type
arr.itemsize  # Bytes per element
arr.nbytes    # Total memory
```

------------------------------------------------------------------------

# Changing Shape

``` python
arr.reshape(2,3)
arr.flatten()
arr.ravel()
arr.T
```

Definitions: - **reshape()** -- Changes shape without changing data. -
**flatten()** -- Returns a copy as 1D. - **ravel()** -- Returns a
flattened view whenever possible. - **T** -- Transpose rows and columns.

------------------------------------------------------------------------

# Indexing & Slicing

``` python
arr[0]
arr[-1]
arr[1:4]
arr[:,1]
arr[1,:]
arr[0:2,1:3]
```

------------------------------------------------------------------------

# Mathematical Operations

``` python
arr + 5
arr - 5
arr * 2
arr / 2
arr ** 2
np.sqrt(arr)
np.exp(arr)
np.log(arr)
np.sin(arr)
np.cos(arr)
```

------------------------------------------------------------------------

# Statistical Functions

``` python
np.sum(arr)
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
np.min(arr)
np.max(arr)
np.argmin(arr)
np.argmax(arr)
```

------------------------------------------------------------------------

# Aggregation Along Axis

``` python
arr.sum(axis=0)
arr.sum(axis=1)

arr.mean(axis=0)
arr.mean(axis=1)
```

-   `axis=0` → Column-wise
-   `axis=1` → Row-wise

------------------------------------------------------------------------

# Sorting

``` python
np.sort(arr)
np.argsort(arr)
```

------------------------------------------------------------------------

# Joining Arrays

``` python
np.concatenate((a,b))
np.vstack((a,b))
np.hstack((a,b))
```

------------------------------------------------------------------------

# Splitting Arrays

``` python
np.split(arr,2)
np.vsplit(arr,2)
np.hsplit(arr,2)
```

------------------------------------------------------------------------

# Searching

``` python
np.where(arr>5)
np.nonzero(arr)
```

------------------------------------------------------------------------

# Unique Values

``` python
np.unique(arr)
```

------------------------------------------------------------------------

# Copy vs View

``` python
copy = arr.copy()
view = arr.view()
```

-   **copy()** → Independent copy
-   **view()** → Shares original data

------------------------------------------------------------------------

# Boolean Masking

``` python
arr[arr>5]
arr[(arr>2)&(arr<8)]
```

------------------------------------------------------------------------

# Broadcasting

``` python
arr + 5
arr * np.array([1,2,3])
```

Broadcasting automatically expands smaller arrays to match dimensions.

------------------------------------------------------------------------

# Matrix Operations

``` python
A @ B
np.dot(A,B)
np.matmul(A,B)
np.linalg.inv(A)
np.linalg.det(A)
np.linalg.eig(A)
```

------------------------------------------------------------------------

# Random Module

``` python
np.random.seed(42)
np.random.rand(3,3)
np.random.randn(3,3)
np.random.randint(1,10,5)
np.random.choice([1,2,3],5)
np.random.shuffle(arr)
```

------------------------------------------------------------------------

# Useful Functions

``` python
np.abs(arr)
np.round(arr)
np.floor(arr)
np.ceil(arr)
np.clip(arr,0,10)
```

------------------------------------------------------------------------

# Data Types

``` python
arr.astype(int)
arr.astype(float)
```

------------------------------------------------------------------------

# Handling Missing Values

``` python
np.isnan(arr)
np.nanmean(arr)
np.nanmedian(arr)
np.nansum(arr)
```

------------------------------------------------------------------------

# Frequently Used Definitions

-   **Array** -- Collection of elements of the same data type.
-   **ndarray** -- NumPy's main array object.
-   **Axis** -- Direction along which operations occur.
-   **Broadcasting** -- Automatic expansion of arrays for arithmetic.
-   **Vectorization** -- Performing operations on entire arrays without
    loops.
-   **Transpose** -- Swapping rows and columns.
-   **Shape** -- Dimensions of an array.
-   **Dimension** -- Number of axes.
-   **Indexing** -- Accessing specific elements.
-   **Slicing** -- Accessing a range of elements.

------------------------------------------------------------------------

# Common Interview Questions

1.  Difference between Python List and NumPy Array.
2.  What is Broadcasting?
3.  Difference between `flatten()` and `ravel()`.
4.  Difference between `copy()` and `view()`.
5.  What is Vectorization?
6.  Difference between `np.dot()` and `@`.
7.  Difference between `reshape()` and `resize()`.
8.  What is `axis` in NumPy?

------------------------------------------------------------------------

# Quick Revision

``` python
import numpy as np

np.array()
np.zeros()
np.ones()
np.eye()
np.arange()
np.linspace()

arr.shape
arr.ndim
arr.size

arr.reshape()
arr.flatten()
arr.ravel()

np.sum()
np.mean()
np.std()
np.min()
np.max()

np.where()
np.unique()

np.concatenate()
np.vstack()
np.hstack()

np.random.rand()
np.random.randint()

np.dot()
np.linalg.inv()
```
