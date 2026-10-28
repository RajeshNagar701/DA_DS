# Array Attributes

# 1. ndim — Number of dimensions
# Tells how many dimensions an array has.

# import numpy as np

# arr = np.array([[10, 20, 30],
#                 [40, 50, 60]])

# print(arr.ndim)  # Output: 2

# Task: Create a 1D array and a 3D array. Print their dimensions.


# 2. shape — Rows and columns Returns the size of each dimension.
# import numpy as np

# arr = np.array([[10, 20, 30],
#                 [40, 50, 60]])

# print(arr.shape)# Output: (2, 3)


# This means 2 rows and 3 columns.
# Task: Create a 3 × 4 array and print its shape.



# 3. size — Total number of elements

# import numpy as np
# arr = np.array([[10, 20, 30],
#                 [40, 50, 60]])

# print(arr.size)# Output: 6

# Task: Create an array containing 10 numbers and print its size.



# 4. dtype — Data type Tells the type of values stored in the array.

# import numpy as np

# arr = np.array([[10, 20, 30],
#                 [40, 50, 60]])

# print(arr.dtype)# Output: int64


# The exact integer type can vary by system.
# Task: Create arrays of integers, floats, and strings. Print their data types.


# 5. itemsize — Bytes per element
# Tells how many bytes one array element uses.


# import numpy as np

# arr = np.array([[10, 20, 30],
#                 [40, 50, 60]])

# print(arr.itemsize)# Output: commonly 8

# For example, an int64 element uses 8 bytes.
# Task: Create an int32 array and print its item size.



# 6. nbytes — Total array data memory
# Tells how many bytes the array elements occupy.

# import numpy as np

# arr = np.array([[10, 20, 30],[40, 50, 60]])
# print(arr.nbytes)# Output: commonly 48


# Calculation: 6 elements × 8 bytes = 48 bytes.
# Task: Create an array of 5 int32 elements and print nbytes.
