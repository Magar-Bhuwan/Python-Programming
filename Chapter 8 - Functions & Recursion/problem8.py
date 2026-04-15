#Write a program using function to print multiplication table of a given number.

def multiplication(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')

n = int(input("Enter a number for multiplication: "))
multiplication(n)