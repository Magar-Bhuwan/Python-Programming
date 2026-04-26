from functools import reduce

# lambda function is also known as anonymous function
# it is a small function that can take any number of arguments but can only have one expression
# syntax: lambda arguments: expression
# Example:
#   lambda x: x + 1
#   lambda x, y: x + y
#   lambda x, y, z: x + y + z
# lambda function are used when we need a function for a short time or single use
# for large or complex functions, we should use def
# lambda functions are often used with higher-order functions like map, filter, and reduce
# for example:  

# map() is used to apply a function to all the items in an input list
# filter() is used to filter items from a list based on a condition
# reduce() is used to apply a function cumulatively to the items of a list

#Normal function method
def addition(a, b):
    return a + b
print(addition(10, 20))

#lambda function method
x = lambda a, b: a + b
print(x(10, 20))

result = lambda x: x * x
print(result(10))


list1 = [1,2,3,4,5,6,7,8,9,10]

# using map() with lambda function
map_lambda = list(map(lambda x: x * x, list1))
print(map_lambda)

# using filter() with lambda function
filter_lambda = list(filter(lambda x: x % 2 == 0, list1))
print(filter_lambda)

# using reduce() with lambda function
reduce_lambda = reduce(lambda x, y: x + y, list1)
print(reduce_lambda)

# lambda function in if-else statements
lambda_if_else = lambda x: x + 1 if x > 0 else x - 1
print(lambda_if_else(1))
print(lambda_if_else(-1))