# Write a program to find the maximum number in a list using the reduce function/method.

from functools import reduce
n = [ 5, 70, 20, 15, 69, 23, 90, 45, 100]
max_num = reduce(lambda x, y: x if x > y else y, n)
print("Maximum number in the list: ", max_num)