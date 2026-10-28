"""
FILLED ARRAYS

np.zeros(shape) — all zeros
np.ones(shape) — all ones
np.empty(shape) — uninitialized (garbage values)
np.eye(n) / np.identity(n) — identity matrix

Zero, One and Empty Arrays

"""


# 1) np.zeros() Meaning: Creates an array filled with zeros.

# arr = np.zeros(4)
# print(arr)

# Output: [0. 0. 0. 0.]
# Task: Create a 3 × 3 array filled with zeros.

# 2) np.ones() : Meaning: Creates an array filled with ones.
# arr = np.ones(5)
# print(arr)

# Output: [1. 1. 1. 1. 1.]
# Task: Create a 2 × 4 array filled with ones.


# 3) np.empty() : Meaning: Creates an array without initializing its values. The values may be unpredictable because the memory can contain existing data.

# arr = np.empty(3)
# print(arr)

# Output: Values are unpredictable.
# Task: Create an empty NumPy array with 6 elements.



# ====  Identity and Diagonal Arrays ===


# 4) np.eye() Meaning: Creates a 2D array with ones on the main diagonal
# and zeros elsewhere.

# arr = np.eye(3)
# print(arr)


# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
# Task: Create a 4 × 4 diagonal array using np.eye().



# 5) np.identity() Meaning: Creates a square identity matrix. 
# The number specifies both rows and columns.

# arr = np.identity(2)
# print(arr)


# Output:
# [[1. 0.]
#  [0. 1.]]
# Task: Create a 5 × 5 identity matrix.
# Remember: np.eye() allows different row and column counts, while np.identity() creates only square matrices.



