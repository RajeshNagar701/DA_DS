"""
1. What is NumPy?
NumPy stands for Numerical Python. 
It is a Python library designed for efficient numerical computation and working 
with multidimensional arrays.

NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, 
and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project 
and you can use it freely.


Why is NumPy essential for Data Science?

•	In Python we have lists that serve the purpose of arrays, but they are slow to process.
•	NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
•	The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
•	Arrays are very frequently used in data science, where speed and resources are very important.
•	Efficient calculations on large collections of numbers.
•	Multidimensional arrays for structured numerical data.
•	Mathematical operations without writing explicit Python loops for every calculation.

Why is NumPy Faster Than Lists?
•	NumPy arrays are stored at one continuous place in memory unlike lists, 
    so processes can access and manipulate them very efficiently.
•	This behavior is called locality of reference in computer science.
•	This is the main reason why NumPy is faster than lists. 
    Also it is optimized to work with latest CPU architectures.

Which Language is NumPy written in?
•	NumPy is a Python library and is written partially in Python, 
    but most of the parts that require fast computation are written in C or C++.


Installing and importing NumPy

Check Python and PIP

python -m pip install numpy

"""


# import numpy as np

# arr = np.array([10, 20, 30])    

# print(arr)         # [10 20 30]
# print(type(arr))   # <class 'numpy.ndarray'>


# Note : ndarray  means N-dimensional array, the main array object provided by NumPy.

# Note : To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray

# import numpy as np
# arr = np.array((1, 2, 3, 4, 5))
# print(arr)                   # [1 2 3 4 5]



# Access 2-D Arrays

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row: ', arr[0, 1])   #2



# Access 3-D Arrays
# import numpy as np

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])   # 6




# Negative Indexing

# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('Last element from 2nd dim: ', arr[1, -1])     # 10




# python List Vs NumPy

#                         Python list             vs          NumPy array

# Feature                 Python list                         NumPy array
# Data types              Can mix types                   Usually one common dtype
# Numerical addition      Concatenates lists              Adds values element-wise
# Memory layout           Stores references to objects    Often stores homogeneous values in a compact data buffer
# Numerical workloads     Often need loops                Supports vectorized operations

