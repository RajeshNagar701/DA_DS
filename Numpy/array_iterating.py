# Iterating Arrays
# Iterating means going through elements one by one.

import numpy as np

# arr = np.array([1, 2, 3])

# for x in arr:
#   print(x)



# Iterating 2-D Arrays
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   print(x)


# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   for y in x:
#     print(y)



# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)





"""
Iterating Arrays Using nditer()
The function nditer() is a helping function that can be used from 
very basic to very advanced iterations. It solves some basic issues which we 
face in iteration, lets go through it with examples.
"""

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#   print(x)
