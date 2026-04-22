# walrus operator (:=) 
# It is used to assign a value to a variable as part of an expression.
# It is introduced in Python 3.8.

"""
Use the walrus operator when:
-------------------------------------------------
You want to avoid repeated calculations
You need a value inside a condition
You want cleaner and shorter code

When NOT to use it
-------------------------------------------------
If it makes code harder to read
In very complex expressions (can confuse others)

"""


# syntax : (varibale := expression)

# Example 1:

# Without walrus operator
n = len("Hello")
if n > 3:
    print(n)

# with walrus operator
if(n:=len("Hello"))>3:
    print(n)


# Example 2:
# Without walrus operator
line = input("Enter something: ")
while(line != "exit"):
    print(line)
    line = input("Enter something: ")

# with walrus operator
while(line:=input("Enter something: ")) != "exit":
    print(line)


# Example 3:

numbers = [1,2,3,4,5]

squares = [y for x in numbers if(y := x*x) > 10]
print(squares)