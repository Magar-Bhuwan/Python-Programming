# List comprehension is a concise way to create lists.
# Syntax: list = [expression for item in iterable]

# using normal method

l = [1, 2, 3, 4, 5]

square_l = []
for item in l:
    square_l.append(item*item)
print(square_l)

# using list comprehension
l = [1, 2, 3, 4, 5]
square_l = [i * i for i in l]
print(square_l)

# example 2 with conditional logic
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [item for sublist in nested_list for item in sublist if item % 2 == 0]
print(flat_list)
