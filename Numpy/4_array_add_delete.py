"""
• append(arr, values): Appends values to the end of an array.
• insert(arr, obj, values): Inserts values along the given axis before the given indices.
• delete(arr, obj, axis): Deletes subarrays along a specific axis.


"""
# import numpy as np

# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# new_row = np.array([[7, 8, 9]])
# print(np.append(matrix,new_row, axis=0))


# # Inserts a row of zeros before index 1 (between the existing rows)
# print(np.insert(matrix, 1, [0, 0,0], axis=0))  # add in row
# print(np.insert(matrix, 1, [0, 0,0], axis=1))  # add in column


# # Deletes the element at flat index 4 (which is the number 50)
# matrix = np.array([[10, 20, 30], , 
#                    [70, 80, 90]])

# # CASE A: No axis specified (Flattens the array)
# # Deletes the element at flat index 4 (which is the number 50)
# print(np.delete(matrix, 4))
# # Output: [10, 20, 30, 40, 60, 70, 80, 90]

# # CASE B: Delete a row (axis=0)
# # Deletes the row at index 1 (the middle row:)
# print(np.delete(matrix, 1, axis=0))
# # Output:
# # [[10 20 30]
# #  [70 80 90]]

# # CASE C: Delete a column (axis=1)
# # Deletes the column at index 2 (the last column:)
# print(np.delete(matrix, 2, axis=1))
# # Output:
# # [[10 20]
# #  [40 50]
# #  [70 80]]