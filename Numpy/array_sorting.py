
# Sorting Arrays
# Sorting means putting elements in an ordered sequence.

# import numpy as np

# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))

# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))


# Sorting a 2-D Array

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))



# arg Sorting  // sorting value but gives index

x = np.array([50, 600, 10, 14])
# Indices:    0    1   2   3

indices = np.argsort(x)
print(indices)  
# Output: [2 3 0 1]