# 1). Arithmetic Operations : Arithmetic operations perform calculations on array elements element by element.


# a = np.array([10, 20, 30])
# b = np.array([2, 4, 5])

# 1. Addition +
# print(a + b)# [12 24 35]
# Task: Add [5, 10, 15] and [2, 3, 4].


# 2. Subtraction -
# print(a - b)# [ 8 16 25]
# Task: Subtract [2, 4, 6] from [10, 20, 30].

# 3. Multiplication *
# print(a * b)# [20 80 150]
# Task: Multiply [2, 3, 4] by [5, 6, 7].

# 4. Division /
# print(a / b)# [5. 5. 6.]
# Task: Divide [20, 40, 60] by [2, 4, 5].

# 5. Floor division //
# Divides and rounds down to the nearest integer value.
# print(np.array([7, 10]) // 3)# [2 3]
# Task: Perform floor division on [15, 22, 31] by 4.


# 6. Power **
# Raises each element to a power.
# print(np.array([2, 3, 4]) ** 2)# [ 4  9 16]
# Task: Calculate the cube of [2, 3, 5].


# 7. Modulus %
# Returns the remainder after division.
# print(np.array([10, 15, 20]) % 3)# [1 0 2]
# Task: Find the remainder when [12, 17, 25] is divided by 5.



# 2). Comparison Operators
# Comparison operators compare corresponding elements and return True or False.

# a = np.array([10, 20, 30])
# b = np.array([15, 20, 25])

# Operator

# == Equal to a == b → [False True False]
# != Not equal to a != b → [True False True]
# >  Greater than a > b → [False False True]
# <  Less than a < b → [True False False]
# >= Greater than or equal a >= b → [False True True]
# <= Less than or equal a <= b → [True True False]



# Example:
# marks = np.array([45, 75, 90, 30])
# print(marks >= 50)

# Output:
# [False  True  True False]



# 3). Logical Operations Logical operations combine or reverse conditions.

# 1. np.logical_and() Returns True when both conditions are true.
# marks = np.array([35, 55, 75, 95])
# print(np.logical_and(marks >= 40, marks <= 80))

# Output:
# [False  True  True False]
# Task: Find marks between 50 and 90, inclusive.


# 2. np.logical_or() Returns True when at least one condition is true.

# marks = np.array([25, 45, 65, 85])
# print(np.logical_or(marks < 30, marks > 80))

# Output:
# [ True False False  True]
# Task: Find numbers that are less than 10 or greater than 50.


# 3. np.logical_not() Reverses a Boolean result: True becomes False and vice versa.

# a = np.array([True, False, True])
# print(np.logical_not(a))

# Output:
# [False  True False]
# Task: Reverse the Boolean array [False, True, True, False].

# 4. Broadcasting
# Meaning: Broadcasting allows NumPy to perform operations between arrays of compatible shapes, even when their dimensions differ.
# Example 1: Array and single number

# a = np.array([10, 20, 30])
# print(a + 5)

# Output:
# [15 25 35]

# NumPy adds 5 to every element.
# Example 2: 2D array and 1D array

# a = np.array([[1, 2, 3],[4, 5, 6]])
# b = np.array([10, 20, 30])

# print(a + b)

# Output:
# [[11 22 33]
#  [14 25 36]]



# Aggregate operations Calculate a summary from multiple elements.

# a = np.array([10, 20, 30, 40])
# print(np.sum(a))    # 100
# print(np.mean(a))   # 25.0
# print(np.min(a))    # 10
# print(np.max(a))    # 40
# print(np.std(a))    # 11.180...


# a = np.array([[1, 2, 3],[4, 5, 6]])

# print(np.sum(a, axis=0))  # [5 7 9]
# print(np.sum(a, axis=1))  # [ 6 15]

# axis=0: calculate down the rows, producing column totals.
# axis=1: calculate across the columns, producing row totals.
