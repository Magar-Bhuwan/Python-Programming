# try-except-else
# try:    # block of code to be tested
# except: # block of code to be executed if an error occurs
# else:  # block of code to be executed if no error occurs. or it will executed if try block will executed without any error.

# Example 1: Using the try-except-else block
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception as e:
    print(e)
else:
    print("No error occurred")


