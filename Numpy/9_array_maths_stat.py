# 1. Mathematical Functions These functions perform calculations on array elements.

# a = np.array([10, 20, 30])
# b = np.array([2, 4, 5])

# Function        Simple meaning          Example
# np.add()        Addition            np.add(a, b) → [12, 24, 35]
# np.subtract()   Subtraction         np.subtract(a, b) → [8, 16, 25]
# np.multiply()   Multiplication      np.multiply(a, b) → [20, 80, 150]
# np.divide()     Division            np.divide(a, b) → [5., 5., 6.]
# np.power()      Raise to a power    np.power(a, 2) → [100, 400, 900]
# np.mod()        Remainder           np.mod(a, b) → [0, 0, 0]
# np.sqrt()       Square root         np.sqrt([4, 9, 16]) → [2., 3., 4.]
# np.exp()        Calculate \(e^x\)   np.exp([0, 1]) → [1., 2.718...]
# np.log()        Natural logarithm   np.log([1, np.e]) → [0., 1.]
# np.log10()      Base-10 logarithm   np.log10([10, 100]) → [1., 2.]


# 2. Trigonometric Functions
# These functions are used in mathematics, geometry, engineering, and scientific calculations. 
# NumPy's trigonometric functions use radians, not degrees, unless you convert the anglesfirst.


# Function        Meaning
# np.sin()        Sine of an angle
# np.cos()        Cosine of an angle
# np.tan()        Tangent of an angle
# np.arcsin()     Finds an angle from a sine value
# np.degrees()    Converts radians to degrees
# np.radians()    Converts degrees to radians

# Example:
# angles = np.array([0, 30, 90])
# r = np.radians(angles)

# print(np.sin(r))
# print(np.cos(r))

# Output (approximately):
# [0.  0.5  1. ]
# [1.  0.8660254  0.]

# Example of inverse sine:
# print(np.degrees(np.arcsin(0.5)))  # 30.0



# # ROUNDING
# # NumPy provides multiple rounding functions depending on whether you want to 
# # specify decimal places, round up, round down, or drop decimals entirely.



# Direct Comparison of NumPy Rounding Functions

# Function	           Behavior	                Example (3.7)	Example (-2.3)	Example (2.5)
# np.round(a, decimals)	Rounds to specified decimal 
# places (uses round-to-even for .5)	                     4.0	        -2.0	      2.0
# np.floor(a)	    Rounds down toward negative infinity	 3.0	        -3.0	      2.0
# np.ceil(a)	   Rounds up toward positive infinity	     4.0	        -2.0	      3.0
# np.trunc(a) / np.fix(a)	Rounds toward zero 
#                 (chops off the decimal part)	         3.0	        -2.0	      2.0
# np.rint(a)	   Rounds to the nearest integer (equivalent to np.round(a, 0))	4



# arr = np.array([1.2345, 2.6789, 3.14159])
# # Round to 2 decimal places
# print(np.round(arr, decimals=2))  
# # Output: [1.23 2.68 3.14]

