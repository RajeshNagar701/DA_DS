"""

NumPy Array Shape
The shape of an array is the number of elements in each dimension.
NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)    # (2, 4)


Create an array with 5 dimensions using ndmin using a vector with 
values 1,2,3,4 and verify that last dimension has value 4:

arr = np.array([1, 2, 3, 4], ndmin=5)  #  [[[[[1 2 3 4]]]]]
print(arr)
print('shape of array :', arr.shape)     # (1, 1, 1, 1, 4)	

Note : In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.


"""

# import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr.shape)    # (2, 4)



# arr = np.array([1, 2, 3, 4], ndmin=5)  #  [[[[[1 2 3 4]]]]]
# print(arr)
# print('shape of array :', arr.shape)     # (1, 1, 1, 1, 4)	

# Note : In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.




# Array Reshaping

# Reshape From 1-D to 2-D

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr) 


# Reshape From 1-D to 3-D

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)
