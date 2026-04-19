#A technique where functions calls itself to solve a problem
#instead of using loop, recursion breaks a big problem into smaller, similar sub-problems.
#Base Case --> stops the recursion
#Recursive Case --> function calls itself

#Factorial of a number: 5! = 5 x 4 x 3 x 2 x 1

def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
         return n * fact(n-1)
    
n = int(input("Enter a number: "))
print(f"Factorial of a number {n} = ", fact(n))

