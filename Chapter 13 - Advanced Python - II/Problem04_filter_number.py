# Write a program to filter a list of numbers which are divisible by 5.

# Method 1
numbers = [10, 15, 22, 30, 42, 50, 60]
divisible_num = list(filter(lambda x: x if x % 5 == 0 else None, numbers))
print(divisible_num)

# or, Method 2

def divisible5(num):
    if num % 5 == 0:
        return True
    return False
n = [10, 15, 22, 30, 42, 50, 60]
divisible_n = list(filter(divisible5, n))
print(divisible_n)
