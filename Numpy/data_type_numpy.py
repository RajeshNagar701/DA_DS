"""

Data Types in Python
By default Python have these data types:
•	strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
•	integer - used to represent integer numbers. e.g. -1, -2, -3
•	float - used to represent real numbers. e.g. 1.2, 42.42
•	boolean - used to represent True or False.
•	complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
Below is a list of all data types in NumPy and the characters used to represent them.

•	i – integer
•	S - string
•	b - boolean
•	u - unsigned integer
•	f – float
•	c - complex float
•	m - timedelta
•	M - datetime
•	O - object
•	U - unicode string
•	V - fixed chunk of memory for other type ( void )


"""

import numpy as np

# arr = np.array([1, 2, 3, 4])
# print(arr.dtype)     # int64


# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)     # <U6

# Creating Arrays With a Defined Data Type
# arr = np.array([1, 2, 3, 4], dtype='i4')

# print(arr)                       # [1,2,3,4]
# print(arr.dtype )           # int32	


# Change data type from float to integer by using int as parameter value:

# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype(int)

# print(newarr)         # [1 2 3]
# print(newarr.dtype)   #int64
