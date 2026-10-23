# NumPy Array Slicing
# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5])       # [2 3 4 5]
# print(arr[4:])        # [5 6 7]
# print(arr[:4])        # [1 2 3 4]




# Negative Slicing
# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[-3:-1])     # [5 6]



# STEP   Use the step 
# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])       # [2 4]

# print(arr[::2])	# [1 3 5 7]	   step 2 start from 1 



# Slicing 2-D Arrays     
# arr[row_start:row_end, col_start:col_end]

# arr = np.array([
# 	     [1, 2, 3, 4, 5],        2 row & 5 column
# 	     [6, 7, 8, 9, 10]
# 	  ])

# print(arr[1, 1:4])      # [7 8 9]
# print(arr[0:2, 2])      # [3 8]



# Expression	Meaning
# arr[0, 2]	One element: 3
# arr[:, 2]	Third column from all rows: [3 8]
# arr[0, :]	All columns from the first row
# arr[0:2, 2]	Third column from rows 0 and 1
# arr[0:2, 1:4]	Rows 0–1 and columns 1–3
