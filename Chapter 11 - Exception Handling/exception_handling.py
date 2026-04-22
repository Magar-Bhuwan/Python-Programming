# Exception Handling
# It is use to handle runtime errors, which are not caught during compilation, i.e. logical errors
# It is very useful for file handling, database connectivity, etc.
# Syntax: try, except, else, finally

# try:    # block of code to be tested
# except: # block of code to be executed if an error occurs
# else:  # block of code to be executed if no error occurs
# finally: # block of code to be executed regardless of an error occurs

# There are so many types of exceptions:
# 1. ArithmeticError    -> Error in arithmetic operations
# 2. ZeroDivisionError  -> Division by zero
# 3. ValueError         -> Invalid value
# 4. TypeError          -> Invalid type
# 5. IndexError         -> Invalid index
# 6. KeyError           -> Invalid key
# 7. FileNotFoundError  -> File not found
# 8. Exception          -> All types of exceptions

# Example 1:
try:
    n = int(input("Enter the number: "))
    print(n)

except ValueError:
    print(e)

