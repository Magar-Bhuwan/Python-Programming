#Write a program using recursive function for sum of first n natural numbers. 


def sum(n):
    if (n == 1):
        return 1
    return sum(n-1) + n

print(sum(5))