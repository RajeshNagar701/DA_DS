# Creating  arrays using np.arange()
# np.arange() generates values within a specified range using a step size.  
# np.arange(start, stop, step)

# import numpy as np

# arr = np.arange(5)               # [0 1 2 3 4]        0 to 4   last number not count
# arr = np.arange(2, 10)           # [2 3 4 5 6 7 8 9]  2 to 10
# arr = np.arange(2, 11, 2)        #  [ 2  4  6  8 10]   step 2  
# arr = np.arange(10, 0, -2)       #  [10  8  6  4  2]   descending values

# print(arr)




"""
============================================================================

Creating  arrays using np.linspace()

Expert tip: Floating-point steps can introduce rounding surprises. 
For a specific number of samples between two endpoints, np.linspace()
is often more suitable


"""

import numpy as np
 
# arr = np.linspace(0, 10, 5)
# print(arr)                      # [ 0.   2.5   5.  7.5  10. ]


# arr = np.linspace(1, 6, 6)
# print(arr)	             # [1. 2. 3. 4. 5. 6.]


# Exclude the endpoint

# arr = np.linspace(0, 10, 5, endpoint=False)
# print(arr)                    # [0. 2. 4. 6. 8.]

"""

np.arange() vs np.linspace()

  Feature	            np.arange()	        np.linspace()
Main parameter	     Step size	         Number of values
Stop value	      Excluded by default	  Included by default
Best for	       Integer sequences	    Fixed-size sample sets
Example	         np.arange(0, 10, 2)	    np.linspace(0, 10, 6)

print(np.arange(1, 8, 3))       # [1 4 7]

print(np.linspace(1, 8, 3))    #  [1.  4.5 8. ]


Notice that arange() excludes 8, whereas linspace() includes it by default.


"""