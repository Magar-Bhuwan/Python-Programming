# Map Method in Python
# Map method is used to apply a function to each item in an iterable and return a new iterable with the results.
# The syntax for the map method is: map(function, iterable)

# Example 01:
l = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, l))
# squared = lambda x: x**2
# result = list(map(squared, l))
print(result)

# Example 02: 
words = ["hello", "world", "python"]
uppercase = list(map(str.upper, words))
print(uppercase)


# Filter method in Python
# Filter method is used to filter items from an iterable based on a function that returns True or False.
# The syntax for the filter method is: filter(function, iterable)

# Example 01:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# Reduce method in Python
# Reduce method is used to apply a function cumulatively to the items of an iterable, from left to right, to reduce the iterable to a single value.
# The syntax for the reduce method is: reduce(function, iterable)

from functools import reduce

# Example 01:
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x+y, numbers)
print("Sum of numbers: ", sum)
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers: ", product)

