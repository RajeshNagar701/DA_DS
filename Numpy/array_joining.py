# Joining NumPy Arrays  concatenate()
# Joining means putting contents of two or more arrays in a single array

import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)   


# Join two 2-D arrays along rows (axis=1):

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)



# Joining Arrays Using Stack Functions  stack(),hstack() horizontal ,vstack() verticle, dstack convert in 2d to 3d

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)
# print(arr)





# Hstack()

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.hstack((arr1, arr2))
# print(arr)



# vstack()

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.vstack((arr1, arr2))
# print(arr)

# dstack()  covert in 2d to 3d

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dstack((a, b))

print(result)
# Output:
# [[[1 4]
#   [2 5]
#   [3 6]]]