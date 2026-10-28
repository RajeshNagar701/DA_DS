# Random Arrays

# 1) np.random.rand() Meaning: Generates random decimal numbers between 0 and 1, excluding 1.

# arr = np.random.rand(3)
# print(arr)

# Example output: [0.23 0.76 0.41]
# Task: Generate 5 random decimal numbers.


# 2) np.random.randn()
# Meaning: Generates random numbers from a standard normal distribution, centered around 0.


# arr = np.random.randn(3)
# print(arr)


# Example output: [-0.45 0.82 1.13]
# Task: Generate a 2 × 3 array of normally distributed random numbers.



# 3) np.random.randint()
# Meaning: Generates random integers. The upper limit is excluded.


# arr = np.random.randint(1, 11, size=5)
# print(arr)

# Example output: [3 9 1 7 5]
# Task: Generate 10 random integers between 1 and 100.


# 4) np.random.choice()
# Meaning: Randomly selects values from a given list or array.

# arr = np.random.choice([10, 20, 30, 40], size=2)
# print(arr)


# Example output: [20 40]
# Task: Randomly select 3 names from a list of 5 student names.


# 5) np.random.seed()
# Meaning: Makes random results reproducible when you use the same seed and the same random operations.


# np.random.seed(10)
# print(np.random.randint(1, 100, size=5))


# output: [10 16 65 29 90]
# Run the code again with the same seed and you will get the same sequence of numbers.

